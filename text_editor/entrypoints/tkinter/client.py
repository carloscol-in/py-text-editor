import dataclasses
import tkinter as tk
import typing as t

from text_editor.core.commands import AddCharacters
from text_editor.core.interfaces.operations import TextOperation
from text_editor.entrypoints.tkinter.operations import DeleteTextOperation, InsertTextOperation
from text_editor.entrypoints.tkinter.receiver import TkinterEditorOperationReceiver
from text_editor.entrypoints.tkinter.supported_events import SupportedTextEvent
from text_editor.service.enums import AlterationType
from text_editor.service.invoker import TextCommandInvoker


@dataclasses.dataclass(frozen=True)
class AlterationTypeCharacterTuple:
    alteration_type: AlterationType
    character: t.Optional[str]


class TextEditorClient:
    _text_editor: tk.Text
    _undo_button: tk.Button

    def __init__(
        self,
        text_editor: tk.Text,
        undo_button: tk.Button
    ):
        self._text_editor = text_editor
        self._undo_button = undo_button

        self._invoker = TextCommandInvoker()

        state = 'disabled' if self._invoker.command_stack_is_empty else 'enabled'

        self._undo_button.configure(command=self.undo, state=state)

    def _map_event_to_alteration_type_and_character(
        self,
        event: tk.Event
    ) -> t.Optional[AlterationTypeCharacterTuple]:
        alterationtype_character = None

        if event.keysym == SupportedTextEvent.BACKSPACE:
            alterationtype_character = AlterationTypeCharacterTuple(
                alteration_type=AlterationType.BACKSPACE,
                character=None
            )
        elif event.keysym == SupportedTextEvent.SPACE:
            alterationtype_character = AlterationTypeCharacterTuple(
                alteration_type=AlterationType.CHAR,
                character=' '
            )
        elif event.keysym == SupportedTextEvent.RETURN:
            alterationtype_character = AlterationTypeCharacterTuple(
                alteration_type=AlterationType.CHAR,
                character='\n'
            )
        elif event.char != '':
            alterationtype_character = AlterationTypeCharacterTuple(
                alteration_type=AlterationType.CHAR,
                character=event.char
            )
        
        return alterationtype_character
    
    def run_editor_operation(self, operation: TextOperation):
        f = getattr(self._text_editor, operation.method)
        f(**operation.to_dict())

    def write(self, event: tk.Event):
        alterationtype_character = self._map_event_to_alteration_type_and_character(
            event=event
        )

        if alterationtype_character is None:
            return
        
        alteration_type, character = (
            alterationtype_character.alteration_type,
            alterationtype_character.character
        )

        index = len(self._text_editor.get('1.0', tk.END + '-1c'))

        cursor_position = self._text_editor.index(tk.INSERT)
        row, column = (int(x) for x in cursor_position.split('.'))

        # choose the command
        if alteration_type == AlterationType.CHAR:
            command = AddCharacters(
                index=index,
                row=row,
                column=column,
                characters=character,
                receiver=TkinterEditorOperationReceiver()
            )
        else:
            # ignore unsupported char types
            return

        operation: InsertTextOperation = self._invoker.invoke(command=command)

        self.run_editor_operation(operation)
            
        if self._undo_button['state'] == 'disabled':
            self._undo_button.configure(state='normal')

        # override normal use, let editor_manager handle the text
        return 'break'
    
    def undo(self):
        operation: DeleteTextOperation = self._invoker.rollback()

        if operation is None:
            return

        self.run_editor_operation(operation)

        index = operation.index1

        # set cursor at place before writing the characters
        self._text_editor.mark_set('insert', index)

        # disable 'undo' button if commands stack is empty
        if self._invoker.command_stack_is_empty:
            self._undo_button.configure(state='disabled')

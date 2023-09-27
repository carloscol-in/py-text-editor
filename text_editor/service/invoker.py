import tkinter as tk
import typing as t

from text_editor.core.commands import AddCharactersToText, BaseEditorAlteration
from text_editor.service.editor_operation_receiver import EditorOperationReceiver
from text_editor.service.alteration_types import AlterationTypes
from text_editor.service.utils import get_alteration_type_and_value


class TextCommandInvoker:
    _text_editor: tk.Text
    commands: t.List[BaseEditorAlteration] = []

    def __init__(self, text_editor: tk.Text):
        self._text_editor = text_editor

    def __call__(self, event: tk.Event):
        alteration_type, value = get_alteration_type_and_value(event)

        index = self._text_editor.index(tk.INSERT)

        if alteration_type == AlterationTypes.CHAR:
            command = AddCharactersToText(
                index=index,
                characters=value
            )
        else:
            # ignore unsupported char types
            return

        self.commands.append(command)
        text_operation = command.do()

        editor_manager = EditorOperationReceiver.manage_editor_with_text_operation(
            editor=self._text_editor,
            text_operation=text_operation
        )

        editor_manager.run()

        # override normal use, let editor_manager handle the text
        return 'break'
    
    def undo(self):
        if len(self.commands) == 0:
            return
        
        command = self.commands.pop()
        
        text_operation = command.undo()

        editor_manager = EditorOperationReceiver.manage_editor_with_text_operation(
            editor=self._text_editor,
            text_operation=text_operation
        )

        editor_manager.run()

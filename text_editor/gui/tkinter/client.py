import tkinter as tk
import typing as t

from text_editor.core.commands import AddCharacters
from text_editor.core.receiver import EditorOperationReceiver
from text_editor.service.enums import AlterationTypes
from text_editor.service.models import EditorOperation
from text_editor.service.invoker import TextCommandInvoker
from text_editor.service.utils import get_alteration_type_and_value


class TextEditorClient:
    _text_editor: tk.Text

    def __init__(self, text_editor: tk.Text):
        self._text_editor = text_editor
        self._invoker = TextCommandInvoker()
    
    def run_editor_operation(self, operation: EditorOperation):
        f = getattr(self._text_editor, operation.method)
        f(**operation.kwargs)

    def write(self, event: tk.Event):
        alteration_type, value = get_alteration_type_and_value(event)

        index = self._text_editor.index(tk.INSERT)

        # choose the command
        if alteration_type == AlterationTypes.CHAR:
            command = AddCharacters(
                index=index,
                characters=value,
                receiver=EditorOperationReceiver()
            )
        else:
            # ignore unsupported char types
            return

        text_operation = self._invoker.invoke(command=command)

        editor_operation = EditorOperation.from_text_operation(
            operation=text_operation
        )

        self.run_editor_operation(editor_operation)

        # override normal use, let editor_manager handle the text
        return 'break'
    
    def undo(self):
        text_operation = self._invoker.rollback()

        if text_operation is None:
            return

        editor_operation = EditorOperation.from_text_operation(
            operation=text_operation
        )

        self.run_editor_operation(editor_operation)

import tkinter as tk
import typing as t

from text_editor.core.commands import BaseEditorAlteration
from text_editor.core.operations import TextOperation


class TextCommandInvoker:
    _text_editor: tk.Text
    commands: t.List[BaseEditorAlteration] = []

    def invoke(self, command: BaseEditorAlteration) -> TextOperation:
        self.commands.append(command)

        text_operation = command.do()

        return text_operation
    
    def rollback(self) -> TextOperation:
        if len(self.commands) == 0:
            return
        
        command = self.commands.pop()
        
        text_operation = command.undo()

        return text_operation

import tkinter as tk
import typing as t

from text_editor.core.commands import BaseEditorAlteration
from text_editor.core.operations import TextOperation


class TextCommandInvoker:
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
    
    @property
    def command_stack_is_empty(self) -> bool:
        return len(self.commands) == 0

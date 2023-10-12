import tkinter as tk
import typing as t

from text_editor.core.commands import BaseEditorAlteration
from text_editor.core.interfaces.operations import TextOperation


class TextCommandInvoker:
    commands: t.List[BaseEditorAlteration] = []

    def invoke(self, command: BaseEditorAlteration) -> TextOperation:
        self.commands.append(command)

        return command.do()
    
    def rollback(self) -> TextOperation:
        if self.command_stack_is_empty:
            return
        
        command = self.commands.pop()

        return command.undo()
    
    @property
    def command_stack_is_empty(self) -> bool:
        return len(self.commands) == 0

import tkinter as tk
import typing as t

from text_editor.core.commands import AddCharacters, BaseEditorAlteration
from text_editor.core.operations import TextOperation
from text_editor.service.editor_operation_receiver import EditorOperationReceiver
from text_editor.service.enums import AlterationTypes
from text_editor.service.utils import get_alteration_type_and_value


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

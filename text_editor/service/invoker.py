import tkinter as tk
import typing as t
import string

from text_editor.core.commands import AddCharactersToText, BaseEditorAlteration
from text_editor.service.editor_operation_manager import EditorOperationManager
from text_editor.service.enums import AlterationTypes, SupportedEventSymbols


class Invoker:
    _text_editor: tk.Text
    commands: t.List[BaseEditorAlteration] = []

    def __init__(self, text_editor: tk.Text):
        self._text_editor = text_editor

    @staticmethod
    def get_alteration_type_and_value(event):
        t = None
        v = None

        key = event.keysym

        if key in string.ascii_letters + string.digits + string.punctuation:
            t = AlterationTypes.CHAR
            v = event.char
        elif key == SupportedEventSymbols.BACKSPACE:
            t = AlterationTypes.BACKSPACE
        elif key == SupportedEventSymbols.SPACE:
            t = AlterationTypes.CHAR
            v = event.char

        return t, v

    def __call__(self, event: tk.Event):
        text = str(self._text_editor.get(1.0, tk.END + '-1c'))

        alteration_type, value = self.get_alteration_type_and_value(event)

        index = self._text_editor.index(tk.INSERT)

        if alteration_type == AlterationTypes.CHAR:
            command = AddCharactersToText(
                index=index,
                characters=value
            )
        else:
            # ignore unsupported char types
            return 'break'

        self.commands.append(command)
        text_operation = command.run()

        editor_manager = EditorOperationManager.manage_editor_with_text_operation(
            editor=self._text_editor,
            text_operation=text_operation
        )

        editor_manager.run()

        # override normal use, let editor_manager handle the text
        return 'break'
    
    def undo(self):
        command = self.commands.pop()
        
        text_operation = command.undo()

        editor_manager = EditorOperationManager.manage_editor_with_text_operation(
            editor=self._text_editor,
            text_operation=text_operation
        )

        editor_manager.run()

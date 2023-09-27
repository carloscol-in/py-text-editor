import tkinter as tk
import typing as t

from text_editor.core.operations import TextOperation


class EditorOperationManager:
    _method: str

    def __init__(
        self,
        editor: tk.Text,
        method: str,
        kwargs: t.List[t.Dict[str, any]]
    ):
        self._editor = editor
        self._method = method
        self._kwargs = kwargs

    @classmethod
    def manage_editor_with_text_operation(
        cls,
        editor: tk.Text,
        text_operation: TextOperation
    ) -> 'EditorOperationManager':
        return cls(
            editor = editor,
            method = text_operation.operation,
            kwargs = text_operation.to_dict()
        )
    
    def run(self):
        f = getattr(self._editor, self._method)
        f(**self._kwargs)

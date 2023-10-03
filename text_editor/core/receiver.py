import tkinter as tk
import typing as t

from text_editor.core.operations import DeleteTextOperation, InsertTextOperation, TextOperation


class EditorOperationReceiver:

    def insert(self, index: str, characters: str) -> InsertTextOperation:
        return InsertTextOperation(
            index=index,
            characters=characters
        )
    
    def delete(self, index: str, characters: str) -> DeleteTextOperation:
        return DeleteTextOperation(
            index=index,
            characters=characters
        )

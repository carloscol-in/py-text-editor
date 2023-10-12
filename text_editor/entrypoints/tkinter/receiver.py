import abc
import tkinter as tk
import typing as t

from text_editor.entrypoints.tkinter.operations import DeleteTextOperation, InsertTextOperation
from text_editor.core.interfaces.receiver import EditorOperationReceiver



class TkinterEditorOperationReceiver(EditorOperationReceiver):

    def insert(
        self,
        row: int,
        column: int,
        characters: str,
        **kwargs: t.Dict
    ) -> InsertTextOperation:
        idx = f'{row}.{column}'

        return InsertTextOperation(
            index=idx,
            chars=characters
        )
    
    def delete(
        self,
        row: int,
        column: int,
        characters: str,
        **kwargs: t.Dict
    ) -> DeleteTextOperation:
        text_length = len(characters)

        index1 = f'{row}.{column}'
        index2 = f'{row}.{column + text_length}'

        return DeleteTextOperation(
            index1=index1,
            index2=index2
        )

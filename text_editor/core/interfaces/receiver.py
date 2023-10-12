import abc
import tkinter as tk
import typing as t

from text_editor.core.interfaces.operations import TextOperation



class EditorOperationReceiver(abc.ABC):

    @abc.abstractmethod
    def insert(
        self,
        index: int,
        row: int,
        column: int,
        characters: str
    ) -> TextOperation:
        ...
    
    @abc.abstractmethod
    def delete(
        self,
        index: int,
        row: int,
        column: int,
        characters: str
    ) -> TextOperation:
        ...

import abc

from .operations import (
    TextOperation,
    InsertTextOperation,
    DeleteTextOperation
)
    

class BaseEditorAlteration(abc.ABC):
    @abc.abstractmethod
    def run(self) -> TextOperation:
        ...

    @abc.abstractmethod
    def undo(self) -> TextOperation:
        ...


class AddCharactersToText(BaseEditorAlteration):
    def __init__(
            self,
            index: str,
            characters: str
        ):
        self._index = index
        self._characters = characters

    def run(self) -> InsertTextOperation:
        return InsertTextOperation(
            index=self._index,
            value=self._characters
        )

    def undo(self) -> InsertTextOperation:
        return DeleteTextOperation(
            index=self._index,
            value=self._characters
        )
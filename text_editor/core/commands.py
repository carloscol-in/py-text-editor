import abc

from text_editor.core.interfaces.receiver import EditorOperationReceiver

from .interfaces.operations import (
    TextOperation,
)


class CommandMetadata:
    ...
    

class BaseEditorAlteration(abc.ABC):

    _receiver: EditorOperationReceiver
    index: int
    row: int
    column: int
    characters: str

    def __init__(
        self,
        characters: str,
        index: int,
        row: int,
        column: int,
        receiver: EditorOperationReceiver
    ):
        self.characters = characters
        self.index = index
        self.row = row
        self.column = column
        self._receiver = receiver

    @abc.abstractmethod
    def do(self) -> TextOperation:
        ...

    @abc.abstractmethod
    def undo(self) -> TextOperation:
        ...


class AddCharacters(BaseEditorAlteration):

    def __init__(
        self,
        characters: str,
        index: int,
        row: int,
        column: int,
        receiver: EditorOperationReceiver
    ):
        super().__init__(
            characters,
            index,
            row,
            column,
            receiver
        )

    def __str__(self):
        return f'[{self.index}]--{self.characters}'

    def do(self) -> TextOperation:
        return self._receiver.insert(
            index=self.index,
            row=self.row,
            column=self.column,
            characters=self.characters
        )

    def undo(self) -> TextOperation:
        return self._receiver.delete(
            index=self.index,
            row=self.row,
            column=self.column,
            characters=self.characters
        )

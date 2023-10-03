import abc

from text_editor.core.receiver import EditorOperationReceiver

from .operations import (
    TextOperation,
    InsertTextOperation,
    DeleteTextOperation
)
    

class BaseEditorAlteration(abc.ABC):
    _receiver: EditorOperationReceiver
    index: str
    characters: str

    @abc.abstractmethod
    def do(self) -> TextOperation:
        ...

    @abc.abstractmethod
    def undo(self) -> TextOperation:
        ...


class AddCharacters(BaseEditorAlteration):
    def __init__(
            self,
            index: str,
            characters: str,
            receiver: EditorOperationReceiver
        ):
        self.index = index
        self.characters = characters
        self._receiver = receiver

    def __str__(self):
        return f'[{self.index}]--{self.characters}'

    def do(self) -> InsertTextOperation:
        return self._receiver.insert(
            index=self.index,
            characters=self.characters
        )

    def undo(self) -> DeleteTextOperation:
        return self._receiver.delete(
            index=self.index,
            characters=self.characters
        )

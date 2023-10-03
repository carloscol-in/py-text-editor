import abc
import dataclasses


@dataclasses.dataclass(frozen=True)
class TextOperation(abc.ABC):
    index: str


@dataclasses.dataclass(frozen=True)
class InsertTextOperation(TextOperation):
    characters: str


@dataclasses.dataclass(frozen=True)
class DeleteTextOperation(TextOperation):
    characters: str

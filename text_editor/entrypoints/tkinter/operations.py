import dataclasses

from text_editor.core.interfaces.operations import TextOperation


@dataclasses.dataclass(frozen=True)
class InsertTextOperation(TextOperation):
    index: str
    chars: str
    method: str = dataclasses.field(default='insert', init=False)

    def to_dict(self):
        return {
            'index': self.index,
            'chars': self.chars
        }


@dataclasses.dataclass(frozen=True)
class DeleteTextOperation(TextOperation):
    index1: str
    index2: str
    method: str = dataclasses.field(default='delete', init=False)

    def to_dict(self):
        return {
            'index1': self.index1,
            'index2': self.index2
        }

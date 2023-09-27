import abc
import dataclasses


@dataclasses.dataclass(frozen=True)
class TextOperation(abc.ABC):
    index: str

    @property
    @abc.abstractmethod
    def operation(self):
        ...

    @abc.abstractmethod
    def to_dict(self):
        return {
            'index': self.index
        }


@dataclasses.dataclass(frozen=True)
class InsertTextOperation(TextOperation):
    value: str

    @property
    def operation(self):
        return 'insert'

    def to_dict(self):
        default_dict = super().to_dict()

        return {
            **default_dict,
            'chars': self.value
        }


@dataclasses.dataclass(frozen=True)
class DeleteTextOperation(TextOperation):
    value: str

    @property
    def operation(self):
        return 'delete'
    
    @property
    def text_length(self):
        return len(self.value)
    
    @staticmethod
    def calculate_end_index(start_index: str, text_length: int):
        return f'{start_index.split(".")[0]}.{int(start_index.split(".")[1]) + text_length}'

    def to_dict(self):
        return {
            'index1': self.index,
            'index2': self.calculate_end_index(self.index, self.text_length)
        }

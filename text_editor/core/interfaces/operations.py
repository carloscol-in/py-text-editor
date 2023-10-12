import abc
import dataclasses


@dataclasses.dataclass(frozen=True)
class TextOperation(abc.ABC):
    method: str = dataclasses.field(init=False)

    @abc.abstractmethod
    def to_dict():
        ...

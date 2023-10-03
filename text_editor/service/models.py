import dataclasses
import typing as t
from text_editor.core.operations import (
    TextOperation,
    InsertTextOperation,
    DeleteTextOperation
)


@dataclasses.dataclass(frozen=True)
class EditorOperation:
    method: str
    kwargs: t.Dict

    @staticmethod
    def _parse_kwargs_for_insert_operation(operation: InsertTextOperation) -> t.Dict:
        return {
            'index': operation.index,
            'chars': operation.characters
        }

    @staticmethod
    def _parse_kwargs_for_delete_operation(operation: DeleteTextOperation) -> t.Dict:
        start_index = operation.index

        text_length = len(operation.characters)

        end_index = f'{start_index.split(".")[0]}.{int(start_index.split(".")[1]) + text_length}'

        return {
            'index1': start_index,
            'index2': end_index
        }

    @classmethod
    def from_text_operation(cls, operation: TextOperation):
        method = None
        
        if isinstance(operation, InsertTextOperation):
            method = 'insert'
            kwargs = cls._parse_kwargs_for_insert_operation(operation=operation)
        elif isinstance(operation, DeleteTextOperation):
            method = 'delete'
            kwargs = cls._parse_kwargs_for_delete_operation(operation=operation)
        else:
            raise Exception('Couldnt map operation.')
        
        return cls(
            method=method,
            kwargs=kwargs
        )

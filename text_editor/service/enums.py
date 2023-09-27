import enum


class AlterationTypes(enum.StrEnum):
    CHAR = enum.auto()
    BACKSPACE = 'BackSpace'


class SupportedEventSymbols(enum.StrEnum):
    BACKSPACE = 'BackSpace'
    SPACE = 'space'

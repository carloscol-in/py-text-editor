import string

from text_editor.service.alteration_types import AlterationTypes
from text_editor.gui.tkinter.supported_events import SupportedTextEvents


def get_alteration_type_and_value(event):
    t = None
    v = None

    key = event.keysym

    if key in string.ascii_letters + string.digits + string.punctuation:
        t = AlterationTypes.CHAR
        v = event.char
    elif key == SupportedTextEvents.BACKSPACE:
        t = AlterationTypes.BACKSPACE
    elif key == SupportedTextEvents.SPACE:
        t = AlterationTypes.CHAR
        v = event.char

    return t, v

import tkinter as tk

from text_editor.service.invoker import TextCommandInvoker


def create_app():
    root = tk.Tk()

    root.title('Text Editor')
    root.geometry('500x300')

    # define canvas
    canvas = tk.Canvas(root, width=300, height=500)
    canvas.pack(fill='both', expand=True)

    # create Text component
    text_editor = tk.Text(root, font=('Helvetica', 14), fg='#ECF6FC', bg='#27272C', bd=0)

    # define Invoker
    invoker = TextCommandInvoker(text_editor=text_editor)

    # create Undo button component
    undo_button = tk.Button(root, text='Undo', command=invoker.undo)
    undo_button.place(x=10, y=10)

    # bindings
    text_editor.bind('<Key>', invoker)

    canvas.create_window(34, 50, anchor='nw', width=300, height=200, window=text_editor)

    return root

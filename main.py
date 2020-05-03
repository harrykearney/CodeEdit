from tkinter import Tk, Label, Text, Button, Scrollbar, filedialog
import tkinter

class Menubar:

    def __init__(self, parent):
        font_specs = ('Calibri', 9)

        menubar = tkinter.Menu(parent.window)
        parent.window.config(menu=menubar)

        file_dropdown = tkinter.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label='New File',
                                    accellerator='CTRL+N',
                                    command=parent.new_file)
        file_dropdown.add_command(label='Open File',
                                    accellerator='CTRL+O',
                                    command=parent.open_file)
        file_dropdown.add_command(label='Save',
                                    accellerator='CTRL+S',
                                    command=parent.save)
        file_dropdown.add_command(label='Save As',
                                    accellerator='CTRL+SHIFT+S',
                                    command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label='Exit',
                                    accellerator='CTRL+Q',
                                    command=parent.window.destroy)

        menubar.add_cascade(label='File', menu=file_dropdown)
        
class Statusbar:

    def __init__(self, parent):

        font_specs = ('Calibri', 11)
        
        self.status = tkinter.StringVar()
        self.status.set('CodeEdit - 0.1')

        label = tkinter.Label(parent.textarea, textvariable=self.status, fg='black',
                                bg='lightgrey', anchor='sw', font=font_specs)

        label.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)

class CodeEdit:

    def __init__(self, window):
        window.title('Untitled - CodeEdit')
        window.geometry('960x540')

        font_specs = ('Calibri', 11)

        self.window = window
        self.filename = None

        self.textarea = Text(window, font=font_specs)
        self.scroll = Scrollbar(window, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.menubar = Menubar(self)
        self.statusbar = Statusbar(self)

    def set_window_title(self, name=None):
        if name:
            self.window.title(f'{name} - CodeEdit')
        else:
            self.window.title('Untitled - CodeEdit')

    def new_file(self):
        self.textarea.delete(1.0, tkinter.END)
        self.filename = None
        self.set_window_title()

    def open_file(self):
        self.filename = filedialog.askopenfilename(
            defaultextension='.txt',
            filetypes=[('All Files', '*.*'),
                        ('Text Files', '*.txt'),
                        ('Python Scripts', '*.py'),
                        ('Markdown Documents', '*.md'),
                        ('JavaScript Files', '*.js'),
                        ('HTML Documents', '*.html'),
                        ('CSS Documents', '*.css')]
        )
        if self.filename:
            self.textarea.delete(1.0, tkinter.END) 
            with open(self.filename, 'r') as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)

    def save(self):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tkinter.END)
                with open(self.filename, 'w') as f:
                    f.write(textarea_content)
            except Exception as e:
                print(e)
        else:
            self.save_as() 

    def save_as(self):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                           ("Text Files", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Documents", "*.md"),
                           ("JavaScript Files", "*.js"),
                           ("HTML Documents", "*.html"),
                           ("CSS Documents", "*.css")])
            textarea_content = self.textarea.get(1.0, tkinter.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    window = Tk()
    ce = CodeEdit(window)
    window.mainloop() 
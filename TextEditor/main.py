import tkinter as tk
from tkinter import filedialog
from tkinter import font

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title('Text Editor')

        # Create a menu bar
        menu_bar = tk.Menu(master)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=master.quit)
        menu_bar.add_cascade(label='File', menu=file_menu)
        master.config(menu=menu_bar)

        # Create a toolbar for formatting options
        toolbar = tk.Frame(master)
        toolbar.pack(side='top', fill='x')
        bold_button = tk.Button(toolbar, text='Bold', command=self.bold_text)
        bold_button.pack(side='left')
        italic_button = tk.Button(toolbar, text='Italic', command=self.italic_text)
        italic_button.pack(side='left')
        underline_button = tk.Button(toolbar, text='Underline', command=self.underline_text)
        underline_button.pack(side='left')
        
        # Add a "Save" button that calls the save_file method
        self.save_button = tk.Button(self.master, text='Save', command=self.save_file)
        self.save_button.pack(side='bottom', fill='x')

        # Create a text area for editing text
        self.text = tk.Text(master)
        self.text.pack(side='bottom', fill='both', expand=True)
        self.text.config(wrap='word')
        self.text.focus_set()

        # Initialize the font settings
        self.bold = False
        self.italic = False
        self.underline = False
        self.font = font.Font(family='Arial', size=12)


    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
            self.text.delete('1.0', tk.END)
            self.text.insert('1.0', text)


    def bold_text(self):
        self.bold = not self.bold
        self.update_font()


    def italic_text(self):
        self.italic = not self.italic
        self.update_font()


    def underline_text(self):
        self.underline = not self.underline
        self.update_font()


    def update_font(self):
        new_font = font.Font(family='Arial', size=12, weight='normal', slant='roman', underline=0)
        if self.bold:
            new_font.configure(weight='bold')
        if self.italic:
            new_font.configure(slant='italic')
        if self.underline:
            new_font.configure(underline=1)
        self.font = new_font
        self.text.tag_configure('font', font=new_font)
        self.text.tag_add('font', '1.0', tk.END)
        
        
    def save_file(self):
        # Ask the user to choose a file to save to
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', initialdir='/path/to/local/folder/')
        if file_path:
            # If the user selected a file, open it and write the text to it
            with open(file_path, 'w') as file:
                text = self.text.get('1.0', tk.END)
                file.write(text)

if __name__ == '__main__':
    # Create a new tkinter window and initialize a TextEditor instance
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk

class PaintApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")

        # Create canvas
        self.canvas = Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Add drawing tools
        self.pencil_button = Button(root, text="Pencil", command=self.use_pencil)
        self.pencil_button.pack(side=LEFT)

        self.brush_button = Button(root, text="Brush", command=self.use_brush)
        self.brush_button.pack(side=LEFT)

        self.eraser_button = Button(root, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack(side=LEFT)

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.draw)

        # Add file menu
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Open", command=self.open_file)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

        # Initialize variables
        self.current_tool = "pencil"
        self.lastx, self.lasty = None, None
        self.color = "black"
        self.eraser_size = 20
        self.pencil_size = 2
        self.brush_size = 10

    def use_pencil(self):
        self.current_tool = "pencil"

    def use_brush(self):
        self.current_tool = "brush"

    def use_eraser(self):
        self.current_tool = "eraser"

    def draw(self, event):
        if self.lastx and self.lasty:
            if self.current_tool == "pencil":
                self.canvas.create_line(self.lastx, self.lasty, event.x, event.y, width=self.pencil_size, fill=self.color)
            elif self.current_tool == "brush":
                self.canvas.create_oval(event.x - self.brush_size, event.y - self.brush_size, event.x + self.brush_size, event.y + self.brush_size, fill=self.color, outline=self.color)
            elif self.current_tool == "eraser":
                self.canvas.create_rectangle(event.x - self.eraser_size, event.y - self.eraser_size, event.x + self.eraser_size, event.y + self.eraser_size, fill="white", outline="white")
        self.lastx, self.lasty = event.x, event.y

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            self.canvas.postscript(file=file_path + ".eps")
            img = Image.open(file_path + ".eps")
            img.save(file_path)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.canvas.delete("all")
            img = Image.open(file_path)
            self.canvas.image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")


if __name__ == "__main__":
    root = Tk()
    PaintApp(root)
    root.mainloop()

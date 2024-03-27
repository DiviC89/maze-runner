from tkinter import BOTH, Canvas, Tk


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, first: Point, second: Point) -> None:
        self.first = first
        self.second = second

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.first.x,
            self.first.y,
            self.second.x,
            self.second.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack()


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title("Mase Runner")
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: Line, fill_color):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False


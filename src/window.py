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
        canvas.pack(fill=BOTH, expand=1)


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


class Cell:
    def __init__(self, x1, y1, x2, y2, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            left_wall = Line(
                Point(self._x1 - 15, self._y1 - 15),
                Point(self._x2 - 25, self._y2 + 15),
            )
            self._win.draw_line(left_wall, "green")
        if self.has_right_wall:
            right_wall = Line(
                Point(self._x1 + 25, self._y1 - 15), Point(self._x2 + 15, self._y2 + 15)
            )
            self._win.draw_line(right_wall, "green")
        if self.has_top_wall:
            top_wall = Line(
                Point(self._x1 - 15, self._y1 - 15),
                Point(self._x2 + 15, self._y2 - 15),
            )
            self._win.draw_line(top_wall, "green")
        if self.has_bottom_wall:
            bottom_wall = Line(
                Point(self._x1 - 15, self._y1 + 15),
                Point(self._x2 + 15, self._y2 + 15),
            )
            self._win.draw_line(bottom_wall, "green")


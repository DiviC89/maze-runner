from window import Line, Point, Window


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(100, 200), Point(200, 35)), "red")
    win.wait_for_close()


main()


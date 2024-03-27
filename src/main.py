from window import Cell, Window


def main():
    win = Window(800, 600)
    cells = []
    for x in range(30, 800, 80):
        for y in range(20, 600, 60):
            cells.append(Cell(x - 5, y - 10, x + 5, y - 10, win))

    for cell in cells:
        cell.draw()
    win.wait_for_close()


main()


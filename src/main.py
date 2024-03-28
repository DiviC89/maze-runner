from window import Cell, Window


def main():
    win = Window(800, 600)
    cells = []
    for x in range(30, 400, 80):
        cells.append([])
        for y in range(20, 300, 60):
            cells[len(cells) - 1].append(Cell(x, y, x, y, win))

    for y in range(len(cells)):
        for x in range(len(cells[y])):
            cells[y][x].draw()
            if x % 2 == 0 and y % 4 == 0:
                cells[y][x].draw_move(cells[y][x - 1])
    win.wait_for_close()


main()


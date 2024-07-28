import curses

def main(stdscr):
    # Отключаем отображение курсора
    curses.curs_set(0)

    # Инициализируем цветовые пары
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLUE)

    # Получаем размер окна
    height, width = stdscr.getmaxyx()

    # Отображаем текст с разными цветовыми парами
    stdscr.addstr(1, width//2 - 10, "Red on White", curses.color_pair(1))
    stdscr.addstr(3, width//2 - 10, "Green on Black", curses.color_pair(2))
    stdscr.addstr(5, width//2 - 10, "Yellow on Blue", curses.color_pair(3))

    # Обновляем экран
    stdscr.refresh()

    # Ожидаем нажатия любой клавиши
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)

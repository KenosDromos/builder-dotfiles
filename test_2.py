import curses

def draw_menu(stdscr, menu_items, current_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    # Drawing border
    stdscr.border(0)

    # Title
    title = "Main Menu"
    stdscr.addstr(1, w // 2 - len(title) // 2, title, curses.A_BOLD)

    for idx, row in enumerate(menu_items):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu_items) // 2 + idx
        if idx == current_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def input_box(stdscr, prompt):
    curses.echo()
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(h // 2, w // 2 - len(prompt) // 2, prompt)
    stdscr.refresh()
    input = stdscr.getstr(h // 2 + 1, w // 2 - len(prompt) // 2, 20)
    return input.decode('utf-8')

def show_stdscr_info(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    info = dir(stdscr)
    stdscr.addstr(0, 0, "stdscr attributes and methods:")
    for idx, item in enumerate(info):
        stdscr.addstr(idx + 1, 0, item)
    stdscr.refresh()
    stdscr.getch()

def main_menu(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    current_row_idx = 0
    menu_items = ['Option 1', 'Option 2', 'Option 3', 'Show stdscr Info', 'Enter Text', 'Exit']
    
    draw_menu(stdscr, menu_items, current_row_idx)

    while True:
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu_items) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu_items[current_row_idx] == 'Exit':
                break
            elif menu_items[current_row_idx] == 'Show stdscr Info':
                show_stdscr_info(stdscr)
            elif menu_items[current_row_idx] == 'Enter Text':
                text = input_box(stdscr, "Enter your text: ")
                stdscr.clear()
                stdscr.addstr(0, 0, f"You entered: {text}", curses.color_pair(3))
                stdscr.refresh()
                stdscr.getch()
            else:
                stdscr.clear()
                stdscr.addstr(0, 0, f"You selected '{menu_items[current_row_idx]}'", curses.color_pair(2))
                stdscr.refresh()
                stdscr.getch()
            draw_menu(stdscr, menu_items, current_row_idx)

        draw_menu(stdscr, menu_items, current_row_idx)

def sub_menu(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    current_row_idx = 0
    menu_items = ['Sub Option 1', 'Sub Option 2', 'Back']
    
    draw_menu(stdscr, menu_items, current_row_idx)

    while True:
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu_items) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row_idx == len(menu_items) - 1:
                break
            else:
                stdscr.clear()
                stdscr.addstr(0, 0, f"You selected '{menu_items[current_row_idx]}'", curses.color_pair(3))
                stdscr.refresh()
                stdscr.getch()
                draw_menu(stdscr, menu_items, current_row_idx)

        draw_menu(stdscr, menu_items, current_row_idx)

if __name__ == "__main__":
    curses.wrapper(main_menu)

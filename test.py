import curses

class BaseScreen:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.init_curses()

    def init_curses(self):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    def draw(self):
        raise NotImplementedError("Subclasses should implement this!")

    def handle_input(self, key):
        raise NotImplementedError("Subclasses should implement this!")

    def run(self):
        while True:
            self.draw()
            key = self.stdscr.getch()
            if not self.handle_input(key):
                break

class MenuScreen(BaseScreen):
    def __init__(self, stdscr, menu_items):
        super().__init__(stdscr)
        self.menu_items = menu_items
        self.current_row_idx = 0

    def draw(self):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        # Drawing border
        self.stdscr.border(0)

        # Title
        title = self.get_title()
        self.stdscr.addstr(1, w // 2 - len(title) // 2, title, curses.A_BOLD)

        for idx, row in enumerate(self.menu_items):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(self.menu_items) // 2 + idx
            if idx == self.current_row_idx:
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, row)
                self.stdscr.attroff(curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, row)
        self.stdscr.refresh()

    def handle_input(self, key):
        if key == curses.KEY_UP and self.current_row_idx > 0:
            self.current_row_idx -= 1
        elif key == curses.KEY_DOWN and self.current_row_idx < len(self.menu_items) - 1:
            self.current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return self.select_item(self.current_row_idx)
        return True

    def select_item(self, index):
        raise NotImplementedError("Subclasses should implement this!")

    def get_title(self):
        return "Menu"

class MainMenu(MenuScreen):
    def __init__(self, stdscr):
        menu_items = ['Option 1', 'Option 2', 'Submenu', 'Enter Text', 'Exit']
        super().__init__(stdscr, menu_items)

    def get_title(self):
        return "Main Menu"

    def select_item(self, index):
        if index == 4:  # Exit
            return False
        elif index == 2:  # Submenu
            SubMenu(self.stdscr).run()
        elif index == 3:  # Enter Text
            text = InputScreen(self.stdscr, "Enter your text:").run()
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"You entered: {text}", curses.color_pair(3))
            self.stdscr.refresh()
            self.stdscr.getch()
        else:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"You selected '{self.menu_items[index]}'", curses.color_pair(2))
            self.stdscr.refresh()
            self.stdscr.getch()
        return True

class SubMenu(MenuScreen):
    def __init__(self, stdscr):
        menu_items = ['Sub Option 1', 'Sub Option 2', 'Back']
        super().__init__(stdscr, menu_items)

    def get_title(self):
        return "Sub Menu"

    def select_item(self, index):
        if index == 2:  # Back
            return False
        else:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"You selected '{self.menu_items[index]}'", curses.color_pair(3))
            self.stdscr.refresh()
            self.stdscr.getch()
        return True

class InputScreen(BaseScreen):
    def __init__(self, stdscr, prompt):
        super().__init__(stdscr)
        self.prompt = prompt
        self.input_text = ""

    def draw(self):
        curses.echo()
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        self.stdscr.addstr(h // 2, w // 2 - len(self.prompt) // 2, self.prompt)
        self.stdscr.refresh()
        self.input_text = self.stdscr.getstr(h // 2 + 1, w // 2 - len(self.prompt) // 2, 20).decode('utf-8')

    def handle_input(self, key):
        return False  # Exit after input

    def run(self):
        super().run()
        return self.input_text

def main(stdscr):
    MainMenu(stdscr).run()

if __name__ == "__main__":
    curses.wrapper(main)

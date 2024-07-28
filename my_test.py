import curses
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Tuple, Any


from builder.core.types import Vector2, BBox

class Direction(Enum):
    VERTICAL = 'vertical'
    HORIZONTAL = 'horizontal'

class Controller:
    def __init__(self,
                 cursor = Vector2(0, 0),
                 limit = Vector2(0, 0),
                 direction = Direction.VERTICAL,
                 is_2d = False,
                ):
        self.cursor = cursor
        self.limit = limit
        self.direction = direction
        self.is_2d = is_2d
        self.enter = False

        self.keys = {}
        self._init_keys()
    
    def _init_keys(self):
        keys = {
            Direction.VERTICAL: {
                curses.KEY_UP:    (lambda: self.cursor.x > 0, lambda: self.cursor.x - 1),
                curses.KEY_DOWN:  (lambda: self.cursor.x < self.limit.x, lambda: self.cursor.x + 1),
            },
            Direction.HORIZONTAL: {
                curses.KEY_LEFT:  (lambda: self.cursor.y > 0, lambda: self.cursor.y - 1),
                curses.KEY_RIGHT: (lambda: self.cursor.y < self.limit.y, lambda: self.cursor.y + 1),
            },
        }

        if self.is_2d:
            self.keys = { 
                keys[Direction.VERTICAL],
                keys[Direction.HORIZONTAL],
            }
        else:
            if self.direction == Direction.VERTICAL:
                self.keys = {
                    keys[Direction.VERTICAL]
                }
            elif self.direction == Direction.HORIZONTAL:
                self.keys = {
                    keys[Direction.HORIZONTAL]
                }
            else:
                raise NameError("")
    
    def key_registration(self, key: int) -> bool:
        if key in [curses.KEY_ENTER, 10, 13]:
            self.enter = True

        if self.is_2d:
            self._handle_2d_movement(key)
        else:
            self._handle_1d_movement(key)

        return True

    def _handle_2d_movement(self, key: int):
        if key in self.movements:
            check, action = self.movements[key]
            if check():
                self.cursor.x, self.cursor.y = action() if key in {curses.KEY_UP, curses.KEY_DOWN} else self.cursor.x, action()

    def _handle_1d_movement(self, key: int):
        if key in movements:
            check, action = movements[key]
            if check():
                self.cursor.x, self.cursor.y = action() if self.direction == Direction.VERTICAL else self.cursor.x, action()

class MBase(ABC):
    def __init__(self, 
                 stdscr: curses.window
                 ):
        self.stdscr = stdscr
        self.init_curses()

    def init_curses(self):
        curses.curs_set(0)  # Cursor hide
        
        # Color scheme
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    @abstractmethod
    def draw(self):
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def handle_input(self, key):
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def run(self):
        raise NotImplementedError("Subclasses should implement this!")


class SMenu(MBase):
    def __init__(self, 
                 stdscr: curses.window, 
                 *,
                 menu_items: List[str], title: str ="Menu",
                 menu_type: str = "vertical"
                 ):
        MBase.__init__(stdscr)
        self.menu_items = menu_items
        self.title = title
        self.menu_type = menu_type

        self._init_controller()
    
    def _init_controller(self):
        if self.menu_type == "vertical":
            self.controller = Controller(Vector2(), Vector2(0, len(self.menu_items)))
        if self.menu_type == "horizontal":
            self.controller = Controller(Vector2(), Vector2(), Vector2(0, len(self.menu_items)))
        else:
            raise SyntaxError(f"There is no such type of menu {self.menu_type}")
        
    def draw(self):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        # Drawing border
        self.stdscr.border(0)

        # Title
        self.stdscr.addstr(1, w // 2 - len(self.title) // 2, self.title, curses.A_BOLD)

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

    @abstractmethod
    def select_item(self, index):
        raise NotImplementedError("Subclasses should implement this!")

    def get_title(self):
        return self.title

# Пример использования MenuScreen
class MainMenu(MenuScreen):
    def __init__(self, stdscr):
        menu_items = ["Start Game", "Options", "Exit"]
        super().__init__(stdscr, menu_items, title="Main Menu")

    def select_item(self, index):
        if index == 0:
            print("Start Game selected")
        elif index == 1:
            print("Options selected")
        elif index == 2:
            return False
        return True
    

def draw_menu(stdscr: curses.window, menu_items, current_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu_items):
        x = w//2 - len(row)//2
        y = h//2 - len(menu_items)//2 + idx
        if idx == current_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def main_menu(stdscr: curses.window):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_idx = 0
    menu_items = ['Option 1', 'Option 2', 'Option 3', 'Exit']
    
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
                stdscr.addstr(0, 0, f"You selected '{menu_items[current_row_idx]}'")
                stdscr.refresh()
                stdscr.getch()
                draw_menu(stdscr, menu_items, current_row_idx)

        draw_menu(stdscr, menu_items, current_row_idx)

# if __name__ == "__main__":
#     curses.wrapper(main_menu)

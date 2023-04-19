import curses


class Colors:
    def __init__(self):
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        self.white_on_black = curses.color_pair(1)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.green_on_black = curses.color_pair(2)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        self.blue_on_black = curses.color_pair(3)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
        self.red_on_black = curses.color_pair(4)


colors = Colors()

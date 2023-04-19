import curses


def analyse():
    scr = curses.initscr()
    try:
        choice = scr.getkey()
    except:
        choice = None
    if choice in ['KEY_UP', 'W', 'w', 'Ц', 'ц', 119, 87, 72, 230]:  # <=> up
        return 'U'
    elif choice in ['KEY_DOWN', 'S', 's', 'Ы', 'ы', 115, 83, 80, 235]:  # <=> down
        return 'D'
    elif choice in ['KEY_RIGHT', 'D', 'd', 'В', 'в', 100, 68, 77, 162]:  # <=> right
        return 'R'
    elif choice in ['KEY_LEFT', 'A', 'a', 'Ф', 'ф', 97, 65, 75, 228]:  # <=> left
        return 'L'
    elif ord(choice) in [10, 32] or choice in ['KEY_ENTER', '\n', 'E', 'e', 13, 227]:  # <=> Enter
        return 'E'
    elif ord(choice) in [27] or choice in ['^[', 'Q', 'q', 27]:  # <=> Esc <=> Back
        return 'B'

if __name__ == '__main__':
    from menu_main import main_menu_start

    main_menu_start()
    
    # from files import get_menu_list
    # from json import load, dump
    #
    # for k in ['Commands', 'SysFiles', 'Utilities']:
    #     data = get_menu_list(k)
    #     for file in data:
    #         print(file)
    #         with open(file, 'r', encoding='utf-8') as f:
    #             records = load(f)
    #         records["question_state"] = 0
    #         with open(file, "w", encoding="UTF-8") as f:
    #             dump(records, f, ensure_ascii=False, indent=2)
    
    # import time
    # import curses
    # from curses import wrapper
    #
    # scr = curses.initscr()
    #
    # while True:
    #     scr.clear()
    #     y, x = curses.LINES, curses.COLS
    #     scr.addstr(y, x, f'y = {y}, x = {x}')
    #     scr.refresh()
    # while True:
    #     try:
    #         k = scr.getkey()
    #     except:
    #         k = None
    #     scr.clear()
    #     scr.addstr(5, 5, f'Key: {k}, num = {ord(k)}')
    #     scr.refresh()

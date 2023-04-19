if __name__ == '__main__':
    from menu_main import main_menu_start

    main_menu_start()
    
    # from files import get_menu_list
    #
    # print(*get_menu_list('Commands'), sep='\n')
    
    # import time
    # import curses
    # from curses import wrapper
    #
    # scr = curses.initscr()
    #
    # while True:
    #     try:
    #         k = scr.getkey()
    #     except:
    #         k = None
    #     scr.clear()
    #     scr.addstr(5, 5, f'Key: {k}, num = {ord(k)}')
    #     scr.refresh()

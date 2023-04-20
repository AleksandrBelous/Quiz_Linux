util_menu_state = 0


def utilities_draw(scr):
    global util_menu_state
    
    import os
    import curses
    # scr = curses.initscr()
    from colores import colors
    
    from files import get_menu_list
    menu = sorted(os.path.split(f)[-1].removesuffix(".json") for f in get_menu_list('Utilities'))
    n, max_ = len(menu), len(max(menu, key=lambda s: len(s)))
    l, r = '  ', '  '
    l_cl, r_cl = '< ', ' >'
    
    while True:
        scr.clear()
        scr.border()
        col = colors.white_on_black
        st = util_menu_state
        for i in range(n):
            if i == st:
                scr.addstr(i + 2 + 1, 2, f'{l_cl}{menu[i]:<{max_}}{r_cl}', col | curses.A_BOLD)
            else:
                scr.addstr(i + 2 + 1, 2, f'{l}{menu[i]:<{max_}}{r}', col)
        ###################################
        from menu_move import analyse
        choice = analyse(scr)
        if choice == 'U':
            util_menu_state = (st - 1) % n
        elif choice == 'D':
            util_menu_state = (st + 1) % n
        elif choice == 'E':
            ...
        elif choice == 'B':
            from menu_new_game import new_game_draw
            new_game_draw(scr)
        scr.refresh()

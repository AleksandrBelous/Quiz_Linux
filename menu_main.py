main_menu_state = 0


def menu_draw(scr):
    global main_menu_state
    
    import curses
    from colores import colors
    curses.curs_set(0)
    # scr = curses.initscr()
    
    menu = ['ПРОДОЛЖИТЬ',
            'ПРОГРЕСС',
            'БЛИЦ-РЕЖИМ',
            'НОВАЯ ИГРА',
            'НАСТРОЙКИ',
            'АВТОРЫ',
            'ЗАВЕРШИТЬ']
    
    n, max_ = len(menu), len(max(menu, key=lambda s: len(s)))
    l, r = ' |   ', '   | '
    l_cl, r_cl = '(|)> ', ' <(|)'
    
    # hight, width = len(menu), len(l_cl) + max_ + len(r_cl)
    h, w = scr.getmaxyx()
    
    while True:
        y, x = (h - n) // 2, w // 2 - (max_ + len(l_cl) + len(r_cl)) // 2
        
        scr.clear()
        scr.border()
        
        st = main_menu_state
        
        for i in range(n):
            if i == st != n - 1:
                scr.addstr(y + i, x, f'{l_cl}{menu[i]:^{max_}}{r_cl}', colors.green_on_black | curses.A_BOLD)
            elif i == st == n - 1:
                scr.addstr(y + i, x, f'{l_cl}{menu[i]:^{max_}}{r_cl}', colors.red_on_black | curses.A_BOLD)
            else:
                scr.addstr(y + i, x, f'{l}{menu[i]:^{max_}}{r}', colors.white_on_black)
        ###################################
        from menu_move import analyse
        choice = analyse(scr)
        if choice == 'U':
            main_menu_state = (st - 1) % n
        elif choice == 'D':
            main_menu_state = (st + 1) % n
        elif choice == 'E':
            if st == 0:
                ...
            elif st == 1:
                ...
            elif st == 2:
                ...
            elif st == 3:
                from menu_new_game import new_game_draw
                new_game_draw(scr)
            elif st == n - 1:
                scr.clear()
                exit(0)
        elif choice == 'S':
            h, w = scr.getmaxyx()
            scr.clear()
            curses.resize_term(h, w)
        scr.refresh()


def main_menu_start():
    from curses import wrapper
    wrapper(menu_draw)

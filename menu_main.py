def menu_draw(scr):
    from files import get_settings, save_settings, clear_settings
    key = 'main_menu_state'
    st = get_settings(key)
    file = 'game_conf.json'
    
    import curses
    from colores import colors
    curses.curs_set(0)
    # scr = curses.initscr()
    
    menu = ['ПРОДОЛЖИТЬ',
            'ПРОГРЕСС',
            'БЛИЦ-РЕЖИМ',
            'ВЫБОР ТЕМЫ',
            'НОВАЯ ИГРА',
            'УПРАВЛЕНИЕ',
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
            st = (st - 1) % n
        elif choice == 'D':
            st = (st + 1) % n
        elif choice == 'E':
            if st == 0:  # continue game
                save_settings(file, key, st)
                from resume import resume
                resume(scr)
            elif st == 1:  # progress bar
                ...
            elif st == 2:  # blits mod
                save_settings(file, key, st)
                from blitz_mode import blitzmode
                blitzmode(scr)
            elif st == 3:  # choosing the theme
                save_settings(file, key, st)
                from menu_choosing_theme import choosing_theme_draw
                choosing_theme_draw(scr)
            elif st == 4:  # new game
                clear_settings()
                save_settings(file, key, st)
                from menu_choosing_theme import choosing_theme_draw
                choosing_theme_draw(scr)
            elif st == n - 1:
                scr.clear()
                save_settings(file, key)
                exit(0)
        elif choice == 'S':
            h, w = scr.getmaxyx()
            scr.clear()
            curses.resize_term(h, w)
        scr.refresh()


def main_menu_start():
    from curses import wrapper
    wrapper(menu_draw)

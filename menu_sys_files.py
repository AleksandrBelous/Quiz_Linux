def sys_files_draw(scr):
    from files import get_settings, save_settings
    key = 'files_menu_state'
    st = get_settings(key)
    
    import os
    import curses
    # scr = curses.initscr()
    from colores import colors
    
    from files import get_menu_list
    files_lst = sorted(get_menu_list('SysFiles'), key=lambda f: os.path.split(f)[-1].removesuffix(".json"))
    menu = [os.path.split(f)[-1].removesuffix(".json") for f in files_lst]
    n, max_ = len(menu), len(max(menu, key=lambda s: len(s)))
    l, r = '  ', '  '
    l_cl, r_cl = '< ', ' >'
    
    h, w = scr.getmaxyx()
    
    while True:
        scr.clear()
        scr.border()
        y, x = (h - n) // 2, w // 2 - (max_ + len(l_cl) + len(r_cl)) // 2
        for i in range(n):
            if i == st:
                scr.addstr(y + i, x, f'{l_cl}{menu[i]:<{max_}}{r_cl}', colors.green_on_black | curses.A_BOLD)
            else:
                scr.addstr(y + i, x, f'{l}{menu[i]:<{max_}}{r}', colors.white_on_black)
        ###################################
        from menu_move import analyse
        choice = analyse(scr)
        if choice == 'U':
            st = (st - 1) % n
        elif choice == 'D':
            st = (st + 1) % n
        elif choice == 'E':
            save_settings(key, st)
            from menu_questions import questions_window
            questions_window(files_lst[st], scr)
        elif choice == 'B':
            save_settings(key, st)
            from menu_choosing_theme import choosing_theme_draw
            choosing_theme_draw(scr)
        elif choice == 'S':
            h, w = scr.getmaxyx()
            scr.clear()
            curses.resize_term(h, w)
        scr.refresh()

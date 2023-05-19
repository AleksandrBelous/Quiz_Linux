def choosing_theme_draw(scr):
    from files import get_settings, save_settings
    key = 'theme_state'
    st = get_settings(key)
    
    from colores import colors
    import curses
    # scr = curses.initscr()
    head = 'Тема викторины'
    menu = [f'Команды bash ({get_settings("bash_prc")} %)',
            f'Системные файлы ({get_settings("files_prc")} %)',
            f'Инструменты ({get_settings("util_prc")} %)']
    
    n, max_ = len(menu), len(max(menu, key=lambda s: len(s)))
    l, r = ' |   ', '   | '
    l_cl, r_cl = '(|)> ', ' <(|)'
    
    h, w = scr.getmaxyx()
    
    while True:
        scr.clear()
        scr.border()
        y, x = (h - (n + 2)) // 2, w // 2 - (max_ + len(l_cl) + len(r_cl)) // 2
        scr.addstr(y, x, f'{head:^{len(l_cl) + max_ + len(r_cl)}}', colors.blue_on_black | curses.A_BOLD)
        scr.addstr(y + 1, x, '\n')
        for i in range(n):
            if i == st:
                scr.addstr(y + 2 + i, x, f'{l_cl}{menu[i]:^{max_}}{r_cl}', colors.green_on_black | curses.A_BOLD)
            else:
                scr.addstr(y + 2 + i, x, f'{l}{menu[i]:^{max_}}{r}', colors.white_on_black)
        ###################################
        from menu_move import analyse
        choice = analyse(scr)
        if choice == 'U':
            st = (st - 1) % n
        elif choice == 'D':
            st = (st + 1) % n
        elif choice == 'E':
            save_settings(key, st)
            if st == 0:
                from menu_bash_commands import bash_commands_draw
                bash_commands_draw(scr)
            elif st == 1:
                from menu_sys_files import sys_files_draw
                sys_files_draw(scr)
            elif st == 2:
                from menu_utilities import utilities_draw
                utilities_draw(scr)
        elif choice == 'B':
            save_settings(key, st)
            from menu_main import menu_draw
            menu_draw(scr)
        elif choice == 'S':
            h, w = scr.getmaxyx()
            scr.clear()
            curses.resize_term(h, w)
        scr.refresh()

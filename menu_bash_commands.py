from json import load


def bash_commands_draw(scr):
    from files import get_settings, save_settings
    key = 'bash_menu_state'
    st = get_settings(key)
    file = 'game_conf.json'
    
    import os
    import curses
    # scr = curses.initscr()
    from colores import colors
    
    from files import get_menu_list
    files_lst = sorted(get_menu_list('Commands'), key=lambda f: os.path.split(f)[-1].removesuffix(".json"))
    menu = [os.path.split(f)[-1].removesuffix(".json") for f in files_lst]
    n, max_ = len(menu), len(max(menu, key=lambda s: len(s)))
    l, r = '', ''
    l_cl, r_cl = '', ''
    
    scr_h, scr_w = scr.getmaxyx()
    m = 0
    
    while True:
        scr.clear()
        scr.border()
        y, x = (scr_h - m) // 2, scr_w // 2 - (max_ + len(l_cl) + len(r_cl)) // 2
        scr.addstr(y - 3, x, f'{l}{menu[st - 3]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        scr.addstr(y - 2, x, f'{l}{menu[st - 2]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        scr.addstr(y - 1, x, f'{l}{menu[st - 1]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        with open(files_lst[st], 'r', encoding='utf-8') as st_f:
            records = load(st_f)
        scr.addstr(y, x, f'{l_cl}{menu[st]:<{max_}}{r_cl} {records["info"]}', colors.green_on_black | curses.A_BOLD)
        scr.addstr(y + 1, x, f'{l}{menu[(st + 1) % n]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        scr.addstr(y + 2, x, f'{l}{menu[(st + 2) % n]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        scr.addstr(y + 3, x, f'{l}{menu[(st + 3) % n]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        ###################################
        from menu_move import analyse
        choice = analyse(scr)
        if choice == 'U':
            st = (st - 1) % n
        elif choice == 'D':
            st = (st + 1) % n
        elif choice == 'E':
            save_settings(file, key, st)
            from menu_questions import questions_window
            questions_window(files_lst[st], scr)
        elif choice == 'B':
            save_settings(file, key, st)
            save_settings(file, "resume", 0)
            from menu_choosing_theme import choosing_theme_draw
            choosing_theme_draw(scr)
        elif choice == 'S':
            scr_h, scr_w = scr.getmaxyx()
            scr.clear()
            curses.resize_term(scr_h, scr_w)
        scr.refresh()

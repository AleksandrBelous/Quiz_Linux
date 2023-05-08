from json import load

bash_menu_state = 0


def bash_commands_draw(scr):
    global bash_menu_state
    
    import os
    import curses
    scr = curses.initscr()
    from colores import colors
    
    from files import get_menu_list
    files_lst = sorted(get_menu_list('Commands'), key=lambda f: os.path.split(f)[-1].removesuffix(".json"))
    menu = [os.path.split(f)[-1].removesuffix(".json") for f in files_lst]
    n, max_ = len(menu), len(max(menu, key=lambda s: len(s)))
    l, r = '', ''
    l_cl, r_cl = '', ''
    
    scr_h, scr_w = scr.getmaxyx()
    
    while True:
        scr.clear()
        scr.border()
        st = bash_menu_state
        with open(files_lst[st], 'r', encoding='utf-8') as st_f:
            records = load(st_f)
        y, x = (scr_h - 3) // 2, scr_w // 2 - (max_ + len(l_cl) + len(r_cl)) // 2
        scr.addstr(y - 3, x, f'{l}{menu[st - 3]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        scr.addstr(y - 2, x, f'{l}{menu[st - 2]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        scr.addstr(y - 1, x, f'{l}{menu[st - 1]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        scr.addstr(y, x, f'{l_cl}{menu[st]:<{max_}}{r_cl}{records["info"]}', colors.green_on_black | curses.A_BOLD)
        scr.addstr(y + 1, x, f'{l}{menu[(st + 1) % n]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        scr.addstr(y + 2, x, f'{l}{menu[(st + 2) % n]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        scr.addstr(y + 3, x, f'{l}{menu[(st + 3) % n]:<{max_}}{r}', colors.white_on_black | curses.A_DIM)
        ###################################
        from menu_move import analyse
        choice = analyse(scr)
        if choice == 'U':
            bash_menu_state = (st - 1) % n
        elif choice == 'D':
            bash_menu_state = (st + 1) % n
        elif choice == 'E':
            ...
        elif choice == 'B':
            from menu_new_game import new_game_draw
            new_game_draw(scr)
        elif choice == 'S':
            scr_h, scr_w = scr.getmaxyx()
            scr.clear()
            curses.resize_term(scr_h, scr_w)
        scr.refresh()

# sys_files_menu_state = 0
# utilities_menu_state = 0
# info_state = 0
#
#
# def info(path):
#     global info_state
#     st = info_state
#     from json import load
#     with open(path, 'r', encoding='utf-8') as f:
#         dct = load(f)
#         print(f'\n'
#               f'\t{dct["info"]}')
#     import menu_move
#     choice = menu_move.analyse()
#     if choice == 'B':
#         if info_state == 0:
#             bash_commands()
#         elif info_state == 1:
#             sys_files()
#         elif info_state == 2:
#             utilities()
#
#
# def find_info(command):
#     """Python code to search <command.json> file in current folder."""
#     import os
#     dir_path, task_path = os.path.dirname(os.path.realpath(__file__)), ''
#     for root, dirs, files in os.walk(dir_path):
#         if command + '.json' in files:
#             task_path = os.path.join(root, command + '.json')
#             break
#     os.system('cls')
#     info(task_path)

new_game_menu_state = 0


def new_game_draw(scr):
    global new_game_menu_state
    
    from colores import colors
    import curses
    # scr = curses.initscr()
    head = 'Тема викторины'
    menu = ['Команды bash',
            'Системные файлы',
            'Спец. программы']
    
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
        st = new_game_menu_state
        for i in range(n):
            if i == st:
                scr.addstr(y + 2 + i, x, f'{l_cl}{menu[i]:^{max_}}{r_cl}', colors.green_on_black | curses.A_BOLD)
            else:
                scr.addstr(y + 2 + i, x, f'{l}{menu[i]:^{max_}}{r}', colors.white_on_black)
        ###################################
        from menu_move import analyse
        choice = analyse(scr)
        if choice == 'U':
            new_game_menu_state = (st - 1) % n
        elif choice == 'D':
            new_game_menu_state = (st + 1) % n
        elif choice == 'E':
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
            from menu_main import menu_draw
            menu_draw(scr)
        elif choice == 'S':
            h, w = scr.getmaxyx()
            scr.clear()
            curses.resize_term(h, w)
        scr.refresh()
        #############################################
        # new = {'theme': input(''), 'hard': input('')}
        # from json import dump
        # with open('game_conf.json', 'w', encoding='utf-8') as f:
        #     dump(new, f, ensure_ascii=False, indent=2)

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
    
    while True:
        scr.clear()
        scr.border()
        col = colors.white_on_black
        scr.addstr(2, 2, f'{head:^{len(l_cl) + max_ + len(r_cl)}}', col)
        scr.addstr(3, 2, '\n')
        st = new_game_menu_state
        for i in range(n):
            if i == st:
                scr.addstr(i + 3 + 1, 2, f'{l_cl}{menu[i]:^{max_}}{r_cl}', col | curses.A_BOLD)
            else:
                scr.addstr(i + 3 + 1, 2, f'{l}{menu[i]:^{max_}}{r}', col)
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
        scr.refresh()
        #############################################
        # new = {'theme': input(''), 'hard': input('')}
        # from json import dump
        # with open('game_conf.json', 'w', encoding='utf-8') as f:
        #     dump(new, f, ensure_ascii=False, indent=2)

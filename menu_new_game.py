bash_menu_state = 0
sys_files_menu_state = 0
utilities_menu_state = 0
new_game_menu_state = 0
info_state = 0


def info(path):
    global info_state
    st = info_state
    from json import load
    with open(path, 'r', encoding='utf-8') as f:
        dct = load(f)
        print(f'\n'
              f'\t{dct["info"]}')
    import menu_move
    choice = menu_move.analyse()
    if choice == 'B':
        if info_state == 0:
            bash_commands()
        elif info_state == 1:
            sys_files()
        elif info_state == 2:
            utilities()


def find_info(command):
    """Python code to search <command.json> file in current folder."""
    import os
    dir_path, task_path = os.path.dirname(os.path.realpath(__file__)), ''
    for root, dirs, files in os.walk(dir_path):
        if command + '.json' in files:
            task_path = os.path.join(root, command + '.json')
            break
    os.system('cls')
    info(task_path)


def bash_commands():
    global bash_menu_state, info_state
    st = bash_menu_state
    import os
    os.system('cls')
    commands = sorted(['gzip', 'tar',
                       'df', 'du', 'fdisk', 'findmnt',
                       'cat', 'cp', 'head', 'ln', 'ls', 'mkdir', 'more', 'mv', 'pwd', 'rm', 'tail', 'touch', 'wc',
                       'xargs',
                       'awk', 'grep', 'sed'])
    n = len(commands)
    print('\n')
    for i in range(n):
        if i == st:
            print(f'\t< {commands[i]} >')
        else:
            print(f'\t{commands[i]}')
    ###################################
    from menu_move import analyse
    choice = analyse()
    if choice == 'U':
        bash_menu_state = (st - 1) % n
        bash_commands()
    elif choice == 'D':
        bash_menu_state = (st + 1) % n
        bash_commands()
    elif choice == 'E':
        info_state = 0
        find_info(commands[st])
    elif choice == 'B':
        new_game()
    else:
        bash_commands()


def sys_files():
    global sys_files_menu_state, info_state
    st = sys_files_menu_state
    import os
    os.system('cls')
    commands = sorted(['cpuinfo', 'meminfo'])
    n = len(commands)
    print('\n')
    for i in range(n):
        if i == st:
            print(f'\t< {commands[i]} >')
        else:
            print(f'\t{commands[i]}')
    ###################################
    from menu_move import analyse
    choice = analyse()
    if choice == 'U':
        sys_files_menu_state = (st - 1) % n
        sys_files()
    elif choice == 'D':
        sys_files_menu_state = (st + 1) % n
        sys_files()
    elif choice == 'E':
        info_state = 1
        find_info(commands[st])
    elif choice == 'B':
        new_game()
    else:
        sys_files()


def utilities():
    global utilities_menu_state, info_state
    st = utilities_menu_state
    import os
    os.system('cls')
    commands = sorted(['gpg', 'nmap'])
    n = len(commands)
    print('\n')
    for i in range(n):
        if i == st:
            print(f'\t< {commands[i]} >')
        else:
            print(f'\t{commands[i]}')
    ###################################
    from menu_move import analyse
    choice = analyse()
    if choice == 'U':
        utilities_menu_state = (st - 1) % n
        utilities()
    elif choice == 'D':
        utilities_menu_state = (st + 1) % n
        utilities()
    elif choice == 'E':
        info_state = 2
        find_info(commands[st])
    elif choice == 'B':
        new_game()
    else:
        utilities()


def new_game():
    global new_game_menu_state
    st = new_game_menu_state
    from os import system
    system('cls')
    if st == 0:
        print('\n'
              '\t === Тема викторины ===\n'
              '\t  <<< Команды bash >>> \n'
              '\t    Системные файлы    \n'
              '\t    Спец. программы    \n')
    elif st == 1:
        print('\n'
              '\t === Тема викторины ===\n'
              '\t      Команды bash     \n'
              '\t<<< Системные файлы >>>\n'
              '\t    Спец. программы    \n')
    elif st == 2:
        print('\n'
              '\t === Тема викторины ===\n'
              '\t      Команды bash     \n'
              '\t    Системные файлы    \n'
              '\t<<< Спец. программы >>>\n')
    ###################################
    from menu_move import analyse
    choice = analyse()
    if choice == 'U':
        new_game_menu_state = (st - 1) % 3
        new_game()
    elif choice == 'D':
        new_game_menu_state = (st + 1) % 3
        new_game()
    elif choice == 'E':
        if st == 0:
            bash_commands()
        elif st == 1:
            sys_files()
        elif st == 2:
            utilities()
    elif choice == 'B':
        from menu_main import menu_draw
        menu_draw()
    else:
        new_game()
    #############################################
    new = {'theme': input(''), 'hard': input('')}
    from json import dump
    with open('game_conf.json', 'w', encoding='utf-8') as f:
        dump(new, f, ensure_ascii=False, indent=2)

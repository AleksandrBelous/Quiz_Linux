from json import load


def resume(scr):
    with open('game_conf.json', 'r', encoding='utf-8') as f:
        records = load(f)
    if records["resume"] == 0:  # bash
        from menu_bash_commands import bash_commands_draw
        bash_commands_draw(scr)
    elif records["resume"] == 1:  # sys
        from menu_sys_files import sys_files_draw
        sys_files_draw(scr)
    elif records["resume"] == 2:  # tools
        from menu_utilities import utilities_draw
        utilities_draw(scr)

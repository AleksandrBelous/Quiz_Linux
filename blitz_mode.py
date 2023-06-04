import random
from json import load
import os


def blitzmode(scr):
    lst = []
    
    from files import get_menu_list
    
    for k in ['Commands', 'SysFiles', 'Utilities']:
        data = get_menu_list(k)
        for file in data:
            lst.append(file)
    n = len(lst)
    
    while True:
        file = lst[random.randint(0, n - 1)]
        answer_state = 0
        
        import curses
        # scr = curses.initscr()
        from colores import colors
        with open(file, 'r', encoding='utf-8') as f:
            records = load(f)
        
        len_req_ques, name = len(records["questions"]), os.path.split(file)[-1].removesuffix(".json")
        
        scr_h, scr_w = scr.getmaxyx()
        n, max_ = 4 + 1 + 1 + 1, len(max(records["questions"], key=lambda dct: len(dct["question"]))["question"])
        
        r = '<'
        
        st = random.randint(0, len_req_ques - 1)
        options = records["questions"][st]["options"]
        random.shuffle(options)
        
        while True:
            scr.clear()
            scr.border()
            y, x = (scr_h - n) // 2, scr_w // 2 - max_ // 2
            scr.addstr(y, x, f'{records["man"]:^{max_}}', colors.blue_on_black | curses.A_UNDERLINE)
            tmp = f'{name} [{st + 1}/{len_req_ques}]'
            scr.addstr(y + 1, x, f'{tmp:^{max_}}', colors.white_on_black)
            scr.addstr(y + 2, x, f'{records["questions"][st]["question"]:^{max_}}', colors.white_on_black)
            answ_max_ = len(max(records["questions"][st]["options"], key=lambda a: len(a))) + 1
            luck = None
            for i in range(4):
                if i == answer_state:
                    scr.addstr(y + 3 + i, x, f'{options[i]:<{answ_max_}}{r}', colors.white_on_black)
                else:
                    scr.addstr(y + 3 + i, x, f'{options[i]:<{answ_max_}}', colors.white_on_black)
                if luck is None and records["questions"][st]["options"][i] == records["questions"][st]["answer"]:
                    luck = i
            ###################################
            from menu_move import analyse
            choice = analyse(scr)
            if choice == 'U':
                answer_state = (answer_state - 1) % 4
            elif choice == 'D':
                answer_state = (answer_state + 1) % 4
            elif choice == 'E':
                scr.addstr(y + 3 + luck, x, f'{records["questions"][st]["options"][luck]:<{answ_max_}} ', colors.green_on_black)
                if records["questions"][st]["options"][answer_state] != records["questions"][st]["answer"]:
                    scr.addstr(y + 3 + answer_state, x, f'{records["questions"][st]["options"][answer_state]:<{answ_max_}} ', colors.red_on_black)
                scr.refresh()
                choice = analyse(scr)
                if choice in ['R', 'U', 'E']:
                    st = (st + 1) % len_req_ques
                    options = records["questions"][st]["options"]
                    random.shuffle(options)
                elif choice in ['L', 'D']:
                    st = (st - 1) % len_req_ques
                    options = records["questions"][st]["options"]
                    random.shuffle(options)
                answer_state = 0
                break
            elif choice == 'R':
                # st = (st + 1) % len_req_ques
                # options = records["questions"][st]["options"]
                # random.shuffle(options)
                break
            elif choice == 'L':
                # st = (st - 1) % len_req_ques
                # options = records["questions"][st]["options"]
                # random.shuffle(options)
                break
            elif choice == 'B':
                from menu_main import menu_draw
                menu_draw(scr)
            elif choice == 'S':
                scr_h, scr_w = scr.getmaxyx()
                scr.clear()
                curses.resize_term(scr_h, scr_w)
            scr.refresh()

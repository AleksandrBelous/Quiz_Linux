main_menu_state = 0


def menu_draw():
    from os import system
    system('cls')
    global main_menu_state
    st = main_menu_state
    if st == 0:
        print('\n'
              '\t<<< Продолжить >>>\n'
              '\t     Прогресс     \n'
              '\t    Новая игра    \n'
              '\t    Управление    \n'
              '\t      Авторы      \n'
              '\t     Завершить    \n')
    elif st == 1:
        print('\n'
              '\t    Продолжить    \n'
              '\t <<< Прогресс >>> \n'
              '\t    Новая игра    \n'
              '\t    Управление    \n'
              '\t      Авторы      \n'
              '\t     Завершить    \n')
    elif st == 2:
        print('\n'
              '\t    Продолжить    \n'
              '\t     Прогресс     \n'
              '\t<<< Новая игра >>>\n'
              '\t    Управление    \n'
              '\t      Авторы      \n'
              '\t     Завершить    \n')
    elif st == 3:
        print('\n'
              '\t    Продолжить    \n'
              '\t     Прогресс     \n'
              '\t    Новая игра    \n'
              '\t<<< Управление >>>\n'
              '\t      Авторы      \n'
              '\t     Завершить    \n')
    elif st == 4:
        print('\n'
              '\t    Продолжить    \n'
              '\t     Прогресс     \n'
              '\t    Новая игра    \n'
              '\t    Управление    \n'
              '\t  <<< Авторы >>>  \n'
              '\t     Завершить    \n')
    elif st == 5:
        print('\n'
              '\t    Продолжить    \n'
              '\t     Прогресс     \n'
              '\t    Новая игра    \n'
              '\t    Управление    \n'
              '\t      Авторы      \n'
              '\t <<< Завершить >>>\n')
    ###################################
    from menu_move import analyse
    choice = analyse()
    if choice == 'U':
        main_menu_state = (st - 1) % 6
        menu_draw()
    elif choice == 'D':
        main_menu_state = (st + 1) % 6
        menu_draw()
    elif choice == 'E':
        if st == 0:
            ...
        elif st == 1:
            ...
        elif st == 2:
            from menu_new_game import new_game
            new_game()
        elif st == 5:
            print('\n\tПриходите играть снова!\n')
            exit(0)
    else:
        menu_draw()

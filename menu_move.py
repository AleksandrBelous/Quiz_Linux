def analyse():
    import msvcrt
    choice = ord(msvcrt.getch())
    if choice in [119, 72, 230]:  # <=> up
        return 'U'
    elif choice in [115, 80, 235]:  # <=> down
        return 'D'
    elif choice in [100, 77, 162]:  # <=> right
        return 'R'
    elif choice in [97, 75, 228]:  # <=> left
        return 'L'
    elif choice in [13, 32, 227]:  # <=> Enter
        return 'E'
    elif choice in [27]:  # <=> Esc <=> Back
        return 'B'

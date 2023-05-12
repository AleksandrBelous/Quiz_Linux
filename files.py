def get_menu_list(to_find: str) -> list:
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(dir_path):
        if to_find in root:
            dir_path = root
            break
    # print(f'tmp path: {dir_path}')
    menu = []
    for root, dirs, files in os.walk(dir_path):
        # print(f'root: {root}')
        # print(f'dirs: {dirs}')
        # print(f'files: {files}')
        for file in files:
            # menu.append(os.path.join(os.path.split(root)[0], file))
            menu.append(os.path.join(root, file))
    return menu

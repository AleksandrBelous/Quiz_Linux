from json import load


def resume():
    with open('game_conf.json', 'r', encoding='utf-8') as f:
        records = load(f)

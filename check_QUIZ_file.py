#
from json import load


def check(command):
    """
    Argument: the path to the .json file
    Result: content output to the console, nesting is displayed.
    """
    with open(f'{command}', encoding='UTF-8') as file_in:
        records = load(file_in)
    for k, v in records.items():
        for pairs in v:
            print(pairs['question'])
            for opt in pairs['options']:
                print(f'    {opt}')
            print(pairs['answer'])


if __name__ == '__main__':
    command = 'Commands/Files/ls.json'
    check(command)

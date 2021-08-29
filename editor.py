# write your code here
def plain():
    text = input('Text: ')
    return f'{text}'


def bold():
    text = input('Text: ')
    return f'**{text}**'


def italic():
    text = input('Text: ')
    return f'*{text}*'


def header():
    level = int(input('Level: '))

    if level not in range(1, 6):
        print('The level should be within the range of 1 to 6')
        return header()

    text = input('Text: ')
    heading = '#' * level

    return f'{heading} {text}\n'


def link():
    label = input('Label: ')
    url = input('URL: ')

    return f'[{label}]({url})'


def inline_code():
    text = input('Text: ')
    return f'`{text}`'


def new_line():
    return '\n'


def unordered_list():
    rows_number = get_list_info()
    filled_rows = 0
    text = ''

    while filled_rows < rows_number:
        row_placeholder = '*'
        row_text = input(f'Row #{filled_rows + 1}: ')
        text += f'{row_placeholder} {row_text}\n'
        filled_rows += 1

    return text


def ordered_list():
    rows_number = get_list_info()
    filled_rows = 0
    text = ''

    while filled_rows < rows_number:
        row_number = filled_rows + 1
        row_placeholder = f'{row_number}.'
        row_text = input(f'Row #{row_number}: ')
        text += f'{row_placeholder} {row_text}\n'
        filled_rows += 1

    return text


def get_list_info():
    rows_number = int(input('Number of rows: '))
    if rows_number < 1:
        print('The number of rows should be greater than zero')
        return get_list_info()
    return rows_number


def get_list_of_available_formatters():
    return ['plain', 'bold', 'italic', 'header', 'link', 'new-line', 'inline-code', 'ordered-list', 'unordered-list']


def get_list_of_formatters_function():
    return [plain, bold, italic, header, link, new_line, inline_code, ordered_list, unordered_list]


def get_list_of_special_commands():
    return ['help', 'done']


def add_prefix(string):
    return f'!{string}'


def print_help():
    available_formatters = get_list_of_available_formatters()
    special_commands = map(add_prefix, get_list_of_special_commands())
    print('Available formatters:', ' '.join(available_formatters))
    print('Special commands:', ' '.join(special_commands))


def process_formatter(command):
    available_formatters_names = get_list_of_available_formatters()
    available_formatters = get_list_of_formatters_function()

    index = available_formatters_names.index(command)
    formatter = available_formatters[index]
    new_text = formatter()
    return new_text


def done(text):
    file_with_results = open('output.md', 'w', encoding='utf-8')
    file_with_results.write(text)
    file_with_results.close()
    return True


def main(text):
    user_input = input('Choose a formatter: ')

    if user_input == '!help':
        print_help()
        main(text)
        return

    if user_input == '!done':
        return done(text)

    if user_input in get_list_of_available_formatters():
        text += process_formatter(user_input)
        if len(text) != 0:
            print(text)
        main(text)
        return
    else:
        print('Unknown formatting type or command')
        main(text)
        return


main('')

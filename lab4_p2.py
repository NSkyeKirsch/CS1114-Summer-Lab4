def get_most_common_word(file_path):
    """

    :param file_path: name of file containing readable text
    :return: tuple like this: (most_common_word, most_common_word_frequency)

    if file fails to be readable, return ("", -1)
    """
    try:
        file = open(file_path, 'r')
    except FileNotFoundError:
        return "", -1

    all_lines = ""
    cleaned_lines = ""
    punctuations = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
    for line in file:
        if len(line) > 0:
            all_lines += line.strip().lower()
    for char in all_lines:
        if char not in punctuations:
            cleaned_lines += char
    words_list = cleaned_lines.strip().split()

    most_common_word = "Most common word", 0
    for item in words_list:
        if words_list.count(item) > most_common_word[1]:
            most_common_word = item, words_list.count(item)

    return most_common_word


def main():
    print(get_most_common_word('independence.txt'))


if __name__ == "__main__":
    main()

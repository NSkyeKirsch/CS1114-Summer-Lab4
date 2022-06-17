def count_words(filepath):
    error = True
    while error:
        try:
            file = open(filepath, 'r')
            error = False
        except FileNotFoundError:
            filepath = input("Error: Enter a new file: ")

    # count how many words are in each line (skip first line)
    # print line number and num words in that line
    file.readline()
    counter = 1
    punctuations = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
    for line in file:
        full_line = ""
        cleaned_lines = ""
        if len(line) > 1:
            full_line += line.strip().lower()
            for char in full_line:
                if char not in punctuations:
                    cleaned_lines += char
            words_list = cleaned_lines.strip().split()
            print(line.strip(), counter, len(words_list))
            counter += 1


    file.close()


def main():
    inp_filename = input("Enter a filepath: ")
    count_words(inp_filename)


main()

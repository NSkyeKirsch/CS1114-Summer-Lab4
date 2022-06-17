def read_files(file_name):
    text = ""
    for line in file_name:
        text += line
    return text


def swap_content(first_file, second_file):
    error = True
    while error:
        try:
            file_one = open(first_file, 'r')
            error = False
        except FileNotFoundError:
            first_file = input("Error: Enter a new first file: ")

    error = True
    while error:
        try:
            file_two = open(second_file, 'r')
            error = False
        except FileNotFoundError:
            second_file = input("Error: Enter a new second file: ")

    file_one_text = read_files(file_one)
    file_two_text = read_files(file_two)

    file_one.close()
    file_two.close()

    file_one = open(first_file, 'w')
    file_two = open(second_file, 'w')

    file_two.write(file_one_text)
    file_one.write(file_two_text)

    file_one.close()
    file_two.close()




def main():
    inp_1 = input('first file name: ')
    inp_2 = input('second file name: ')
    swap_content(inp_1, inp_2)
    print('done!')


if __name__ == "__main__":
    main()

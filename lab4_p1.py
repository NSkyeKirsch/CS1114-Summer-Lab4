import random


def write_lines(filepath, numbers):
    file = open(filepath, 'w')
    numbers.sort()
    # minimum, median, average (float 3 places), maximum
    min_val = min(numbers)
    if len(numbers) % 2 == 0:
        median_first = numbers[len(numbers)//2 - 1]
        median_second = numbers[len(numbers)//2]
        median = (median_second + median_first)//2
    else:
        median = numbers[len(numbers)//2]
    average = sum(numbers)/len(numbers)
    max_val = max(numbers)
    #
    str_numbers = str(numbers)
    str_numbers = str_numbers[1:len(str_numbers) - 1]
    file.write("{0:},{1:},{2:.3f},{3:} \n".format(min_val, median, average, max_val))
    file.writelines(str_numbers)
    file.close()


def generate_numbers(start_value, end_value, size):
    num_list = [random.randint(start_value, end_value) for value in range(size)]
    return num_list


def main():
    random_numbers = generate_numbers(0, 250, 25000)
    write_lines('lab2_p1.out', random_numbers)


if __name__ == "__main__":
    main()

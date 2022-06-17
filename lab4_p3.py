def random_function_errors(add_var, file_path):
    worked = True
    try:
        import not_a_real_module.py
        new_var = add_var
    except ModuleNotFoundError as mod_err:
        print("The error: ModuleNotFoundError:", mod_err)
        worked = False


    worked2 = True
    if worked:
        try:
            file = open(file_path, 'x')
            file.close()
        except FileExistsError as file_err:
            print("The error: FileExistsError:", file_err)
            worked2 = False

    if worked2:
        try:
            addition = new_var + 2
        except NameError as name_err:
            print("The error: NameError:", name_err)
        except TypeError as type_err:
            print("The error: TypeError:", type_err)
        very_new_var = 2

        try:
            very_new_var += add_var
        except TypeError as type_err:
            print("The error: TypeError:", type_err)





def main():
    random_function_errors('waddwa', 'dawdwa.txt')

if __name__ == "__main__":
    main()
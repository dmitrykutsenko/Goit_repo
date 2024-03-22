def get_fullname (first_name, last_name, middle_name = ""):
    middle_name = "" if (str(middle_name) == "") else (" " + str(middle_name))
    print(f'{str(first_name)}{str(middle_name)} {last_name}')

get_fullname("Petro", "Petrovich")

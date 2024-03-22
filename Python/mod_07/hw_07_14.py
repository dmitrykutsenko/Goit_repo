# Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу, додаватиме до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.
#
# Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.
#
# Нумерація рядків іде від 0.

def get_employees_by_profession(path, profession):
    with open(path, "r") as file:
        a = file.readlines()
    b = list()
    for i in a:
        if i.find(profession) != -1:
            b.append(i[:-1])
    b = "".join(b)
    b = b.replace(profession, "")
    return b.strip()

def to_indexed(source_file, output_file):
    with open(source_file, "r") as source:
        with open(output_file, "w") as output:
            for idx, line in enumerate(source.readlines()):
                output.write(f"{idx}: {line}")
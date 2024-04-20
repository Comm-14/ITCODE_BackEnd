def check_initials(full_name):
    name_parts = full_name.split()
    last_name = name_parts[-3]
    initials = "".join([name[0] + '.' for name in name_parts[-2:]])
    return last_name, initials

def main():
    full_name = input("Введите полное имя, отчество и фамилию: ")
    last_name, initials = check_initials(full_name)
    print("Фамилия и инициалы:", last_name, initials)

if __name__ == "__main__":
    main()
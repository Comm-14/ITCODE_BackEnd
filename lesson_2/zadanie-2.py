def replace_h(input_str):
    first_h = input_str.find('h')
    last_h = input_str.rfind('h')
    replaced = input_str[:first_h + 1] + input_str[first_h + 1:last_h].replace('h','H') + input_str[last_h:]
    return replaced
def main():
    input_str = input("Введите строку: ")
    modified_str = replace_h(input_str)
    print("Результат замены:", modified_str)
if __name__ == "__main__":
    main()
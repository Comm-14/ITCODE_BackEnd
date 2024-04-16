def replace_h(input_str):
    first_h_index = input_str.find('h')
    last_h_index = input_str.rfind('h')
    if first_h_index == -1 or first_h_index == last_h_index:
        return input_str
    replaced_str = input_str[:first_h_index + 1] + input_str[first_h_index + 1:last_h_index].replace('h','H') + input_str[last_h_index:]
    return replaced_str
def main():
    input_str = input("Введите строку: ")
    modified_str = replace_h(input_str)
    print("Результат замены:", modified_str)
if __name__ == "__main__":
    main()
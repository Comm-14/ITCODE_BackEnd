def reversed(input_str):
    reversed_str = ""
    for i in range(len(input_str) - 1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str
def main():
    input_str = input("Введите строку: ")
    reversed_str = reversed(input_str)
    print("Строка в обратном порядке:", reversed_str)

if __name__ == "__main__":
    main()
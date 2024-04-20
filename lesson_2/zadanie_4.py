def count_words(input_str):
    count = 0
    k = 0
    for char in input_str:
        if char == ' ' and k == 1:
            count += 1
            k = 0
        elif not char == ' ':
            k = 1
    if k == 1:
        count += 1

    return count


def main():
    # Получаем строку от пользователя
    input_str = input("Введите строку: ")

    # Подсчитываем количество слов
    word_count = count_words(input_str)
    print("Количество слов в строке:", word_count)


if __name__ == "__main__":
    main()
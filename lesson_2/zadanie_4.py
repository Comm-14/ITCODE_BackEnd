def count_words(input_str):
    count = 0
    in_word = False
    for char in input_str:
        if char == ' ' and in_word:
            count += 1
            in_word = False
        elif not char == ' ':
            in_word = True
    if in_word:
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
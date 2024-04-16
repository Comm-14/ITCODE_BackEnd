def count_words(input_str):
    words = input_str.split()
    return len(words)
def main():
    input_str = input("Введите строку: ")
    word_count = count_words(input_str)
    print("Количество слов в строке:", word_count)
if __name__ == "__main__":
    main()
def swap_words(input_str):
    words = input_str.split()
    swapped_str = words[1] + " " + words[0]
    return swapped_str

def main():
    input_str = input("Введите строку из двух слов, разделенных пробелом: ")
    swapped_str = swap_words(input_str)
    print("Получившаяся строка:", swapped_str)
if __name__ == "__main__":
    main()
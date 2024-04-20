words = ["open", "close", "pizza", "you", "watermelon"]
def longest_word_for(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
def longest_word_while(words):
    longest = ""
    i = 0
    while i < len(words):
        if len(words[i]) > len(longest):
            longest = words[i]
        i += 1
    return longest

# Проверяем результаты
print("Самое длинное слово (for цикл):", longest_word_for(words))
print("Самое длинное слово (while цикл):", longest_word_while(words))
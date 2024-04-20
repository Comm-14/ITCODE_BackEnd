def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
a = input("Введите строку: ")
if palindrome(a):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
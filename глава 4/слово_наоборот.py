# просим ввести слово
# создаем новое слово начиная с конца и выводим
# профит
word = input("Введите любое слово: ")
new_word = ""
for i in range(-1, -len(word)-1, -1):
    new_word += word[i]
print(new_word)
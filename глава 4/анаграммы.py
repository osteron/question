# Анаграммы (Word Jumble)
#
# Компьютер выбирает какое-либо слово и хаотически переставляет его буквы
# Задача игрока - восстановить исходное слово
import random
# создадим последовательность слов, из которых ПК будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
# случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)
# создадим переменную, с которой буде затем сопоставлена версия игрока
correct = word
# создадим анаграмму выбранного слова, в которой буквы будут расставлены хаотично
jumble = ""
# создадим счетчик попыток
counter = 1
# подсказка
prompt = ""
# итоговый балл
total = 9
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
# начало игры
print(
    """
                    Добро пожаловать в игру "Анаграммы"!
        Надо переставить буквы так, чтобы получилось осмысленное слово.
                        У Вас есть десять попыток.
            (Для выхода нажмите Enter, не вводя своей версии)
    """
)
print("Вот анаграмма:", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "" and total > 0:
    total -= 1
    # print("К сожалению, вы неправы.")
    guess = input("Попробуйте отгадать исходное слово: ")
    counter += 1
    if counter % 3 == 0:
        answer = input("Вы хотите подсказку? Введите 'да', если хотите. Она будет стоить 3 балла.\n")
        # если попросил подсказку
        if answer.lower() == "да":
            print("Вот подсказка:")
            for i in range(0, len(correct) // 2, 1):
                prompt += correct[i]
            print(prompt)
            total -= 3
        else:
            print("Ваше право.\n")
if guess == correct:
    print("Да, именно так! Вы отгадали!\n")
if total <= 0:
    print("Увы, но Вы проиграли.")
else:
    print("Спасибо за игру. Ваш итоговый балл равен", total, "очков.")
input("\nНажмите Enter, чтобы выйти")
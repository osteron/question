# Симулятор трехлетнего ребенка
# Демонстрирует работу цикла while

print("\tДобро пожаловать в программу 'Симулятор трехлетнего ребенка'\n")
print("Имитируется разговор с маленьким ребенком.")
print("Попробуйте остановить этот кошмар.\n")
response = ""
while response != "потому что":
    response = input("Почему?\n").lower()
print("А, ладно.")
input("\n\nНажмите Enter, чтобы выйти.")
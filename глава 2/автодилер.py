# Эта программа помогает расчитать суммы налогов, регистрационных
# сборов, агентских сборов и цену доставки машины по месту
# назначения. Достаточно ввести цену автомобиля

price = int(input("Введите цену автомобиля: "))
nalog = int(price * 0.05)
reg_sbor = int(price * 0.02)
agent_sbor = 3000
delivery = 10000
total = price + nalog + reg_sbor + agent_sbor + delivery
print("Налог:", nalog, "\nРегистрационный сбор:", reg_sbor, "\nАгентский сбор:", agent_sbor)
print("Доставка:", delivery)
print("Итоговая сумма:", total,"рублей")
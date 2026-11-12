import random

print("Загадай число от 1 до 100. Я попробую угадать!")
low = 1
high = 100
while True:
    guess = random.randint(low, high)
    print(f"Мой вариант: {guess}")
    answer = input("Твоё число больше, меньше или я угадал? ").strip().lower()
    if answer == "больше":
        low = guess + 1
    elif answer == "меньше":
        high = guess - 1
    elif answer == "угадал":
        print("Ура! Я угадал!")
        break
    else:
        print("Пиши: 'больше', 'меньше' или 'угадал'.")

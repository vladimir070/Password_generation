import random
import string # чтоб не писать всё вручную

# херня с буквами и символами (генерим)
x = string.ascii_letters + string.punctuation # ВСЕ буквы (большие и маленькие) и знаки !@#$%^&*() и тд
letters = [] # список для букв/символов
for _ in range(6): # Увеличили количество - делаем пароль побольше
    char = random.choice(x) # выбираем
    letters.append(char) # кладём в список

# херня с цифрами (генерим)
z = string.digits # все цифры от 0 до 9
numbers = [] # список для цифр
for _ in range(6): # больше цифр тоже надо
    number = random.choice(z) # выбираем
    numbers.append(number) # кладём в список

# всё вместе (обьединяем и перемешиваем)
all_chars = letters + numbers # обьеденяем
random.shuffle(all_chars) # перемешиваем
password = "".join(all_chars) # делаем из списка строку (пароль)

# вывод пароля
print(f"Пароль: {password}")
# 3а допомогою колекції deque реалізуйте структуру даних FIFO. 
# Створіть змінну fifo, що містить колекцію deque. Обмежте розмір за допомогою константи MAX_LEN.
# Функція push додає значення element до кінця списку fifo. Функція pop дістає та повертає перше значення зі списку fifo.

# Імпортуємо клас deque з модуля collections
from collections import deque

# Визначаємо константу для максимальної довжини FIFO
MAX_LEN = 10

# Створюємо змінну fifo, що містить колекцію deque
fifo = deque(maxlen=MAX_LEN)

# Визначаємо функцію для додавання елемента до кінця fifo
def push(element):
    # Додаємо елемент до правого краю fifo за допомогою методу append
    fifo.append(element)

# Визначаємо функцію для вилучення елемента з початку fifo
def pop():
    # Перевіряємо, чи fifo не порожній
    if fifo:
        # Вилучаємо та повертаємо елемент з лівого краю fifo за допомогою методу popleft
        return fifo.popleft()
    # Інакше повертаємо None
    else:
        return None
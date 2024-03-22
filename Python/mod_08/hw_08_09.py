# Списки у Python реалізовані таким чином, що вибір елемента по індексу відбувається за константний час (дуже швидко) і додавання/видалення елементу в кінець списку теж відбувається дуже швидко. Але ось додавання елементу у будь-яке інше місце в списку змушує Python перерахувати індекси усіх елементів списку до кінця. Для великих списків це може бути дуже невигідно. Щоб швидко додавати елементи в початок списку, в Python в пакеті collections є така колекція як deque:
#
#from collections import deque
#
#d = deque()
#d.append('last')
#d.appendleft('first')
#d.insert(1, 'middle')
#print(d)  # deque(['first', 'middle', 'last'])
#
#print(d.pop())  # 'last'
#print(d.popleft())  # 'first'
#print(d)  # deque(['middle'])
#
# Окрім додавання в початок за допомогою appendleft, у deque є і швидке видалення першого елементу popleft.
#
# Ще однією особливістю deque є можливість обмежити розмір deque:
#
#from collections import deque
#
#d = deque(maxlen=5)
#for i in range(10):
#    d.append(i)
#
#print(d)  # deque([5, 6, 7, 8, 9], maxlen=5)
#
#Як видно з прикладу, нові елементи витісняють старіші, але розмір залишається незмінним.
#
# В іншому deque веде себе точно як список Python
#
# За допомогою колекції deque для списків треба реалізувати структуру даних LIFO. 
# Отже створіть змінну lifo, що містить колекцію deque. Далі обмежте розмір за допомогою константи MAX_LEN. Функція push додає значення element на початок списку lifo. Функція pop дістає та повертає перше значення зі списку lifo.

# Import the deque class from the collections module
from collections import deque

# Define a constant for the maximum length of the LIFO
MAX_LEN = 10

# Create a lifo variable containing the deque collection
lifo = deque(maxlen=MAX_LEN)

# Define a function to push an element to the beginning of the lifo
def push(element):
    # Append the element to the left of the lifo using the appendleft method
    lifo.appendleft(element)

# Define a function to pop an element from the beginning of the lifo
def pop():
    # Check if the lifo is not empty
    if lifo:
        # Pop and return the element from the left of the lifo using the popleft method
        return lifo.popleft()
    # Otherwise, return None
    else:
        return None
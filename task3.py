
n = int(input("write number of your array: "))
arr = list(map(int, input(f"write your {n} elements: ").split()))[:n]
max_element = max(arr)
negative_elements = []
for x in arr:
    if x < 0:
        negative_elements.append(x)

# Обчислюємо середнє арифметичне (із захистом від ділення на 0)
if negative_elements:
    avg_negative = sum(negative_elements) / len(negative_elements)
else:
    avg_negative = "відсутні"

# 5. Знаходимо парні від'ємні елементи у зворотному порядку
even_negative_reversed = []
for x in arr:
    if x < 0 and x % 2 == 0:
        # Вставляємо на початок списку (індекс 0), щоб одразу отримати зворотний порядок
        even_negative_reversed.insert(0, x)

print(f"Максимум: {max_element}")
print(f"Середнє від'ємних: {avg_negative}")
print(f"Парні від'ємні у зворотному порядку: {even_negative_reversed}")
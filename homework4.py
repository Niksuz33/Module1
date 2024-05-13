# Создайте переменную immutable_var и присвойте ей кортеж из нескольких
# элементов разных типов данных.
# Выполните операции вывода кортежа immutable_var на экран.
immutable_var = 1, 2, 'hello', True
print(immutable_var)
print('Immutable tuple: ', immutable_var)

immutable_var = tuple([1, 2, 'hello', True])
print(immutable_var)

# Попытайтесь изменить элементы кортежа immutable_var.
# immutable_var [1] = 300

# Объясните, почему нельзя изменить значения элементов кортежа.
# Ответ:  Потому что кортежи это НЕизменяемый тип коллекций

# Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
# Измените элементы списка mutable_list.
# Выведите на экран измененный список mutable_list.

mutable_list = ["Duke", "Nuken", True, "Forever", 100500]
print('Mutable list: ', mutable_list)
mutable_list [0] = "DIN"
mutable_list [1] = "Jarren"
print('Mutable list Modified:', mutable_list)

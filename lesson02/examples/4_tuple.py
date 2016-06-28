# =================================
#             Кортежи
# =================================

# Кортеж - НЕизменяемая последовательность, элементами которой могут быть любые типы данных
empty_tuple = ()  # Пустой кортеж
my_tuple = (1, 4, 'Hello', [1, 2, 5], 1.5)

my_tuple_2 = 2, 4, 6  # Так тоже кортеж

# Кортеж созжают не скобки, а наличие запятых
tup1 = (4)  # Так получится Int
print("type(tup1) --> ", type(tup1))

tup2 = 2, 4 # А так кортеж
print("type(tup2) --> ", type(tup2))

# Изменить элементы кортежа нельзя
# my_tuple[0] = 5  <-- ошибка

# В остальном кортеж подобен списку

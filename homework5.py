immutable_var = 'Позитив', 42, True
print(immutable_var)
# immutable_var[2] = False
# print(immutable_var)
print('Неизменяемость кортежей обусловлена необходимостью держать данные в неизменном виде, легким доступом к ним и экономией памяти')
mutable_list = ['Чапа-чапа', 100, False]
print(mutable_list)
mutable_list[0] = 'чипи-чипи'
mutable_list[1] = -100
mutable_list[2] = True
print(mutable_list)
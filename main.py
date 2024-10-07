# module_3_3.ru

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list_2 = [54.32, 'Строка' ]
print_params()
print_params(5,456)
print_params(*values_list_2, 42)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(5, 12, c=None)

values_list_3 = [32.23, 'Привет', [1, 2, 6] ]
print_params(values_list_3)
values_dict = {'a':456, 'b':'Удачи', 'c':[23, 12, 44]}
print_params(values_dict)   #Dic,
print_params(*values_dict)
print_params(**values_dict)



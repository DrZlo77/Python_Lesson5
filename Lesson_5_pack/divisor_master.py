
'''
Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
Модуль содержит функции:
'''

#==================================================================================
from builtins import range

'''
1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
'''
def simp_number(number):

    '''
    :param number: Целое число для проверки
    :return:являеться ли число натуральным
    '''

    if type(number)== float:
       print("Это дробь, введите целое число")
       return

    if type(number) != int:
       print("Введите целое число")
       return

    counter_coincidences = 0

    for counter in range(number):

        if int(number/(counter+1)) == float (number/(counter+1)):
            counter_coincidences += 1

    if counter_coincidences > 2:
        # print('Число не является простым')
        return False
    else:
        # print('Число является простым')
        return True


#==================================================================================
'''
2) выводит список всех делителей числа;
'''
def divider_number (number):
    '''
    :param number: Целое число
    :return: список со всеми делителями числа
    '''

    if type(number)== float:
       print("Это дробь, введите целое число")
       return

    if type(number) != int:
       print("Введите целое число")
       return


    divider_list = []

    for num in range(number):
        if (number/(num+1)).is_integer():
            divider_list.append(int((number/(num+1))))
    return divider_list

#==================================================================================
'''
3) выводит самый большой простой делитель числа.
'''
def most_plain_divider (number):
    '''

    :param number: Целое число
    :return: Самое большое просто число являющееся делителем входящего числа
    '''

    if type(number)== float:
       print("Это дробь, введите целое число")
       return

    if type(number) != int:
       print("Введите целое число")
       return

    divider_list = divider_number(number)

    divider_list.sort()
    divider_list.reverse()

    simp_divider = []

    for divider in divider_list:
        if simp_number(divider):
            simp_divider.append(divider)
    print(simp_divider)

    return simp_divider[0]


#==================================================================================
'''
4) функция выводит каноническое разложение числа на простые множители;
'''
def canon_decomposition_number (number):
    '''
    :param number: Целое число
    :return: простые множители числа
    '''
    if type(number) == float:
        print("Это дробь, введите целое число")
        return

    if type(number) != int:
        print("Введите целое число")
        return

    factor_list = []

    if simp_number(number): # Если число простое возвращаем его же и 1
        factor_list.append(1)
        factor_list.append(number)
        return factor_list

    prime_divider = []
    for a in range(1,number): # получаем все простые делители входящего числа
        if number%a==0 and simp_number(a):
            prime_divider.append(a)
    #print(prime_divider)
    prime_divider.remove(1)

    type_number = number
    step_factor = []
    for divi in prime_divider: # получаем простой список моножителей входящего числа путем деления входящего числа на простые делители
        while type_number%divi == 0: # полученные выше, пока число делиться без остатка
            step_factor.append(divi) # пишем делитель в список множителей
            type_number = type_number/divi # с каждым витком цикла анализируемое число уменьшаем путем деления на делитель
    #print(step_factor)
    dict_factor = {}
    dict_factor = {factor:step_factor.count(factor) for factor in step_factor} # создаем словарь ключами которого будут множетели, а значения это количество повторейний

    formula = f''

    for key,values in dict_factor.items(): # выводим формулу в строку

        formula = formula + f'*{str(key)}^{str(values)}'
    formula = formula[1:len(formula)]
    return formula

#==================================================================================
'''
5) функция выводит самый большой делитель (не обязательно простой) числа. 
'''

def most_big_divider (number):
    '''
    :param number: Целое число
    :return: Самый большой делитель числа(нужно не оно само, насколько я понял )
    '''

    if type(number) == float:
        print("Это дробь, введите целое число")
        return

    if type(number) != int:
        print("Введите целое число")
        return

    if number == 1:
        return 1
    elif number == 0:
        return 'Введи больше нуля'

    max_div = divider_number(number)
    max_div.sort()
    max_div.reverse()
    max_div.remove(max(max_div))
    return max_div[0]

# print(most_plain_divider(100))


# print(most_big_divider(8889))
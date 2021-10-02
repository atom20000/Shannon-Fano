# import sys
# Надо переписать ввод на многострочный, пока для реализации самого алгоритма
# сделаем однострочный ввод
def symbol_code(arr, sym):
    for i in arr:
        Code[i[0]]+=sym
    return
def Shennon(list_):
    probab_coeff = sum(map(lambda x: x[1], list_))/2
    prom_sum = 0
    for i in range(len(list_)):
        prom_sum += list_[i][1]
        if prom_sum >= probab_coeff:
            index = i + (abs(prom_sum - probab_coeff) < abs(prom_sum - list_[i][1] - probab_coeff))
            break
        
#Теоретически можно везде сделать +1 к индесу, но это менее эффективно по сравнению с этим спопобом.
    
    symbol_code(list_[:index],'1')
    symbol_code(list_[index:],'0')
    
    if len(list_[:index])!=1:
        Shennon(list_[:index])

    if len(list_[index:])!=1:
        Shennon(list_[index:])
orig_text = input()
unic_char = sorted(list(set(orig_text)))
len_text = len(orig_text)
list_frequ = sorted([(char,round(orig_text.count(char)/len_text, 4)) for char in unic_char],key = lambda x: (-x[1], x[0]))
Code = {char : '' for char in unic_char}
print('Список типа: "символ" - "частота появления"\n',list_frequ)
Shennon(list_frequ)
print('Словарь типа: "символ" - "код"\n',Code)
print('Закодированное сообщение:\n', ''.join([Code[i] for i in orig_text]))

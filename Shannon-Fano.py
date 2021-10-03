from sys import stdin
from math import log2
# Надо переписать ввод на многострочный, пока для реализации самого алгоритма
# сделаем однострочный ввод (Уже сделали)

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
    
    symbol_code(list_[:index],'0')
    symbol_code(list_[index:],'1')
    
    if len(list_[:index])!=1:
        Shennon(list_[:index])

    if len(list_[index:])!=1:
        Shennon(list_[index:])
def Huffman(list_):
    while len(list_)>1:
        two_elem = list_.pop()
        one_elem = list_.pop()
        list_.append(((one_elem[0],two_elem[0]),round(one_elem[1]+two_elem[1],4)))
        list_.sort(key = lambda x: -x[1])
    encode_tree(list_[0][0],'')
    
def encode_tree(tuple_,sym):
    if isinstance(tuple_[0],str):
        symbol_code([[tuple_[0]]],sym+'0')
    else:
        encode_tree(tuple_[0],sym+'0')
    if isinstance(tuple_[1],str):
        symbol_code([[tuple_[1]]],sym+'1')
    else:
        encode_tree(tuple_[1],sym+'1')
def Choice_and_output():
    choice = input('1-Шеннон-Фано\n2-Хаффман\n')
    if choice=='1':
        Shennon(list_frequ.copy())
    elif choice=='2':
        Huffman(list_frequ.copy())
    else:
        print('Так и не выбрали как кодировать')
        return
    
    print('|','Cимвол','|','Вероятность','|','Код',' '*7,'|')
    print('|','_'*6,'|','_'*11,'|','_'*11,'|')
    for i in list_frequ:
        print('|',i[0],' '*(5-len(str(i[0]))),'|',i[1],' '*(10-len(str(i[1]))),'|',Code[i[0]],' '*(10-len(str(Code[i[0]]))),'|')
        print('|','_'*6,'|','_'*11,'|','_'*11,'|')
        
    #print('Список типа: "символ" - "частота появления"\n',list_frequ)
    #print('Словарь типа: "символ" - "код"\n',Code)
    print('Закодированное сообщение:\n',''.join([Code[i] if i!='\n' else i+' ' for j in input_ for i in j]))
    print('-'*100)

    entropy = round(-sum([(i[1]*log2(i[1])) for i in list_frequ]),4)
    print('Энтропия -- ', entropy)
    averg_len = round(sum([ i[1]*len(Code[i[0]]) for i in list_frequ]),4)
    print('Средняя длина кода -- ', averg_len)
    print(f'Критерий эффективности\n Абсолютный: {round(averg_len-entropy,4)}\n Относительный: {round((averg_len-entropy)/entropy*100, 4)} %')

if __name__ == '__main__':
    #orig_text = input()
    input_ = stdin.readlines()
    orig_text = ''.join(map(lambda x: x.rstrip(),input_))

    unic_char = sorted(list(set(orig_text)))
    len_text = len(orig_text)
    list_frequ = sorted([(char,round(orig_text.count(char)/len_text, 4)) for char in unic_char],key = lambda x: (-x[1], x[0]))
    Code = {char : '' for char in unic_char}
    Choice_and_output()

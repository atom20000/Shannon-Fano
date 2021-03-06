from sys import stdin
from math import log2
from anytree import Node, RenderTree
from anytree.exporter import DotExporter


root = Node('root')

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
    encode_tree(list_[0][0],'',root)
    
def encode_tree(tuple_,sym,parent):
    if isinstance(tuple_[0],str):
        symbol_code([[tuple_[0]]],sym+'0')
        last_node = Node(sym+'0',parent)
        Node(tuple_[0],last_node)
    else:
        encode_tree(tuple_[0],sym+'0',Node(sym+'0',parent))
    if isinstance(tuple_[1],str):
        symbol_code([[tuple_[1]]],sym+'1')
        last_node = Node(sym+'1',parent)
        Node(tuple_[1],last_node)
    else:
        encode_tree(tuple_[1],sym+'1',Node(sym+'1',parent))

def Encode(code_text):
    Code_char = { i[1] : i[0] for i in Code.items()}
    encode_text=''
    sym =''
    for i in code_text:
        sym+=i
        if Code_char.get(sym.strip()) != None:
            encode_text+=Code_char[sym.strip()]
            sym=''
        elif sym == '\n': 
            encode_text+=(sym+' ')
            sym = ''
    return encode_text


def Choice_and_output():
    choice = input('1-Шеннон-Фано\n2-Хаффман\n')
    name_file = input('Название файла сохранения\n')
    if choice=='1':
        Shennon(list_frequ.copy())
        name_file = name_file+'_sh.txt'
    elif choice=='2':
        Huffman(list_frequ.copy())
        DotExporter(root).to_picture(f'{name_file}_tre_ha.png')
        name_file = name_file+'_ha.txt'
    else:
        print('Так и не выбрали как кодировать')
        return
    with open(name_file,'w') as file:
        file.write(''.join(('|','Cимвол','|','Вероятность','|','Код',' '*8,'|','\n')))
        file.write(''.join(('|','_'*6,'|','_'*11,'|','_'*11,'|','\n')))
        for i in list_frequ:
            file.write(''.join(('|',i[0],' '*(6-len(i[0])),'|',str(i[1]),' '*(11-len(str(i[1]))),'|',Code[i[0]],' '*(11-len(str(Code[i[0]]))),'|','\n')))
            file.write(''.join(('|','_'*6,'|','_'*11,'|','_'*11,'|','\n')))
        
    #print('Список типа: "символ" - "частота появления"\n',list_frequ)
    #print('Словарь типа: "символ" - "код"\n',Code)
        code_text = ''.join([Code[i] if i!='\n' else i+' ' for j in input_ for i in j])
    #print('Закодированное сообщение:\n', code_text)
        file.write(''.join(('-'*100,'\n')))

        entropy = round(-sum([(i[1]*log2(i[1])) for i in list_frequ]),4)
        file.write(''.join(('Энтропия -- ', str(entropy),'\n')))
        averg_len = round(sum([ i[1]*len(Code[i[0]]) for i in list_frequ]),4)
        file.write(''.join(('Средняя длина кода -- ', str(averg_len),'\n')))
        file.write(f'Критерий эффективности\n Абсолютный: {round(averg_len-entropy,4)}\n Относительный: {round((averg_len-entropy)/entropy*100, 4)} % \n')
        file.write(''.join(('-'*100,'\n')))
        file.write(Encode(code_text))

if __name__ == '__main__':
    #orig_text = input()
    print('Текст для кодирования:')
    input_ = stdin.readlines()
    orig_text = ''.join(map(lambda x: x.rstrip(),input_))

    unic_char = sorted(list(set(orig_text)))
    len_text = len(orig_text)
    list_frequ = sorted([(char,round(orig_text.count(char)/len_text, 4)) for char in unic_char],key = lambda x: (-x[1], x[0]))
    Code = {char : '' for char in unic_char}
    Code_char = {}
    Choice_and_output()

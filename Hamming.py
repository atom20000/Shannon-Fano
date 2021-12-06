code = list(input())
i = 0
while pow_ := 2**i:
    if pow_ <= len(code):
        code.insert(pow_-1,'0')
        i+=1
    else:
        break

print(''.join(code), '       ', len(code))

def sum_bit(list_code, step):
    sum_bit = 0
    for j in range(step):
        #import pdb;pdb.set_trace()
        sum_bit+=sum(list(map(lambda x : int(x), (list_code[step-1+j::step*2]))))
    return sum_bit

j = 0
code_copy = code.copy()
while pow_ := 2**j:
    if pow_ <= len(code):
        code[pow_-1] = str(sum_bit(code,pow_)%2)
        code_copy[pow_-1] = str(sum([sum(list(map(lambda x : int(x), (code_copy[pow_-1+i::pow_*2])))) for i in range(pow_)])%2)
        j+=1
    else:
        break
print(''.join(code), '       ', len(code))
print(''.join(code_copy), '       ', len(code_copy))


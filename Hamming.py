import numpy
class Hamming():   

    def __init__(self):
        self.code = list(input())

    def insert_ex_bit(self):
        i = 0
        while pow_ := 2**i:
            if pow_ <= len(self.code):
                self.code.insert(pow_-1,'0')
                i+=1
            else:
                break
        self.print_code()
        #print(''.join(self.code), '       ', len(self.code))


    def _sum_bit(list_code, step):
        sum_bit = 0
        for j in range(step):
            #import pdb;pdb.set_trace()
            sum_bit+=sum(list(map(lambda x : int(x), (list_code[step-1+j::step*2]))))
        return sum_bit

    def print_code(self):
        for i, ch in enumerate(self.code):
            if i%4 == 0: print(' ', end='')
            if bin(i+1).count('1') == 1:
                print(f'\x1b[31m{ch}\x1b[0m', end='')
            else:
                print(f'\x1b[37m{ch}\x1b[0m', end='')

    def create_code(self):
        j = 0
        #code_copy = code.copy()
        while pow_ := 2**j:
            if pow_ <= len(self.code):
                self.code[pow_-1] = str(self._sum_bit(self.code,pow_)%2)
                #code_copy[pow_-1] = str(sum([sum(list(map(lambda x : int(x), (code_copy[pow_-1+i::pow_*2])))) for i in range(pow_)])%2)
                j+=1
            else:
                break
        self.print_code()
        #print(''.join(code), '       ', len(code))
        #print(''.join(code_copy), '       ', len(code_copy))
    def check_error(self):
        j = 0
        error_bit = 0
        while pow_ := 2**j:
            if pow_ <= len(self.code):
                if self._sum_bit(self.code,pow_)%2>0:
                    error_bit +=pow_
                j+=1
            else:
                break
        return error_bit

    def corrected_code(self):
        error_bit = self.check_error()
        if error_bit:
            self.code[error_bit-1] = '0' if int(self.code[error_bit-1]) else '1'
        
class SumNumBy():

    def __init__(self):
        a = bin(int(input('первое число ')))
        b = bin(int(input('второе число ')))

        self.a = list(a[a.index('b')+1:])[::-1]
        self.b = list(b[b.index('b')+1:])[::-1]

        size = max(len(self.a),len(self.b))

        self.a += ['0']*(size - len(self.a))
        self.b += ['0']*(size - len(self.b))

        self.a += ['1' if a[0] == '-' else '0']
        self.b += ['1' if b[0] == '-' else '0']

    def prum_to_back_code(self,num):
        b = list(map(lambda x: '0' if int(x)==1 else '1', num[:len(num)-1]))
        b += num[-1]
        return b

    def prum_to_extation_code(self,num):
        b = self.back_code(num)
        edin = ['1']+['0']*(len(num)-1)
        b = self.sum_num(b, edin)
        return b

    def sum_num(self,num1,num2):
        overflow = 0
        res = []
        for o in zip(num1,num2):
            value = int(o[0]) + int(o[1]) + overflow
            overflow = value//2
            res.append(str(value%2))
        return res
    
    def sum_num_class_value(self):
        self.a = self.extation_code(self.a) if self.a[-1] == '1' else self.a
        self.b = self.extation_code(self.b) if self.b[-1] == '1' else self.b
        return self.sum_num(self.a, self.b)

    def extation_to_back_code(self, num):
        edin = ['1']+['0']*(len(num)-2)+['1']
        b = self.sum_num(num,edin)
        return b 

class Entropy():
    
    def __init__(self):
        self.mat = numpy.array(
            [
                [.3, .2, 0.000000000000001],
                [0.0000000000000001, .05, .1],
                [0.0000000000000001, .1, .25]
            ],
            numpy.float64
        )
        self.P_x = numpy.sum(self.mat, axis=1)
        self.P_y = numpy.sum(self.mat, axis=0)
        self.P_x_Y = self.mat/self.P_x

    @property
    def H_X(self):
        return numpy.sum(-self.P_x*numpy.log2(self.P_x))

    @property
    def H_Y(self):
        return numpy.sum(-self.P_y*numpy.log2(self.P_y))

    @property
    def H_x_Y(self):
        return numpy.sum(-self.mat*numpy.log2(self.P_x_Y))

    @property
    def H_X_Y(self):
        return numpy.sum(-self.mat*numpy.log2(self.mat))

    @property
    def E_X_Y(self):
        return numpy.sum(self.H_X+self.H_Y-self.H_Y)

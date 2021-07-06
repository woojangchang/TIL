# complex number
complex1 = 2 + 4j
complex2 = -1 + 3j
complex3 = complex1 * complex2
print(f'{complex1}*{complex2} = {complex3}')
print('real :', complex3.real, 'imag :', complex3.imag)
print('conjugate :', complex3.conjugate())
print('abs :', abs(complex3))

'''
(2+4j)*(-1+3j) = (-14+2j)
real : -14.0 imag : 2.0
conjugate : (-14-2j)
abs : 14.142135623730951
'''
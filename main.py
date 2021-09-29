'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
    p = 1
    for v in lst:
        p *= v
    return p

'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    rest = x % y
    while rest != 0:
        x = y
        y = rest
        rest = x % y
    return y

def main():
    print(is_prime(3))
    print(is_prime(6))
    print(get_product([3, 4, 5]))
    print(get_cmmdc_v1(12,8))
    print(get_cmmdc_v2(12,8))

if __name__ == '__main__':
    main()
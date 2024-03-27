import unittest

def is_prime(num):
    if num <= 1:   
        return False  #si un numero es menor o igual a 1 no es primo
    divisor = 2  #inicializa la variable divisor 
    while divisor * divisor <= num:  #mientras que el divisor multiplicado por el mismo sea menor o igual que el numero
        if num % divisor == 0:   #si el resto de la division entre el numero y el divisor es cero
            return False   #devuelve falso
        divisor += 1  #se incrementa el valor del divisor
    return True   #devuelve verdadero

    
class Test_is_prime(unittest.TestCase):
    
    def test_0(self):
        num = is_prime(0)
        self.assertFalse(num)


    def test_1(self):
        num = is_prime(1)
        self.assertFalse(num)

    def test_2(self):
        num = is_prime(2)
        self.assertTrue(num)

    def test_3(self):
        num = is_prime(3)
        self.assertTrue(num)

    def test_4(self):
        num = is_prime(4)
        self.assertFalse(num)

    def test_5(self):
        num = is_prime(5)
        self.assertTrue(num)

    def test_6(self):
        num = is_prime(6)
        self.assertFalse(num)

    def test_7(self):
        num = is_prime(7)
        self.assertTrue(num)

    def test_53(self):
        num = is_prime(53)
        self.assertTrue(num)
    

if __name__ == '__main__':
    unittest.main()
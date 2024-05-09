import unittest

def CalcularMCD(nro1,nro2):

#Algoritmo para hallar el Maximo Comun Divisor
    while nro2!=0:
        temp = nro1 
        nro1 = nro2 
        nro2 = temp % nro2 

    return nro1

class TestMCD(unittest.TestCase):

    def test_mcd_2numeros(self):
        esperado = 2
        actual = CalcularMCD(6,8)
        self.assertEqual(actual,esperado)
    
    def test_mcd_4numeros(self):
        esperado = 3
        actual = CalcularMCD(CalcularMCD(CalcularMCD(9,12),6),15)
        self.assertEqual(actual,esperado)

    def tearDown(self):
        #Aqui va lo contrario cuando el test ha terminado
        pass

#LLamar al modulo principal para ejecutar las pruebas unitarias
if __name__ == '__main__':
    unittest.main()
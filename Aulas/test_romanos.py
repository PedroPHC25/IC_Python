import unittest
from romanos import num_romanos

class TesteRomanos(unittest.TestCase):
    def test_um(self):
        um = num_romanos(1)
        self.assertEqual('I', um)

    def test_zero(self):
        zero = num_romanos(0)
        self.assertEqual('', zero)

    def test_dois(self):
        dois = num_romanos(2)
        self.assertEqual('II', dois)

    def test_tres(self):
        tres = num_romanos(3)
        self.assertEqual('III', tres)

    def test_quatro(self):
        quatro = num_romanos(4)
        self.assertEqual('IV', quatro)

    def test_cinco(self):
        cinco = num_romanos(5)
        self.assertEqual('V', cinco)

    def test_seis(self):
        seis = num_romanos(6)
        self.assertEqual('VI', seis)

    def test_sete(self):
        sete = num_romanos(7)
        self.assertEqual('VII', sete)

    def test_oito(self):
        oito = num_romanos(8)
        self.assertEqual('VIII', oito)

    def test_nove(self):
        nove = num_romanos(9)
        self.assertEqual('IX', nove)

    def test_dez(self):
        dez = num_romanos(10)
        self.assertEqual('X', dez)

    def test_onze(self):
        onze = num_romanos(11)
        self.assertEqual('XI', onze)

    def test_doze(self):
        doze = num_romanos(12)
        self.assertEqual('XII', doze)

    def test_treze(self):
        treze = num_romanos(13)
        self.assertEqual('XIII', treze)

if __name__ == '__main__':
    unittest.main()
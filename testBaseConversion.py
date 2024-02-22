from baseConversion import dec_to_base_convert
from baseConversion import base_to_dec_convert
import unittest

class TestDecToBaseConvert(unittest.TestCase):
    
    def test_dec_to_base_convert_invalid_decNum(self):
        self.assertEqual(-1, dec_to_base_convert(-1, 2))
        self.assertEqual(-1, dec_to_base_convert(-100, 5))

    def test_dec_to_base_convert_invalid_base(self):
        self.assertEqual(-1, dec_to_base_convert(10, -1))
        self.assertEqual(-1, dec_to_base_convert(10, 0))
        self.assertEqual(-1, dec_to_base_convert(10, 1))
        self.assertEqual(-1, dec_to_base_convert(10, 36))
        self.assertEqual(-1, dec_to_base_convert(10, 37))
        
    def test_dec_to_base_convert(self):
        self.assertEqual("11111101000", dec_to_base_convert(2024, 2))
        self.assertEqual("3750", dec_to_base_convert(2024, 8))
        self.assertEqual("7E8", dec_to_base_convert(2024, 16))
        self.assertEqual("714", dec_to_base_convert(1024, 12))
        self.assertEqual(-1, dec_to_base_convert(-155, 4))
        self.assertEqual("DG", dec_to_base_convert(250, 18))

    def test_base_to_dec_convert_invalid_num_str(self):
        self.assertEqual(-1, base_to_dec_convert("-1", 16))
        self.assertEqual(-1, base_to_dec_convert("-100", 5))

    def test_base_to_decconvert_invalid_base(self):
        self.assertEqual(-1, base_to_dec_convert("123", -1))
        self.assertEqual(-1, base_to_dec_convert("123", 0))
        self.assertEqual(-1, base_to_dec_convert("123", 1))
        self.assertEqual(-1, base_to_dec_convert("123", 36))
        self.assertEqual(-1, base_to_dec_convert("123", 37))
        
    def test_base_to_dec_convert(self):
        self.assertEqual(2024, base_to_dec_convert("11111101000", 2))
        self.assertEqual(2024, base_to_dec_convert("3750", 8))
        self.assertEqual(2024, base_to_dec_convert("7E8", 16))
        self.assertEqual(1024, base_to_dec_convert("714", 12))
        self.assertEqual(-1, base_to_dec_convert("-155", 4))
        self.assertEqual(250, base_to_dec_convert("DG", 18))

if __name__ == '__main__':
    unittest.main()



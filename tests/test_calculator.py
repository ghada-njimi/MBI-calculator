import unittest
from bmi_calculator.calculator import calculate_bmi
from bmi_calculator.utils import bmi_category

class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.8571, places=4)
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)

    def test_bmi_category(self):
        self.assertEqual(bmi_category(17), "Insuffisance pondérale")
        self.assertEqual(bmi_category(22), "Poids normal")
        self.assertEqual(bmi_category(27), "Surpoids")
        self.assertEqual(bmi_category(32), "Obésité")

if __name__ == "__main__":
    unittest.main()

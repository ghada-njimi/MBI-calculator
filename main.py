"""Point d'entrée du programme."""

from bmi_calculator.calculator import calculate_bmi
from bmi_calculator.utils import bmi_category

def main():
    print("=== Calculateur d'IMC ===")
    try:
        weight = float(input("Entrez votre poids (kg) : "))
        height = float(input("Entrez votre taille (m) : "))
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.")
        return

    try:
        bmi = calculate_bmi(weight, height)
    except ValueError as e:
        print(f"Erreur : {e}")
        return

    category = bmi_category(bmi)

    print(f"\nVotre IMC est : {bmi:.2f}")
    print(f"Catégorie : {category}")


if __name__ == "__main__":
    main()

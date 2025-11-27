"""Module pour le calcul de l'IMC."""

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calcule l'IMC.
    :param weight_kg: poids en kg
    :param height_m: taille en m
    :return: IMC
    """
    if height_m <= 0:
        raise ValueError("La taille doit être supérieure à 0.")
    return weight_kg / (height_m ** 2)

"""Fonctions utilitaires pour l'IMC."""

def bmi_category(bmi: float) -> str:
    """Retourne la catégorie associée à un IMC."""
    if bmi < 18.5:
        return "Insuffisance pondérale"
    elif 18.5 <= bmi < 25:
        return "Poids normal"
    elif 25 <= bmi < 30:
        return "Surpoids"
    else:
        return "Obésité"

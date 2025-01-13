#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule la factorielle d'un entier non négatif.
    Args:
        n (int): Nombre entier dont on veut calculer la factorielle.
    Returns:
        int: Factorielle de n.
    Raises:
        ValueError: Si n est négatif.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def main():
    """
    Point d'entrée principal du script. Gère les arguments, exécute la factorielle
    et affiche le résultat.
    """
    try:
        if len(sys.argv) != 2:
            raise ValueError("Please provide exactly one integer argument.")
        
        n = int(sys.argv[1])  # Convertit l'argument en entier
        
        # Limiter la taille de n pour éviter les dépassements de mémoire
        if n > 10000:
            raise ValueError("The number is too large to compute a factorial.")
        
        f = factorial(n)
        print(f"The factorial of {n} is {f}.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExecution interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Exécuter le script uniquement si appelé directement
if __name__ == "__main__":
    main()

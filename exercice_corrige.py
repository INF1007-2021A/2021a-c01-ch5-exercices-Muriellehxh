#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


def indice(essai, reponse):
    indices = []
    essai = [input('Entrez un chiffre: '), input('Entrez un chiffre:'), input('Entrez un chiffre:'), input('Entrez un chiffre:')









def convert_to_absolute(number: float) -> float:
    if number > 0:
        pass
    else:
        number = -1 * number
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    List = [prefixes[0]+suffixe, prefixes[1]+suffixe, prefixes[2]+suffixe, prefixes[3]+suffixe, prefixes[4]+suffixe, prefixes[5]+suffixe, prefixes[6]+suffixe, prefixes[6]+suffixe]
    return [List]

def prime_integer_summation() -> int:
    prime = [2, 3, 5,]
    number = 6
    while len(prime) < 100:
        is_prime = True
        for diviseur in range(2, number // 2):
            if number % diviseur == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(number)

        number += 1

    return sum(prime)

def factorial(number: int) -> int:
    factorielle = 1

    for el in range(1, number + 1):
        factorielle = factorielle * el
    return factorielle



def use_continue() -> None:
    for number in range(1,10):
        if number == 5:
            continue
        else:
            print(number)



def verify_ages(groups: List[List[int]]) -> List[bool]:  # corrigé

    acceptance = []
    for group in groups:
        if len(group) > 10 or len(group) <= 3:  # if group respects conditions, acceptance <= False
            acceptance.append(False)
            continue  # BYPASSES next statements to start another for loop
        if 25 in group:
            acceptance.append(True)
            continue  # BYPASSES next statements to start another for loop
        if (min(group) < 18) or (50 in group and max(group) > 70):  # skip statement => False
            acceptance.append(False)
            continue  # SKIPS the next lines!!! Starts another for loop

        acceptance.append(True)

    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()

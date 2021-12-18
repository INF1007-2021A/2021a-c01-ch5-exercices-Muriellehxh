#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List



def convert_to_absolute(number: float) -> float:
    if number < 0:
        return number*-1
    else:
        return number



def use_prefixes() -> List[str]:
    prefixes = 'JKLMNOPQ'
    suffixe = 'ack'

    length = 0
    for char in prefixes:
        length += 1

    n = 0
    list_name = []
    while n<length:
        list_name.append(prefixes[n] + suffixe)
        n+=1

    return list_name


def prime_integer_summation() -> int:

    list_prime = []
    numbers_totest = range(1,1000)
    for number in numbers_totest:
        for div_number in numbers_totest:
            if div_number == number:
                continue
            elif number % div_number != 0:
                list_prime.append(number)

    addition = sum(list_prime)
    return addition


def factorial(number: int) -> int:
    n = 1
    for num in range(1, number+1):
        n *= num
    return n

def use_continue() -> None:
    pass



def verify_ages(groups: List[List[int]]) -> List[bool]:
    pass


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

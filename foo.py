#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def number_to_words(number, country='france'):
    """Convert a number to its writing in french.

    The country keyword allows to specify how to handle the 70, 80 and 90
    cases."""

    country = country.lower()
    if country not in ('france', 'belgique', 'suisse'):
        raise ValueError('Unknown country {}'.format(country))

    unique_names = {
        1: "un",
        2: "deux",
        3: "trois",
        4: "quatre",
        5: "cinq",
        6: "six",
        7: "sept",
        8: "huit",
        9: "neuf",
        10: "dix",
        11: "onze",
        12: "douze",
        13: "treize",
        14: "quatorze",
        15: "quinze",
        16: "seize"
        }
    tens_name = {
        1: "dix",
        2: "vingt",
        3: "trente",
        4: "quarante",
        5: "cinquante",
        6: "soixante",
        7: "septante",
        8: "huitante" if country == "suisse" else "quatre-vingt",
        9: "nonante"
    }

    if number < 17:
        return unique_names[number]

    tens = number // 10
    units = number % 10

    if country == 'france' and tens in (7, 9):
        # Cas des 70 et 90 en France
        if number == 71:
            # Exception pour 71: soixante-et-onze
            return "soixante-et-onze"
        rest = number - (tens-1) * 10
        result = tens_name[tens-1] + "-" + number_to_words(rest, country=country)
        return result

    result = tens_name[tens]

    if units == 0:
        return result
    elif units == 1 and not (country in ("france", "belgique") and tens == 8):
        # Ajout de "et-un" sauf pour "quatre-vingt-un" en France et en Belgique
        result += "-et-un"
    else:
        result += "-" + unique_names[units]

    return result

if __name__ == '__main__':
    assert number_to_words(81) == "quatre-vingt-un"
    assert number_to_words(81, country="suisse") == "huitante-et-un"
    assert number_to_words(99) == "quatre-vingt-dix-neuf"
    assert number_to_words(74) == "soixante-quatorze"
    assert number_to_words(99, country='belgique') == "nonante-neuf"
    assert number_to_words(99) == "quatre-vingt-dix-neuf"
    assert number_to_words(93) == "quatre-vingt-treize"
    assert number_to_words(71) == "soixante-et-onze"
    assert number_to_words(71, country="belgique") == "septante-et-un"
    assert number_to_words(70) == "soixante-dix"
    assert number_to_words(50) == "cinquante"
    assert number_to_words(80) == "quatre-vingt"


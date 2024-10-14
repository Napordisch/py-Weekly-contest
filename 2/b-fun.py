arabic = int(input())
roman_numeral_letters = {1: "I",
                         5: "V",
                         10: "X",
                         50: "L",
                         100: "C",
                         500: "D",
                         1000: "M"}
numerals = tuple(roman_numeral_letters.keys())
difference = arabic
roman = ""

while difference != 0:
    diffs = tuple(map(lambda kit: abs(difference) - kit, numerals))
    min_difference = min(map(abs, diffs))

    if min_difference in diffs:
        chosen = numerals[diffs.index(min_difference)]
    elif -min_difference in diffs:
        chosen = numerals[diffs.index(-min_difference)]

    print(chosen)

    if difference > 0:
        roman = roman + roman_numeral_letters[chosen]
        difference -= chosen
    elif difference < 0:
        roman = roman_numeral_letters[chosen] + roman
        difference += chosen


print(roman)

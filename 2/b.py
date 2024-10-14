arabic = int(input())
roman_numeral_letters = {1: "I",
                         4: "IV",
                         5: "V",
                         9: "IX",
                         10: "X",
                         40: "XL",
                         50: "L",
                         90: "XC",
                         100: "C",
                         400: "CD",
                         500: "D",
                         900: "CM",
                         1000: "M"}


numerals = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
difference = arabic
roman = ""

for i in numerals:
    while arabic >= i and arabic >= 0:
        roman = roman + roman_numeral_letters[i]
        arabic -= i


print(roman)
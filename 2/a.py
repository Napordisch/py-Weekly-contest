our_string = input()

palindrome_length = 0

letter_counts = dict()

used_letters = []

for character in our_string:
    if character not in used_letters:
        amount_of_this_character = our_string.count(character)
        if amount_of_this_character % 2 == 0:
            palindrome_length += amount_of_this_character
        else:
            palindrome_length += amount_of_this_character - 1

        used_letters.append(character)


if len(our_string) - palindrome_length > 0:
    palindrome_length += 1

print(palindrome_length)

#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_1_Functions


def letter_count(word, letter):
    count = 0
    for string in word:  # There is a specific string that we are going to look for
        # String is a particular letter (not case-sensitive) in any word(s)
        if string.lower() == letter or string.upper() == letter:  # Count upper and lowercase
            count += 1  # Running count
    return count


# print(letter_count('helloworLd', 'l'))
# print('Mary had a little Lamb'.count('l' or 'L'))

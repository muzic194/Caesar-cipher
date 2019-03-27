import operator

alphabet = "abcdefghijklmnopqrstuvwxyz"  # English Alphabet


# alphabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż' # Polski alfabet

def replace_letter(letter, n):
    """Function takes letter_1 and returns letter_2 which is n-times on the left in alphabet"""

    index = ((alphabet.find(letter.lower())) + n) % len(alphabet)  # find letter in alphabet (alphabet is variable defined above function - but can be inside)
    alphabet_upper = alphabet.upper()  # prepare variable before for loop to not make .upper() method in each iteration

    if letter in alphabet:  # for small letters
        letter = alphabet[index]

    elif letter in alphabet_upper:  # for big letters
        letter = alphabet_upper[index]

    else:  # for everything that is not a letter - white holders, numbers, !@#$%^&*()_+ etc.
        letter = letter  # does not replace for anything - stay the same
    return letter


def code(string, n):
    """From some string return coded string"""

    return "".join([replace_letter(c, n) for c in string])


def decode(string, frequent_letter):
    """Chose your own frequent letter and check how decode works - English: e, t, Polish: a, i, e, o
    Function returns translation with the most frequent "frequent_letter"""

    results = []  # list with translations for each n i alphabet
    frequencies = []  # list with frequencies of frequent letter in each translation

    for n in range(len(alphabet)):
        results.append(code(string, n))
        frequencies.append((code(string, n)).count(frequent_letter))

    return results[frequencies.index(
        max(frequencies))]  # this function returns only first most frequent translation (what if there are more max?)

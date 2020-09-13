# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
file_object = open('ciphertext.txt')
data = file_object.read()
file_object.close

word_list = data.split()

frequency_order = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L",
                   "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

letter_count_table = dict()

for word in word_list:
    for char in word:
        if char.isalpha():
            if char not in letter_count_table:
                letter_count_table[char] = 1
            else:
                letter_count_table[char] += 1
        else:
            continue

letter_count_items = list(letter_count_table.items())
letter_count_items.sort(key=lambda pair: pair[1], reverse=True)

mapped_characters = dict()

for i in range(len(letter_count_items)):
    mapped_characters[letter_count_items[i][0]] = frequency_order[i]


def decode(s):
    decoded_string = ''

    for char in s:
        if char.isalpha():
            decoded_string += mapped_characters[char]
        else:
            decoded_string += char

    return decoded_string


decoded_words = map(decode, word_list)
print(' '.join(decoded_words))

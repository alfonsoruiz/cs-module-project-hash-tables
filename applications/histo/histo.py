import re


def sort_dictionary(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)


def print_histogram(word_count_table):
    longest_word = ''
    special_chars = '" : ; , . - + = / \' | [ ] { } ( ) * ^ & ? !'
    special_char_table = dict.fromkeys(special_chars.split(), True)

    for word, value in word_count_table:
        word = word.lower().replace(' ', '')

        for char in word:
            if char in special_char_table:
                word = word.replace(char, '')

        if len(word) > len(longest_word):
            longest_word = word

        print(f'{word}')


def word_count_histogram(file_name):
    file_obj = open(file_name, 'r')
    text_file = file_obj.read()
    word_list = text_file.split()
    file_obj.close()

    # Data Structures:
    # Create lookup table to keep track of words in text file
    word_table = {}

    # Loop:
    # Split string on white space to isolate words
    # Loop through txt file
    # if word is in lookup table add 1 to the value
    # else add word to lookup table
    for word in word_list:
        if word in word_table:
            word_table[word] += 1
        else:
            word_table[word] = 1

    print_histogram(word_table)


word_count_histogram('robin.txt')

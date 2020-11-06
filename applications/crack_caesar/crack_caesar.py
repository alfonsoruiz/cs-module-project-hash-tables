with open('ciphertext.txt', 'r') as cypher_text:
    text = cypher_text.read()

    # Create lookup table
    def char_count_lookup(txt):
        lookup = {}

        for char in text:
            if char.isalpha():
                if char in lookup:
                    lookup[char] += 1
                else:
                    lookup[char] = 1
            else:
                continue
        return sort_dictionary(lookup)

    # Sort dictionary by value
    def sort_dictionary(dictionary):
        return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

    # Map characters by frequency
    def map_chars(dictionary):
        freq_order = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L",
                      "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]
        key_map = {}

        for n in range(len(freq_order)):
            key_map[dictionary[n][0]] = freq_order[n]

        return key_map

    # Decode text
    def decode_txt(txt, char_map):
        decoded_txt = ''

        for char in text:
            if char.isalpha():
                char = char_map[char]
                decoded_txt += char
            else:
                decoded_txt += char

        print(decoded_txt)

    sorted_char_count_dictionary = char_count_lookup(text)
    char_map = map_chars(sorted_char_count_dictionary)
    decode_txt(text, char_map)

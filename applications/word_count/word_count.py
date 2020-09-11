def word_count(s):
    word_count = dict()
    words = s.split()
    ignore_chars = '":;,.-+=/\\|[]{}()*^&'

    for word in words:
        word = word.lower().strip(ignore_chars)

        if word == '':
            continue

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


if __name__ == "__main__":
    print(word_count(''))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))

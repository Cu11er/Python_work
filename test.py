# def caesar_cipher(string, shift):
#     char_list = [(alphabet[(alphabet.index(sym) - shift) % 26] if sym != ' ' else ' ') for sym in string.lower()]
#     new_str = ''
#     for i_char in char_list:
#         new_str += i_char
#     return new_str


def shift_word(word, shift):
    if shift != 0:
        return word[shift % len(word):] + word[:shift % len(word)]
    else:
        return word


text = input("Введите текст: ")
alphabet = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'.split(', ')

new_text = [alphabet[(alphabet.index(letter) - 1) % len(alphabet)] if letter in alphabet else letter for letter in
            text.lower()]
new_text = ''.join(new_text)
new_text_list = new_text.split()

shift = -3
message_2_list = list()
for word in new_text_list:
    message_2_list.append(shift_word(word, shift))
    if '/' in word:
        shift -= 1

print(' '.join(message_2_list).replace('/', '\n'))

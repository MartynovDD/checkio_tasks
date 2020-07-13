"""
Your task is to decrypt the secret message using the Morse code.
The message will consist of chars with 3 spaces between them and 1 space between each letter of each char.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.
https://py.checkio.org/en/mission/morse-decoder/
"""
from utils.type_checker import type_checker


MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code: str) -> str:
    """
    Decodes given morse code
    :param code: a string of morse code
    :return: decoded string
    """
    type_checker(str, code)
    code_list = code.split("   ")
    for group in code_list:
        group_index = code_list.index(group)
        code_list[group_index] = group = group.split()
        for char in group:
            index = group.index(char)
            if char in MORSE.keys():
                group[index] = MORSE[char]
            if index == 0 and group_index == 0:
                group[index] = group[index].upper()

    words_list = ["".join(group) for group in code_list]
    return " ".join(words_list)

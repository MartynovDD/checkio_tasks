"""
Your task is to decrypt the secret message using the Morse code.
The message will consist of chars with 3 spaces between them and 1 space between each letter of each char.
If the decrypted text starts with a letter then you"ll have to print this letter in uppercase.
https://py.checkio.org/en/mission/morse-decoder/
"""
from utils.check_type import check_type

MORSE = {".-": "a", "-...": "b", "-.-.": "c",
         "-..": "d", ".": "e", "..-.": "f",
         "--.": "g", "....": "h", "..": "i",
         ".---": "j", "-.-": "k", ".-..": "l",
         "--": "m", "-.": "n", "---": "o",
         ".--.": "p", "--.-": "q", ".-.": "r",
         "...": "s", "-": "t", "..-": "u",
         "...-": "v", ".--": "w", "-..-": "x",
         "-.--": "y", "--..": "z", "-----": "0",
         ".----": "1", "..---": "2", "...--": "3",
         "....-": "4", ".....": "5", "-....": "6",
         "--...": "7", "---..": "8", "----.": "9"
         }


def morse_decoder(code: str) -> str:
    """
    Decodes given morse code
    :param code: a string of morse code
    :return: decoded string
    """
    check_type(str, code)

    encoded_words = code.split("   ")
    decoded_words = []

    for encoded_word in encoded_words:
        decoded_word = get_decoded_word(encoded_word)
        decoded_words.append(decoded_word)
    decoded_string = " ".join(decoded_words)

    decoded_string = decoded_string.capitalize()

    return decoded_string


def get_decoded_word(encoded_word: str) -> str:
    encoded_symbols = encoded_word.split()
    decoded_symbols = []

    for encoded_symbol in encoded_symbols:
        decoded_symbol = get_decoded_symbol(encoded_symbol)
        decoded_symbols.append(decoded_symbol)
    decoded_word = "".join(decoded_symbols)

    return decoded_word


def get_decoded_symbol(encoded_symbol: str) -> str:
    return MORSE.get(encoded_symbol, "")

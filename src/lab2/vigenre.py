'''
Шифр Виженера
функции:
1) encrypt_vigenere - зашифровка сообщения
2) decrypt_vigenere - расшифровка сообщения
'''

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    plaintext1 = plaintext.lower()
    keyword = keyword.lower() * 10000
    alph = "abcdefghijklmnopqrstuvwxyz" * 1000
    keyword = keyword[:len(plaintext) + 1]
    shift = []
    for i in range(len(keyword)):
        shift.append(alph.index(keyword[i]))
    for j in range(len(plaintext1)):
        ciphertext += alph[alph.index(plaintext1[j]) + shift[j]]
    if plaintext.isupper():
        ciphertext = ciphertext.upper()
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    ciphertext1 = ciphertext.lower()
    keyword = keyword.lower() * 10000
    alph = "abcdefghijklmnopqrstuvwxyz" * 1000
    keyword = keyword[:len(ciphertext) + 1]
    shift = []
    for i in range(len(keyword)):
        shift.append(alph.index(keyword[i]))
    for j in range(len(ciphertext1)):
        plaintext += alph[alph.index(ciphertext1[j]) - shift[j]]
    if ciphertext.isupper():
        plaintext = plaintext.upper()
    return plaintext
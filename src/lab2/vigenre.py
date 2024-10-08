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
    if plaintext.isupper() == True:
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
    # PUT YOUR CODE HERE
    return plaintext
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if 65 <= ord(plaintext[i]) <= 90:
            if ord(chr(ord(plaintext[i]) + shift)) > ord("Z"):
                ciphertext += chr(ord("A") + (shift - (91 - ord(plaintext[i]))))
            else:
                ciphertext += chr(ord(plaintext[i]) + shift)
        elif 97 <= ord(plaintext[i]) <= 122:
            if ord(chr(ord(plaintext[i]) + shift)) > ord("z"):
                ciphertext += chr(ord("a") + (shift - (123 - ord(plaintext[i]))))
            else:
                ciphertext += chr(ord(plaintext[i]) + shift)
        else:
            ciphertext += chr(ord(plaintext[i]))
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        if 65 <= ord(ciphertext[i]) <= 90:
            if ord(chr(ord(ciphertext[i]) - shift)) < ord("A"):
                plaintext += chr(ord("Z") - (shift - (ord(ciphertext[i]) - ord("A") + 1)))
            else:
                plaintext += chr(ord(ciphertext[i]) - shift)
        elif 97 <= ord(ciphertext[i]) <= 122:
            if ord(chr(ord(ciphertext[i]) - shift)) < ord("a"):
                plaintext += chr(ord("z") - (shift - (ord(ciphertext[i]) - ord("a") + 1)))
            else:
                plaintext += chr(ord(ciphertext[i]) - shift)
        else:
            plaintext += chr(ord(ciphertext[i]))
    return plaintext
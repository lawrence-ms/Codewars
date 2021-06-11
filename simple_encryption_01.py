# https://www.codewars.com/kata/57814d79a56c88e3e0000786

def decrypt(encrypted_text, n):
    if encrypted_text is None:
        return None
    encrypt_lenght = len(encrypted_text)
    second_chars = encrypted_text[:encrypt_lenght//2]
    other_chars = encrypted_text[encrypt_lenght//2:]
    if n <= 0:
        return encrypted_text
    else:
        for pos in range(len(other_chars)):
                encrypted_text += other_chars[pos] + second_chars[pos:pos+1]
        return decrypt(encrypted_text[encrypt_lenght:], n - 1)

def encrypt(text, n):
    second_chars = ""
    other_chars = ""
    if n <= 0:
        return text
    else:
        for pos in range(len(text)):
            if pos % 2 != 0:
                second_chars += text[pos]
            else:
                other_chars += text[pos]
        return encrypt(second_chars + other_chars, n - 1)

def palindrome(string):
    # assert
    assert len(string) > 0, "No se puede ingresar una cadena vacía"
    return string == string[::-1]


if __name__ == '__main__':
    is_palindrome = palindrome("jose")
    if is_palindrome:
        print("es un palindromo")
    else:
        print("No es un palindromo")
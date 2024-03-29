import vigenere

# Transposition cipher
# Character limit: only alphabetic characters, converted to lower case.
# If text length is not multiple of key length, letter "X"-s will be padded to text until text length is multiple of key length
def transposition(text, keyLength, encrypt = True):

    cleanedText = ''.join(filter(str.isalpha, text.lower()))

    if len(cleanedText) % keyLength > 0: # Check text length
        if not encrypt: # Cipher text must be multiple of key length
            return None
        else: # Add padding
            for i in range(keyLength - (len(cleanedText) % keyLength)):
                cleanedText += "x"
    
    chunkLength = keyLength if encrypt else len(cleanedText) // keyLength # Determine length of chunks
    chunkList = [ cleanedText[startPos:startPos+chunkLength] for startPos in range(0,len(cleanedText),chunkLength) ] # split text into chunks

    resultText = ""

    for i in range(chunkLength):
        for chunk in chunkList:
            resultText += chunk[i]

    return resultText

# Demo
if __name__ == '__main__':
    plain = "sistem dan teknologi informasi itb"
    plain2 = "gacor rEk1"
    length = 6
    key = "INDO"

    print("Vigenere key: ", key)
    print("Transposition k (chunk length): ", length)

    print("\nTransposition cipher test")
    print("Plain: ", plain2, " -> ", transposition(transposition(plain2, length), length, False))
    print("Cipher: ", transposition(plain2, length))
    print("Decrypted: ", transposition(transposition(plain2, length), length, False))

    print("\nProduct cipher test")
    print("Plain: ", plain, " -> ", transposition(transposition(plain, length), length, False))
    print("Cipher: ", transposition(vigenere.vigenere(plain, key), length))
    print("Decrypted: ", vigenere.vigenere(transposition(transposition(vigenere.vigenere(plain, key), length), length, False), key, False))
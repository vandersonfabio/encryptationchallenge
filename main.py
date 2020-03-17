def letterToNumber(char):
    if (char.isupper()):
        return ord(char) - 65
    else:
        return ord(char) - 97


def caesarEncrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

            # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def caesarDecrypt(text, s):
    result = ""
    s = 26 - s

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

            # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def vigenereEncrypt(plainText, secret):
    result = ""

    for i in range(len(plainText)):
        char = plainText[i]
        result += caesarEncrypt(char, letterToNumber(secret[i % len(secret)]))

    return result


def vigenereDecrypt(plainText, secret):
    result = ""

    for i in range(len(plainText)):
        char = plainText[i]
        result += caesarDecrypt(char, letterToNumber(secret[i % len(secret)]))

    return result


def generateMatrix():
    matrix = []

    number = 97

    for i in range(5):
        line = []
        for j in range(5):
            line.append(chr(number))
            number += 1
        matrix.append(line)

    return matrix


def tranposeMatrix(matrix):
    aux = []

    for j in range(len(matrix[0])):
        line = []
        for i in range(len(matrix)):
            line.append(matrix[i][j])
        aux.append(line)
    return aux

def mostra_matriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j] + '\t', end='')
        print("")
    print('_' * 10)


def polybusDecript(text):
    result = ""
    matrix = tranposeMatrix(generateMatrix())

    for i in range(0, len(text), 2):
        result += matrix[int(text[i]) - 1][int(text[i + 1]) - 1]

    return result

def convertBinToBase4(binaryString):
    result = ""

    for i in range(0, len(binaryString), 3):
        char = binaryString[i:i+3]
        result += str(int(char, 2))

    return result

if __name__ == '__main__':
    blockA = "gluhtlishjrvbadvyyplkaokqvbxjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk"
    blockB = "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzkifkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"

    encryptedText = 'klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn'

    text = "445411345411233353445412424342443251412123113113531554425442444243443251415343543242344111255135533413424322534311445434534322513431421432513412533412155415345133514444112251444254424444153451235515432134511113112123514254315333214243514453153414345125425315443351543253414443513544"

    secret = "SSKKUULLLL"

    print("Bloco A : " + caesarEncrypt(blockA, 19))
    print("Bloco B : " + caesarEncrypt(blockB, 23))

    print("* " * 50)
    print("Dica 02 : " + vigenereDecrypt(encryptedText, secret))

    a = polybusDecript(text)
    print("* " * 50)
    print("Dica 03 : " + a)

    encryptedText = 'klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn'
    ux = ""

    simbolMessage = "20 33 22 21 00 33 30 01 02 20 22 02 32 20 11 33 03 30 03 32 03 00 22 01 33 23 23 10 03 22 13 13 20 01 11 03 22 20 20 20 22 33 20 13 23 13 33 22 30 33 01 20 21 10 12 11 00 32 23 13 22 02 00 10 31 02 33 20 31 03 12 01 11 33 32 23 02 01 00 32 10 10 30 01 10 23 31 10 02 00 30 23 31 10 03 03 01 02 33 02 23 21 30 12 03 12 22 00 03 13 31 00 10 11 21 03 23 02 20 13 02 32 30 31 23 33 20 02 12 33 30 00 30 12 30 13 03 01 03 03 23 22 02 30 20 03 22 23 32 23 02 02 31 20 23 13 30 02"

    simbolMessage = simbolMessage.replace(" ", "")


    key = ""

    for i in range(len(ux)):
        char = ux[i]
        if ord(char) == 97 or ord(char) == 101 or ord(char) == 105 or ord(char) == 111 or ord(char) == 117:
            key += "1"
        else:
            key += "0"

    print(simbolMessage)

    simbolBinary = ""
    for bit in range(len(simbolMessage)):
        bin = ""
        if simbolMessage[bit] == '0':
            bin = "00"
        if simbolMessage[bit] == '1':
            bin = "01"
        if simbolMessage[bit] == '2':
            bin = "10"
        if simbolMessage[bit] == '3':
            bin = "11"

        simbolBinary += bin

    print(simbolBinary)

    simbolBase4 = convertBinToBase4(simbolBinary)
    print()
    print(simbolBase4)

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


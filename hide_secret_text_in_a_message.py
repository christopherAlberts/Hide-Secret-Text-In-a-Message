import requests


def hide_secret_text_in_a_message():
    while True:

        encodeOrDecoded = input("Encode or Decode (Or 'X' to exit.): ")

        if encodeOrDecoded == "Encode" or encodeOrDecoded == "encode" or encodeOrDecoded == "E" or encodeOrDecoded == "e":

            hiddenPhrase = input("Enter hidden phrase: ")
            publicPhrase = input("Enter public phrase: ")

            hiddenPhrase = hiddenPhrase.replace(' ', '+')
            publicPhrase = publicPhrase.replace(' ', '+')

            result = requests.get(
                'https://neatnik.net/steganographr/api?public=' + publicPhrase + '&private=' + hiddenPhrase)

            result = result.content
            result = result.decode("utf-8")

            print("Here is your encrypted message:")
            print("###############################\n")
            print(result)
            print("\n###############################")

        elif encodeOrDecoded == "Decode" or encodeOrDecoded == "decode" or encodeOrDecoded == "D" or encodeOrDecoded == "d":

            decodePhrase = input("Enter phrase to decode: ")
            result2 = requests.get('https://neatnik.net/steganographr/api?decode=' + decodePhrase)

            print("Here is your decrypted message:")
            print("###############################\n")
            print(result2.content.decode("utf-8"))
            print("\n###############################")

        elif encodeOrDecoded == 'X' or encodeOrDecoded == 'x':
            break

        else:
            print("Error: Input does not match")


if __name__ == "__main__" :
    hide_secret_text_in_a_message()
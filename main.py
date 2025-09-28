print("""                                                                                                                     
 _____         _      _          _____                    _____       _        _____                     _           
|_   _|___ _ _| |_   | |_ ___   |     |___ ___ ___ ___   |     |___ _| |___   |     |___ ___ _ _ ___ ___| |_ ___ ___ 
  | | | -_|_'_|  _|  |  _| . |  | | | | . |  _|_ -| -_|  |   --| . | . | -_|  |   --| . |   | | | -_|  _|  _| -_|  _|
  |_| |___|_,_|_|    |_| |___|  |_|_|_|___|_| |___|___|  |_____|___|___|___|  |_____|___|_|_|\_/|___|_| |_| |___|_|  
                                                                                                                     """)
print("Welcome to our secret machine")
ask = True
while ask:
    text = input('Please Type your text here:').upper()
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..--', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
        ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'  # Space separator
    }
    answer = ''
    for character in text:
        for symbol, value in MORSE_CODE_DICT.items():
            if character == symbol:
                answer += value

    print(f"Here Is Your Morse Code:{answer}")
    ask_to_continue = True
    while ask_to_continue:
        continue_convert = input("Do you have another text to convert? answer with Y/N").upper()
        if continue_convert == "Y":
            ask_to_continue = False
        elif continue_convert == "N":
            ask_to_continue = False
            ask = False
        else:
            print("Invalid answer!")

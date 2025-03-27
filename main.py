# Create Morse code dictionary
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': ' '
}

# Create reverse dictionary for decoding
reverse_morse = {value: key for key, value in morse_dict.items()}

def text_to_morse(text):
    morse_code = []
    for word in text.upper().split():
        morse_word = []
        for char in word:
            if char in morse_dict:
                morse_word.append(morse_dict[char])
        morse_code.append(' '.join(morse_word))
    return ' / '.join(morse_code)

def morse_to_text(morse):
    text = []
    for morse_word in morse.split(' / '):
        chars = []
        for code in morse_word.split():
            if code in reverse_morse:
                chars.append(reverse_morse[code])
        text.append(''.join(chars))
    return ' '.join(text)

while True:
    print("\nOptions:")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        text = input("Enter the text to convert to Morse code: ")
        print("Morse Code:", text_to_morse(text))
    elif choice == '2':
        morse = input("Enter the Morse code to convert to text (use space between letters and ' / ' between words): ")
        print("Decoded Text:", morse_to_text(morse))
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
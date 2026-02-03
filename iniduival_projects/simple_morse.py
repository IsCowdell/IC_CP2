#IC 1st Simple morse code
# making a tuple for the letters which is unchanaglbable btw
ENGLISH_LETTERS = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '
)
#making atuple for symbols 
MORSE_SYMBOLS = (
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
    '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
    '..-', '...-', '.--', '-..-', '-.--', '--..', '/'   # slash used for space
)
# defing the english to morse and setting message as a paraimater
def english_to_morse(msg):
    #creating an empty string 
    morse_output = " "
#making sure the messages are lower
    msg = msg.lower()
# checks wgere it is in the tuple
    for char in msg:
        if char in ENGLISH_LETTERS:
            #
            index = ENGLISH_LETTERS.index(char)
            morse_output += MORSE_SYMBOLS[index]
        #making sure there is no whitespaces
    return  morse_output.strip()
#defing function for morse to english 
def morse_to_english(code):
    #empty string
    english_output = " "
    morse_chars = code.split()
#while loop to check if which sysymbols are in the code
    for symbol in morse_chars:
        # if they do exist in code 
        if symbol in MORSE_SYMBOLS:
            #adding it onto it
            index = MORSE_SYMBOLS.index(symbol)
            #defing it newly
            english_output += ENGLISH_LETTERS[index]
    #showing it again
    return english_output

def main():
    #making a while loop to end the loop if they choose that option
    while True:
        #giving the user rights to choose hwat they want to do 
        print("1. Translate from Morse Code to English")
        print("2. Translate from English to Morse Code")
        print("3. Exit")
        #defing the user input as a variable
        choice = input("Pick: ")
        #if uuer chooses morse code to enlgish 
        if choice == "1":
            #asking for user input and what code should be translated
            morse_input = input("What is the code you need translated?")
            #showing user what the messahe is
            print("Your message says: ")
            #feeds inpout into function
            print(morse_to_english(morse_input))
            #if the choice is 2 then
        elif choice == "2":
            #ask user what messahe they need changesd
            english_input = input("What is the message you need translated?")
            #show user message what message says
            print("Your message says: ")
            #feeds inpout into function
            print(english_to_morse(english_input))
            #leting user leave if wanted
        elif choice == "3":
            break
main()
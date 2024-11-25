from morse_translater import text_to_morse
from grammar_parser import parse_sentence

def translate_and_parse():
    text_input = input("Enter Text: ")
    translated_morse = text_to_morse(text_input)
    print(f"Translated Morse Code: {translated_morse}")
    sentence = text_input.lower().split()
    parse_sentence(sentence)

def main():
    print("Welcome to the English-to-Morse Translator and Sentence Parser!")
    while True:
        command = input("Type 'translate' to convert text to Morse, 'exit' to quit: ").strip().lower()
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "translate":
            translate_and_parse()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

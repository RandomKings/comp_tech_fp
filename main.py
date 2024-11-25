# main.py
from morse_translater import text_to_morse
from grammar_parser import parse_sentence

def main():
    sentence = input("Enter a sentence to translate to Morse code: ")
    
    # Parse the sentence and check its validity
    parse_result = parse_sentence(sentence)
    
    if parse_result["is_valid"]:
        # Display the parse tree in the console
        print("Parse Tree:")
        parse_tree = parse_result["tree"]
        parse_tree.pretty_print()  # Using NLTK's pretty_print for visual clarity
        
        # Translate to Morse code
        morse_code = text_to_morse(sentence)
        print("\nMorse Code Translation:")
        print(morse_code)
    else:
        print("The sentence does not follow proper grammar.")
        print("Error:", parse_result["error"])

if __name__ == "__main__":
    main()

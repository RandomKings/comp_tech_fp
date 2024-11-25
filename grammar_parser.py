import nltk
from nltk import CFG
from word_dictionary import word_dict

# Dynamically generate grammar based on the dictionary
nouns = ' | '.join([f"'{noun}'" for noun in word_dict['nouns']])
verbs = ' | '.join([f"'{verb}'" for verb in word_dict['verbs']])
adverbs = ' | '.join([f"'{verb}'" for verb in word_dict['adverbs']])
determiners = ' | '.join([f"'{det}'" for det in word_dict['determiners']])
prepositions = ' | '.join([f"'{prep}'" for prep in word_dict['prepositions']])

# Grammar definition
grammar = CFG.fromstring(f"""
    S -> NP VP
    NP -> DT NN | NN
    VP -> Vt NP | Vi | VP PP
    PP -> IN NP
    Vi -> {adverbs}
    Vt -> {verbs}
    NN -> {nouns}
    DT -> {determiners}
    IN -> {prepositions}
""")

def parse_sentence(sentence):
    parser = nltk.ChartParser(grammar)
    
    # Ensure `sentence` is a string and then split it by spaces to get words as tokens
    if isinstance(sentence, list):
        # If sentence is a list of characters, join it into a single string first
        sentence = ''.join(sentence)
    
    # Convert to lowercase and split into words
    tokens = sentence.lower().split()
    print(f"Tokens: {tokens}")  # Debugging line to show tokens
    
    parsed_trees = list(parser.parse(tokens))
    
    if parsed_trees:
        for tree in parsed_trees:
            tree.pretty_print()
    else:
        print("The sentence could not be parsed.")



if __name__ == "__main__":
    # Example sentence input (after Morse code translation)
    sentence = input("Enter sentence: ").upper()  # Example: "the man saw the dog in the park"
    parse_sentence(sentence)

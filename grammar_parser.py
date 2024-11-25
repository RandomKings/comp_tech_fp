import nltk
from nltk import CFG
from word_dictionary import word_dict

# Dynamically generate grammar based on the dictionary
nouns = ' | '.join([f"'{noun}'" for noun in word_dict['nouns']])
verbs = ' | '.join([f"'{verb}'" for verb in word_dict['verbs']])
adverbs = ' | '.join([f"'{adv}'" for adv in word_dict['adverbs']])
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
        sentence = ''.join(sentence)
    
    # Convert to lowercase and split into words
    tokens = sentence.lower().split()
    
    # Attempt to parse the sentence and handle errors with detailed feedback
    try:
        parsed_trees = list(parser.parse(tokens))
        if parsed_trees:
            return {"is_valid": True, "tree": parsed_trees[0]}
        else:
            # If parsing fails, attempt to provide more specific error feedback
            error_position = find_error_position(tokens, parser)
            return {
                "is_valid": False,
                "error": f"Invalid structure at position {error_position}."
            }
    except ValueError as e:
        return {"is_valid": False, "error": f"Grammar error: {str(e)}"}

def find_error_position(tokens, parser):
    last_successful_index = -1  # Track the last successful token index
    for i in range(len(tokens)):
        try:
            # Attempt parsing up to and including the i-th token
            partial_tokens = tokens[:i+1]
            list(parser.parse(partial_tokens))  # Try parsing the partial input
            last_successful_index = i  # Update the last successful index if parsing succeeds
        except ValueError:
            break  # Stop at the first failure and report the last successful token's index
    return last_successful_index

def tokenize_sentence(sentence):
    return sentence.lower().split()  # Simple tokenization for the GUI display

if __name__ == "__main__":
    # Example sentence input (after Morse code translation)
    sentence = input("Enter sentence: ").upper()  # Example: "the man saw the dog in the park"
    result = parse_sentence(sentence)
    if result["is_valid"]:
        print("Valid sentence:", sentence)
    else:
        print("Error:", result["error"])

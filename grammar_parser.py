import nltk
from nltk import CFG
from word_dictionary import word_dict

nouns = ' | '.join([f"'{noun}'" for noun in word_dict.get('nouns', [])])
adjectives = ' | '.join([f"'{adj}'" for adj in word_dict.get('adjectives', [])])
adverbs = ' | '.join([f"'{adv}'" for adv in word_dict.get('adverbs', [])])
pronouns = ' | '.join([f"'{pron}'" for pron in word_dict.get('pronouns', [])])
determinants = ' | '.join([f"'{det}'" for det in word_dict.get('determinants', [])])
conjunctions = ' | '.join([f"'{conj}'" for conj in word_dict.get('conjunctions', [])])
verbs = ' | '.join([f"'{verb}'" for verb in word_dict.get('verbs', [])])
verbs_trans = ' | '.join([f"'{verb}'" for verb in word_dict.get('verb_trans', [])])
verbs_intrans = ' | '.join([f"'{verb}'" for verb in word_dict.get('verb_intrans', [])])
prepositions = ' | '.join([f"'{prep}'" for prep in word_dict.get('prepositions', [])])


# Define the CFG grammar
grammar = CFG.fromstring(f"""
    S -> NP VP
    S -> VP
    S -> NP
    S -> NP VP PP
    S -> S Conj S
    
    NP -> Det Noun
    NP -> AdjP Noun
    NP -> Det AdjP Noun
    NP -> Noun
    NP -> Pronoun
    NP -> NP PP
    NP -> AdjP Noun
    NP -> Det AdjP Noun

    VP -> Verb
    VP -> VerbIntrans
    VP -> VerbTrans NP
    VP -> VerbIntrans Adv
    VP -> LinkingVerb VerbIntrans Adv
    VP -> VerbTrans NP PP
    VP -> Verb PP
    VP -> Verb NP
    VP -> LinkingVerb AdjP
    VP -> LinkingVerb Adv AdjP
    VP -> Verb NP VP
    VP -> VP AdvP

    PP -> Prep NP
    PP -> PP PP

    LinkingVerb -> 'is' | 'are' | 'was' | 'were'  
    
    Adj -> {adjectives}
    AdjP -> Adv Adj
    AdjP -> Adj
    AdjP -> AdvP Adj
    AdjP -> Adj Adj
    AdjP -> AdjP Conj AdjP

    Adv -> {adverbs}
    AdvP -> Adv
    AdvP -> AdvP Adv
    AdvP -> Adv Adv
    AdvP -> AdvP Conj AdvP

    Noun -> {nouns}
    Pronoun -> {pronouns}
    Det -> {determinants}
    Det -> Det AdjP
    Det -> Det Conj Det

    Conj -> {conjunctions}
    Verb -> {verbs}
    VerbTrans -> {verbs_trans}
    VerbIntrans -> {verbs_intrans}
    Prep -> {prepositions}
""")

print(grammar)

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
            error_word = find_error_word(tokens, parser)
            return {
                "is_valid": False,
                "error": f"Invalid structure near the word '{error_word}'."
            }
    except ValueError as e:
        return {"is_valid": False, "error": f"Grammar error: {str(e)}"}

def find_error_word(tokens, parser):
    last_successful_word = None  # Track the last successful token
    for i in range(len(tokens)):
        try:
            # Attempt parsing up to and including the i-th token
            partial_tokens = tokens[:i+1]
            list(parser.parse(partial_tokens))  # Try parsing the partial input
            last_successful_word = tokens[i]  # Update the last successful word if parsing succeeds
        except ValueError:
            break  # Stop at the first failure and report the last successful token's word
    # Return the word that caused the error, or None if everything succeeded
    return tokens[i] if i < len(tokens) else None

def tokenize_sentence(sentence):
    return sentence.lower().split()  # Simple tokenization for the GUI display

if __name__ == "__main__":
    # Example sentence input (after Morse code translation)
    sentence = input("Enter sentence: ").lower()  # Example: "the man saw the dog in the park"
    result = parse_sentence(sentence)
    if result["is_valid"]:
        print("Valid sentence:", sentence)
    else:
        print("Error:", result["error"])



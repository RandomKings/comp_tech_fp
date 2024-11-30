def load_words_from_file(file_path):
    word_dict = {
        'adjectives': [],
        'adverbs': [],
        'nouns': [],
        'pronouns': [],
        'determinants': [],  # These are usually fixed
        'conjunctions': [],  # These are usually fixed
        'verb_trans': [],  # These are usually fixed
        'verb_intrans': [],  # These are usually fixed
        'verbs': [],  # General verbs category
        'prepositions': []  # These are usually fixed
    }
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                word, pos = line.split('|')[:2]  # Get the word and part of speech
                pos_list = pos.split(', ')  # Handle multiple parts of speech

                # Add word to the appropriate lists in the dictionary
                if 'adjective' in pos_list:
                    word_dict['adjectives'].append(word)
                if 'adverb' in pos_list:
                    word_dict['adverbs'].append(word)
                if 'noun' in pos_list:
                    word_dict['nouns'].append(word)
                if 'pronoun' in pos_list:
                    word_dict['pronouns'].append(word)
                if 'indefinite article' in pos_list or 'definite article' in pos_list:
                    word_dict['determinants'].append(word)
                if 'conjunction' in pos_list:
                    word_dict['conjunctions'].append(word)
                if 'verb (used with object)' in pos_list:
                    word_dict['verb_trans'].append(word)
                    word_dict['verbs'].append(word)  # Add to general verbs
                if 'verb (used without object)' in pos_list:
                    word_dict['verb_intrans'].append(word)
                    word_dict['verbs'].append(word)  # Add to general verbs
                if 'verb' in pos_list:
                    word_dict['verbs'].append(word)  # Add general verbs explicitly
                if 'preposition' in pos_list:
                    word_dict['prepositions'].append(word)
                # Add more conditions for other parts of speech as needed
        print(word_dict['verbs'])
    return word_dict

# Load the words from the file
word_dict = load_words_from_file('comp_tech/final_prject/cleaned_file.txt')

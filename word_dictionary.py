def load_words_from_file(file_path):
    word_dict = {
        'nouns': [],
        'verbs': [],
        'adverbs': [],
        'adjectives': [],
        'determiners': ['the', 'a', 'an','his'],  # These are usually fixed
        'prepositions': ['in', 'with', 'on', 'under', 'by']  # These are usually fixed
    }
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                word, pos = line.split('|')[:2]  # Get the word and part of speech
                pos_list = pos.split(', ')  # Handle multiple parts of speech

                # Add word to the appropriate lists in the dictionary
                if 'noun' in pos_list:
                    word_dict['nouns'].append(word)
                if 'verb' in pos_list:
                    word_dict['verbs'].append(word)
                if 'adverb':
                    word_dict['adverbs'].append(word)
                if 'adjective':
                    word_dict['adverbs'].append(word)
                # Add more conditions for other parts of speech as needed
    return word_dict

# Load the words from the file
word_dict = load_words_from_file('comp_tech/final_prject/word.txt')




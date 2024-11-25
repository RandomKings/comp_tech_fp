# gui_app.py
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from morse_translater import text_to_morse
from grammar_parser import parse_sentence

def translate_and_display():
    # Get the sentence from the entry widget
    sentence = sentence_entry.get()
    
    # Parse the sentence
    parse_result = parse_sentence(sentence)
    
    if parse_result["is_valid"]:
        # Extract tokens for display in the GUI
        tokens = sentence.lower().split()  # Convert sentence to tokens for display
        
        # Print the parse tree in the console
        parse_tree = parse_result["tree"]
        print("Parse Tree:")
        parse_tree.pretty_print()  # Display parse tree in console for GUI usage
        
        # Translate to Morse code
        morse_code = text_to_morse(sentence)
        
        # Display tokens and Morse code in the GUI
        tokens_str = ', '.join(tokens)  # Format tokens as a comma-separated list
        result_text = f"Tokens:\n{tokens_str}\n\nMorse Code Translation:\n{morse_code}"
    else:
        # Display the error message in the GUI if the grammar is incorrect
        result_text = f"The sentence does not follow proper grammar.\nError: {parse_result['error']}"
    
    # Insert the result into the scrolled text widget
    result_text_widget.config(state=tk.NORMAL)
    result_text_widget.delete("1.0", tk.END)
    result_text_widget.insert(tk.END, result_text)
    result_text_widget.config(state=tk.DISABLED)

# Set up the GUI window
root = tk.Tk()
root.title("Morse Code Translator with Grammar Check")

# Input field for sentence
sentence_label = tk.Label(root, text="Enter a sentence:")
sentence_label.pack()

sentence_entry = tk.Entry(root, width=50)
sentence_entry.pack()

# Button to trigger translation
translate_button = tk.Button(root, text="Translate", command=translate_and_display)
translate_button.pack()

# Scrollable text widget for displaying results
result_text_widget = ScrolledText(root, wrap=tk.WORD, width=60, height=20, state=tk.DISABLED)
result_text_widget.pack()

# Run the GUI event loop
root.mainloop()

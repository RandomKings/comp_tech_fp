import tkinter as tk
from tkinter import messagebox
from morse_translater import text_to_morse
import grammar_parser  # For parse tree functions

# Initialize the main Tkinter window
root = tk.Tk()
root.title("English-to-Morse & Parse Tree GUI")
root.geometry("600x400")

# Function to handle Text to Morse Conversion
def convert_text_to_morse():
    text = entry_text.get("1.0", "end-1c")
    if text:
        morse_output = text_to_morse(text)
        output_text.delete("1.0", "end")
        output_text.insert("1.0", morse_output)
    else:
        messagebox.showwarning("Input Required", "Please enter text for Morse conversion")

# Function to parse the English text and visualize parse tree
def generate_parse_tree():
    sentence = entry_text.get("1.0", "end-1c")
    if sentence:
        try:
            parse_tree = grammar_parser.parse_sentence(sentence)
            output_text.delete("1.0", "end")
            output_text.insert("1.0", "Parse tree generated successfully in console.")
        except ValueError as e:
            messagebox.showerror("Parse Error", f"Grammar does not cover all words: {e}")
    else:
        messagebox.showwarning("Input Required", "Please enter English text before parsing")

# Input Text Field for English Text
entry_text = tk.Text(root, height=4, width=50)
entry_text.pack(pady=10)

# Output Text Field for Morse Code and Parse Tree notification
output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=10)

# Buttons
btn_text_to_morse = tk.Button(root, text="Convert Text to Morse", command=convert_text_to_morse)
btn_text_to_morse.pack(pady=5)

btn_parse = tk.Button(root, text="Generate Parse Tree", command=generate_parse_tree)
btn_parse.pack(pady=5)

# Run the main loop
root.mainloop()

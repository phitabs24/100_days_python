import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
# word = input("Enter a word: ").upper()
final = [nato_dict[char] for char in input("Enter a word: ").upper()]
print(final)


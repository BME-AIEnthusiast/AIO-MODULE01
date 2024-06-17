def count_chars(word):
    char_count = {}

    # Iterate through each character in the word
    for char in word:
        # Ignore spaces if any
        if char != ' ':
            # Convert character to lowercase
            char_lower = char.lower()
            # Update the count of the character
            if char_lower in char_count:
                char_count[char_lower] += 1
            else:
                char_count[char_lower] = 1

    return char_count


string1 = 'Happiness'
print(count_chars(string1))
string2 = 'smiles'
print(count_chars(string2))

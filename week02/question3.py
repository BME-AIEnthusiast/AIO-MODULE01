def word_count(file_path):
    word_counts = {}

    try:
        # Open the file and read
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Iterate through
        for line in lines:
            # Split the line into words based on whitespace
            words = line.split()
            # Iterate through each word
            for word in words:
                # Convert the word to lowercase
                word_lower = word.lower()

                # Update the count
                if word_lower in word_counts:
                    word_counts[word_lower] += 1
                else:
                    word_counts[word_lower] = 1

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

    return word_counts


# Example usage:
file_path = 'P1_data.txt'
print(word_count(file_path))

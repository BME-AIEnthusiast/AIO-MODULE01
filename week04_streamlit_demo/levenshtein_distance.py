import streamlit as st

def levenshtein_distance(word1, word2):
    # Initialize matrix of zeros
    rows = len(word1) + 1
    cols = len(word2) + 1
    distance_matrix = [[0 for x in range(cols)] for x in range(rows)]

    # Populate matrix with initial values
    for i in range(1, rows):
        distance_matrix[i][0] = i
    for j in range(1, cols):
        distance_matrix[0][j] = j

    # Iterate over the matrix to compute the cost of deletions, insertions, and substitutions
    for col in range(1, cols):
        for row in range(1, rows):
            if word1[row-1] == word2[col-1]:
                cost = 0
            else:
                cost = 1
            distance_matrix[row][col] = min(distance_matrix[row-1][col] + 1,      # Cost of deletions
                                            distance_matrix[row][col-1] + 1,      # Cost of insertions
                                            distance_matrix[row-1][col-1] + cost) # Cost of substitutions

    # The last cell of the matrix is the Levenshtein distance
    return distance_matrix[rows-1][cols-1]

# Sample vocabulary list
vocabs = ["apple", "orange", "banana", "grape", "pineapple"]

# Input word to correct
word = st.text_input("Enter a word:")

if word:
    leven_distances = dict()
    for vocab in vocabs:
        leven_distances[vocab] = levenshtein_distance(word, vocab)

    # Sort by distance
    sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
    correct_word = list(sorted_distances.keys())[0]
    
    st.write('Correct word: ', correct_word)

def levenshtein_distance(source, target):
    m = len(source)
    n = len(target)
    
    # Initialize matrix D
    D = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j
    
    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            del_cost = D[i-1][j] + 1
            ins_cost = D[i][j-1] + 1
            sub_cost = D[i-1][j-1] + (0 if source[i-1] == target[j-1] else 1)
            D[i][j] = min(del_cost, ins_cost, sub_cost)
    
    # The Levenshtein distance is the value in the bottom-right corner of the matrix
    return D[m][n]

# Example usage:
source = "kitten"
target = "sitting"
print(f"Levenshtein distance between '{source}' and '{target}' is: {levenshtein_distance(source, target)}")

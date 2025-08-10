def josephus(n, k):
    # Base case: when there is only one person, they are the survivor
    if n == 1:
        return 0  # Returning 0 for 0-based index

    # Recursive case: find the position of the survivor in the smaller circle
    return (josephus(n - 1, k) + k) % n

def find_survivor(n, k):
    # The result from josephus is 0-based, so we convert it to 1-based
    return josephus(n, k) + 1

# Example usage
n1, k1 = 3, 2
print(f"Survivor position for n={n1}, k={k1}: {find_survivor(n1, k1)}")  # Output: 3

n2, k2 = 5, 3
print(f"Survivor position for n={n2}, k={k2}: {find_survivor(n2, k2)}")  # Output: 4

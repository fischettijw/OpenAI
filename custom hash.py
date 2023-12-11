import os; os.system("cls")


def custom_hash(input_string):
    prime = 31  # You can choose any prime number
    result = 0

    for char in input_string:
        result = (result * prime + ord(char)) % (2**32)  # Modulo to ensure a 32-bit hash

    return result

# Example usage:
input_data = "hello my nmae is joe"
hashed_value = custom_hash(input_data)
print(f"The custom hash value of '{input_data}' is: {hashed_value}")

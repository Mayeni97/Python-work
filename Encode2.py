import math
import numpy as np
from numpy.linalg import inv


def text_to_ascii_matrix(message):
    # Convert the text string into ASCII
    message_ascii = list(message.encode("ascii"))

    # Determine the value of n
    n = math.ceil(len(message_ascii) / 2)

    # Divide the string into two equal parts of length n
    row1 = message_ascii[:n]
    row2 = message_ascii[n:]

    # Add padding to ensure both rows have the same length
    if len(row1) < len(row2):
        row1.extend([0] * (len(row2) - len(row1)))
    else:
        row2.extend([0] * (len(row1) - len(row2)))

    # Create a 2xn matrix
    matrix = np.array([row1, row2])

    return matrix


def matrix_set_up(rows, columns, matrix):
    try:
        entries = list(map(int, matrix.split()))
        if len(entries) != rows * columns:
            raise ValueError
        matrix = np.array(entries).reshape(rows, columns)
    except ValueError:
        print(
            "Invalid matrix input. Please enter a matrix with the correct number of rows and columns."
        )
        return None

    return matrix


def multiply_matrix_and_message(matrix, text_matrix):
    result = np.dot(matrix, text_matrix)

    return result


def encrypt_message(message, matrix):
    text_matrix = text_to_ascii_matrix(message)
    result = multiply_matrix_and_message(matrix, text_matrix)

    # Format the output as a string of integers separated by spaces
    encrypted_message = " ".join([str(int(val)) for val in np.nditer(result)])

    return encrypted_message


def decrypt_message(encrypted_message, matrix):
    try:
        entries = list(map(int, encrypted_message.split()))
        if len(entries) != matrix.shape[0] * 2:
            raise ValueError
        text_matrix = np.array(entries).reshape(2, matrix.shape[0])
        matrix_inv = inv(matrix)
        result = multiply_matrix_and_message(matrix_inv, text_matrix)

        # Convert the result back to a string
        decrypted_message = ''.join([chr(int(val)) for val in np.nditer(result)])
    except ValueError:
        print("Invalid encrypted message input. Please enter a valid encrypted message.")
        return None

    return decrypted_message




def main():
    # Get user input for the message, matrix size, and matrix values
    message = input("What is your message?: ")
    rows = int(input("Enter the number of rows for the matrix: "))
    columns = int(input("Enter the number of columns for the matrix: "))
    matrix_input = input("Enter the matrix values (separated by spaces): ")

    # Set up the matrix
    matrix = matrix_set_up(rows, columns, matrix_input)
    if matrix is None:
        return

    # Encrypt the message
    encrypted_message = encrypt_message(message, matrix)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message
    decrypt_answer = input("Do you want to decrypt the message? Enter yes or no: ")
    if decrypt_answer.lower() == 'yes':
        decrypted_message = decrypt_message(encrypted_message, matrix)
    if decrypted_message is not None:
        print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()

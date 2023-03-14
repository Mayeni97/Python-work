import math
import numpy as np

def text_to_ascii_matrix(message):
    # Convert the text string into ASCII
    message = (list(message.encode('ascii')))
    

    # Calculate the length of the string
    length = len(message)

    # Determine the value of n
    n = math.ceil(length/2)

    # Divide the string into two equal parts of length n
    row1 = message[:n]
    row2 = message[n:]

    # Create a 2xn matrix
    matrix = [list(row1), list(row2)]

    return matrix

def matrix_set_up(rows, columns, matrix):
    entries = list(map(int, matrix.split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix

def Multipling_Matrix_and_Message(text_to_ascii_matrix, matrix):
    result = np.dot(text_to_ascii_matrix, matrix)

    return result
    


def main():
    while True:
        message = input("What is your message?:")
        rows = int(input("Enter the number of rows for the matrix:"))
        columns = int(input("Enter the number of columns matrix:"))
        matrix = (input("Enter the matrix in a single line (separated by space): "))
        print("Is '"+ message + "' what you want to sent out?: ")
        answer = input("Enter yes or no: ")
        if answer == "yes":
            print(text_to_ascii_matrix(message))
            print(matrix_set_up(rows,columns,matrix))
            Complete = Multipling_Matrix_and_Message(text_to_ascii_matrix, matrix)
            print(Complete)
        elif answer == "no":
            print("What is the message?")
        else:
            print("Please enter yes or no")
        
main()

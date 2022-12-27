"""
We have placeholders = (rows * 2) - 1
In every row, we are reducing the number of spaces




    *

   * *

  * * *

 * * * *

* * * * *
"""


# define the number of rows in the triangle
rows = 5

# outer loop to handle the number of rows
for i in range(0, rows):
    # inner loop to handle number of spaces
    # values changing acc. to requirement
    for j in range(0, rows - i - 1):
        print(" ", end="")
    # inner loop to handle number of stars
    for j in range(0, i + 1):
        # printing stars
        print("* ", end="")
    # ending line after each row
    print("\n")

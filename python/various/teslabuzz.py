"""

TESLABUZZ
   Write a function that takes in an integer N, then iterates from 1 to N with the following rules:
       Print out on a new line the line number and a colon (IE, 5: )
       If i is a multiple of 3, print out 3
       If i is a multiple of 5, print out S
       If I is a multiple of 7, print out X

   EX:
       1:
       2:
       3: 3
       4:
       5: S
       ...
       15: 3S
"""


def my_iterator(n):
    i = 1
    while i <= n:
        string = ""
        if i % 3 == 0:
            string += str(3)
        if i % 5 == 0:
            string += "S"
        if i % 7 == 0:
            string += "X"
        print("{}: {}".format(i, string))
        i += 1
    return


my_iterator(105)

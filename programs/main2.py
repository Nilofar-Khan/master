from program1 import prog1
from program2 import prog2
from program3 import prog3
import os

def main():
    # Define the input file path
    input_file = os.path.join("inputs", "input.txt")

    # Read inputs from the file
    with open(input_file, "r") as file:
        lines = file.readlines()

    # process inputs for program1,program2 and program3
    name1 = lines[0].strip()  # First line for prog1
    name2 = lines[1].strip()  # Second line for prog2
    name3 = lines[2].strip()  # third line for prog3

    # Initialize and run programs
    obj1 = prog1(name1)
    obj2 = prog2(name2)
    obj3 = prog3(name3)

    obj1.func()
    obj2.func()
    obj3.func()

if __name__ == "__main__":
    main()

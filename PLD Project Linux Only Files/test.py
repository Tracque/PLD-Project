import sympy as sym
import re

with open("Square.dat", 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Check if the file is not empty
            if not lines:
                print(f"File {file_path} is empty.")

            # Get the last line
            last_line = lines[-1]

            # Use regular expression to extract codim and face values
            match = re.search(r'codim: (\d+), face: (\d+)/(\d+)', last_line)

            if match:
                codim = int(match.group(1))
                face = int(match.group(2))

                if face == int(match.group(3)):
                    codim -= 1
                    face = 0
               

print(codim)
print(face)
print(match.group(3))
#! /usr/bin/env python3.7

file_name = input("What is the name of file which you want to create?")
print("Write the contents now, end it with empty line...")
with open(file_name, 'w') as f:
    eof = False
    lines = []

    while not eof:
        line = input()
        if line.strip():
            lines.append(f"{line}\n")
        else:
            eof = True
    f.writelines(lines)
    print("Done!")


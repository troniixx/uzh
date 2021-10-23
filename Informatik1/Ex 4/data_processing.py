#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    #file_original = open(path_reading,'r')

    if not os.path.exists(path_reading):
        return False

    else:
        if os.path.exists(path_reading) =="":
            file_processed = open(path_writing, 'w')
            file_processed = file_processed.close()
            return file_original
        else:
            file_original = open(path_reading,'r')
            file_processed = open(path_writing,'w')

            with open(path_reading) as file:
                lines = file.readlines()
                lines = [line.rstrip() for line in lines]

                for i in range(len(lines)):
                    if i == 0:
                        if (len(lines)) > 1:
                            file_processed.write("Firstname,Lastname\n")
                        else:
                            file_processed.write("Firstname,Lastname")
                    else:
                        if ";" in lines[i]:
                            split = lines[i].split()
                            x = split[0][:-1]
                            y = ","
                            z = split[1]
                            del split[0:]
                            split.append(z)
                            split.append(y)
                            split.append(x)

                            if i !=max(range(len(lines))):
                                file_processed.write(f'{"".join(split)}\n')
                            else:
                                file_processed.write(f'{"".join(split)}')
                        elif '' in lines[i] and len(lines[i]) > 1:
                            split = lines[i].split()
                            x = split[1]
                            y = ","
                            del split[1]
                            split.append(y), split.append(x)

                            if i != max(range(len(lines))):
                                file_processed.write(f'{"".join(split)}\n')
                            else:
                                file_processed.write(f'{"".join(split)}')
                        else:
                            if i != max(range(len(lines))):
                                file_processed.write(",\n")
                            else:
                                file_processed.write(",")

                file_processed.close()
                file_original.close()
            return file_processed


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "public/my_data.txt"  # case:testimp:path
OUTPUT_PATH = "public/my_data_processed.txt"  # case:testimp:path
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")


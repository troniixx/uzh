from sys import argv

def process(input_file):
    sol = {}

    with open(input_file, "r") as df:
        for line in df:
            clean_line = line.strip()
            parts = clean_line.split()
            key = parts[0]
            value = parts[1]
            if value not in sol:

                sol[value] = []
                sol[value].append(key)
            else:
                sol[value].append(key)

    return sol

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python gen_code.py <input_file>")
        exit(1)

    IN = argv[1]
    print(process(IN))
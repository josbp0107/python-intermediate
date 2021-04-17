def read():
    numbers = []
    with open("files_examples/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)

def write():
    names = ["José", "David", "Miguel", "Carlos"]
    with open("files_examples/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    read()
    write()


if __name__ == '__main__':
    run()
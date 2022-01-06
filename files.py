def read():
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        numbers = [int(line) for line in f]
    print("numbers", numbers)

def write():
    names = ["hellen", "caro", "luce", "maría"]
    with open("./files/names.txt", "w", encoding="utf-8") as s:
        for name in names:
            s.write(f"{name}\n")

def append():
    names = ["yore"]
    with open("./files/names.txt", "a", encoding="utf-8") as s:
        for name in names:
            s.write(f"{name}\n")

def run():
    write()
    append()

if __name__ == '__main__':
    run()
def write_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
    except:
        return "Error writing to the file!"


def append_file(filename, content):
    try:
        with open(filename, "a") as file:
            file.write(content)
    except:
        return "Error appending to the file!"


def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except:
        return "Error reading the file!"


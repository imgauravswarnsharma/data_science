# module.py
def extract_first_name(full_name):
    # Splits the full name with whitespace as the delimiter
    name = full_name.split(" ")

    # Returns the first element i.e. the first name
    return name[1][0] + ". " + name[0]

# This segment is executed only if the script is ran explicitly
if __name__ == "__main__":
    print("---Running Module Test---")
    name = extract_first_name("John Hancock")
    print(name)
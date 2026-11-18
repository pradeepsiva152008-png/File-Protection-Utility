# Simple educational file protection using XOR.
# This is NOT secure encryption. Do not use it for sensitive files.

def transform_file(source, destination, password):
    if not password:
        print("Password cannot be empty.")
        return

    key = password.encode("utf-8")
    with open(source, "rb") as file:
        data = file.read()

    protected = bytes(value ^ key[i % len(key)] for i, value in enumerate(data))

    with open(destination, "wb") as file:
        file.write(protected)

    print("File converted successfully:", destination)


print("1. Protect a file")
print("2. Restore a file")
choice = input("Choose an option: ")

source = input("Enter input file path: ")
destination = input("Enter output file path: ")
password = input("Enter password: ")

if choice in ("1", "2"):
    transform_file(source, destination, password)
else:
    print("Invalid option.")

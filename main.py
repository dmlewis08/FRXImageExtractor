import io
import os
import PIL.Image as Image

header_length = 14
size_length = 4


def get_image_size(fileContents: str, offSet: int = 0):
    start = offSet + header_length
    strSize = fileContents[start:start+4]
    return int.from_bytes(strSize[::-1], 'big')


def get_image_contents(fileContents: str, offSet: int = 0):
    size = get_image_size(fileContents, offSet)
    start = offSet + 12
    end = start + size
    return fileContents[start:end]


def get_file_name() -> str:
    goOn = True
    while goOn:
        fPath = input("File path: ")
        if not fPath or not os.path.isfile(fPath):
            print("Invalid or empty file name.")
            resp = input("Try again? (Y or N)")
            goOn = resp.upper().startswith("Y")
        else:
            return fPath
        if not goOn:
            quit(-1)


def get_offset() -> int:
    goOn = True
    while goOn:
        offSet = input("Offset (as hexadecimal): ")
        if offSet:  # and offSet.isnumeric():
            try:
                offSet = int(offSet, 0)  # Expects hex
                return offSet
            except:
                print("Invalid offset (must be an integer).")
                resp = input("Try again? (Y or N)")
                goOn = resp.upper().startswith("Y")
        else:
            print("Invalid or missing offset (must be an integer in hex).")
            resp = input("Try again? (Y or N)")
            goOn = resp.upper().startswith("Y")
        if not goOn:
            quit(-1)


if __name__ == '__main__':
    file_path = get_file_name()

    with open(file_path, "rb") as file:
        fileContent = file.read()

    keepGoing = True
    while keepGoing:
        offset = get_offset()
        image_size = get_image_size(fileContent, offset)

        image_content = get_image_contents(fileContent, offset)
        io_bytes = io.BytesIO(image_content)
        opened_image = Image.open(io_bytes)
        opened_image.show()
        # opened_image.save("image.bmp")  # Uncomment this to save the file

        keepGoing = input("Get another image from the same file? (Y or N) ").upper().startswith("Y")
        if not keepGoing:
            quit()

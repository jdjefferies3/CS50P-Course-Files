import sys
from PIL import Image

def shirt(file_one, file_two):
    # Check if extension is JPEG or PNG
    file_one_ext = file_one.split(".")[1]
    file_two_ext = file_two.split(".")[1]
    if file_one_ext != "jpg" and file_one_ext != "jpeg" and file_one_ext != "png":
        sys.exit("Invalid input")
    if file_two_ext != "jpg" and file_two_ext != "jpeg" and file_two_ext != "png":
        sys.exit("Invalid output")
    if file_one_ext != file_two_ext:
        sys.exit("Input and output have different extensions")

    background = Image.open(file_one)
    overlay = Image.open("shirt.png")
    background = ImageOps.fit(background, size = overlay.size)
    background.paste(overlay, (0,0), overlay)
    background.save(file_two)

def main():
    try:
        if len(sys.argv) == 1 or len(sys.argv) == 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        else:
            shirt(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()

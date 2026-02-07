import os
import sys
import re
import shutil
from PIL import Image
from PIL import UnidentifiedImageError


current_images = []
current_images_wout_ext = []
new_images = []


# Gets list of all images both new ones and already cleaned up ones and cleans up the lists
def get_dir(path: str):
    global new_images
    global current_images
    global current_images_wout_ext
    new_images = os.listdir(path)
    current_files = os.listdir("./")

    # Cleans up list of current images to only include pictures
    for file in current_files:
        file = str(file)
        regex = re.compile(".*.png")
        if re.match(regex, file):
            current_images.append(file)

    # Makes another list with only file names for later number comparing purposes
    for image in current_images:
        image = str(image)
        name = image.split(".")[0]
        current_images_wout_ext.append(name)


# Function that converts any image file into PNG. Need to insert path (Should be like ./ANYTHING/) and filename as argument.
def convert(path: str, filename: str):
    name = filename.split(".")[0]
    regex = re.compile(".*.png")
    if re.match(regex, filename):
        return ""
    else:
        try:
            image = Image.open(path + filename)
            image.save(path + name + ".png")
            os.remove(path + filename)
        except UnidentifiedImageError:
            return ""


# Function that renames every file in new downloads folder with respect to main folder. Arguments are the list of newly downloaded list (Files to be renames) and location to the files (Should be like ./ANYTHING/).
def rename(path: str, new_list: list):
    numbers = []

    # Grab highest number in names from main folder
    for name in current_images_wout_ext:
        numbers.append(int(name))
    try:
        highest = max(numbers)
    except ValueError:
        highest = 0
    highest += 1

    # Change names
    for file in new_list:
        # Ignores files that arent PNGs
        regex = re.compile(".*.png")
        if not re.match(regex, file):
            continue

        filename_list = file.split(".")
        os.rename(
            path + filename_list[0] + "." + filename_list[1],
            path + str(highest) + "." + filename_list[1],
        )
        highest += 1


# Function that grabs every file in specified folder and moves it to main directory
def move(path: str):
    files = os.listdir(path)

    for file in files:
        # Ignore files that aren't properly converted into PNG
        regex = re.compile(".*.png")
        if not re.match(regex, file):
            continue

        shutil.move(path + file, "./" + file)


# Main function that starts when the program is launched, checks for config arguments, ensures necesary folder exist, converts and moves every file.
def main():

    # Checks if user wants to change path of newly downloaded images or not and set new or default path
    try:
        argument = sys.argv[1]
    except IndexError:
        argument = ""

    if argument == "config":
        path = input(
            "Insert path with newly downloaded images (Formatting is './PATH_TO_FOLDER/')"
        )
    elif argument == "":
        path = "./new/"

    get_dir(path)

    # Checks if path exists and creates it if needed
    if not os.path.isdir(path):
        os.makedirs(path)

    # Converts all images into png
    for file in new_images:
        convert(path, file)

    new_images2 = os.listdir(path)
    rename(path, new_images2)
    move(path)


if __name__ == "__main__":
    main()

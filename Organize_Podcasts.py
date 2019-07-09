import os
import shutil
# Here, we import the os and shutil modules to allow python to make changes to
# and move files on the computer.


def make_Hardcore_History_Folder():
    # This function creates the folder 'Hardcore History'
    folders = os.listdir()
    os.mkdir("Hardcore History")
    for folder in folders:
        os.rename(folder, os.path.join("Hardcore History", folder))


def extract_type(filename):
    # This function finds the type of podcast a file is.
    return filename.split(".")[2]


def extract_series_name(filename):
    # This function finds the series name if the file is in a series.
    first_split = filename.split(".")[1]
    series_name = first_split.split("-")[0]
    return series_name


def make_type_directories(types):
    # This function makes folders based on the type of file.
    for kind in types:
        os.mkdir(kind)


def make_series_directories(series_name):
    # This function makes folders based on the series name.
    for name in series_name:
        os.mkdir(name)


def organize_podcasts(Directory):
    # This function moves to the directory to be organized.
    # Then organizes the files based on type
    os.chdir(Directory)

    episodes = os.listdir()

    # This creates a list to hold the types.
    types = []

    for episode in episodes:
        # This loops through the files and extracts the type.
        kind = extract_type(episode)
        if kind not in types:
            types.append(kind)
    make_type_directories(types)
    for episode in episodes:
        # This loops through the types and creates folders for them.
        kind = extract_type(episode)
        os.rename(episode, os.path.join(kind, episode))


def sort_series(Directory):
    # This function moves to directory to sort by series.
    os.chdir(Directory)
    series = os.listdir()
    # This creates a list to hold the series names.
    series_name = []

    for episode in series:
        # This loops through the episodes and extracts the series name.
        name = extract_series_name(episode)
        if name not in series_name:
            series_name.append(name)
    make_series_directories(series_name)
    for episode in series:
        # This loops through the series names and creates folders for them.
        name = extract_series_name(episode)
        os.rename(episode, os.path.join(name, episode))


def move():
    # This moves the created folders to the 'E:', if you don't have two drives
    # this can be omitted.
    shutil.move(
            "C:\\Users\\zakk and chey\\Downloads\\Hardcore History", "E:\\"
                    )


# This runs the functions.

organize_podcasts("C:\\Users\\zakk and chey\\Downloads")
make_Hardcore_History_Folder()
sort_series("C:\\Users\\zakk and chey\\Downloads\\Hardcore History\\series")
move()

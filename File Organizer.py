import os, shutil

folder = input("Enter the folder you want to sort: ") # User inputs a folder

# Checks if folder exists and if not, terminates the program
if not os.path.exists(folder):
    print(folder, "does not exist.")
    exit()

# Different types of folder and their extensions
documents = [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".doc"]
pictures = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"]
videos = [".mp4", ".mkv", ".avi", ".mov", ".wmv"]
audio = [".mp3", ".wav", ".flac", ".aac", ".ogg"]
programs = [".py", ".java", ".cpp", ".js", ".html", ".css"]
applications = [".exe", ".msi"]

folder_types = ["Documents", "Pictures", "Videos", "Audio", "Programs", "Applications"] # All the folder names in a single array

for folder_type in folder_types: # Making each of the new folders (empty)
    os.makedirs(os.path.join(folder, folder_type), exist_ok=True)

# Mapping all the folder names to their extensions
sort_mapping = {
    "Documents": documents,
    "Pictures": pictures,
    "Videos": videos,
    "Audio": audio,
    "Programs": programs,
    "Applications": applications
}

subdirectories = os.listdir(folder) # Making a list that stores every directory

for subdirectory in subdirectories:
    file = os.path.join(folder, subdirectory) # Assigning the file to the variable file

    if os.path.isfile(file): # Only sorting if the file is a file (not a folder)
        name, extension = os.path.splitext(file) # Splitting the name and extension of the file
        extension = extension.lower() # Making the extension lowercase

        found = False # Reseting found as false

        for category, ext in sort_mapping.items(): # Looping through every category in sort_mapping
            if extension in ext: # Moving file if extension is found
                found = True
                print(subdirectory, "moved to:", category)
                shutil.move(file, os.path.join(folder, category))
                break
            
        if not found: # Moving file to Others if extension not found
            os.makedirs(os.path.join(folder, "Others"), exist_ok=True)
            shutil.move(file, os.path.join(folder, "Others"))
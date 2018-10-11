import os

# Have user set the title of the gallery, where the final gallery should be outputted, and the current location of photos
pageTitle = input("What is the title of this gallery? ")
outputFolder = input("What directory should the file be created in? ")
photoLocation = input("Where are the photos located?")

outputLocation = outputFolder + "/" + pageTitle + "-gallery.html"

# If file exists, delete it
if os.path.exists(outputLocation):
    os.remove(outputLocation)

# If the output folder does not exist, create it
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

# Create the new output
outputHTML = open(outputLocation, "w+")



# Iterate through each file in directory
for filename in os.listdir(photoLocation):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(filename)



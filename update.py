"""This script maps the folders in data folder to a JSON file"""
import json
import platform
import os

# This is the final dictionary that will be written to a json files
data = {}
data["repo"] = {}

# All the items for which an object will be created in data.json
cards = []


print("This is python version {}".format(platform.python_version()))
print("current working directory is {}".format(os.getcwd()))
print(" ")

# Getting to the list of all the folders in the current directory.
# This should be the data folder
path = os.getcwd()
dataPath = path + "\data"
cards = os.listdir(dataPath)

# Creating a list of paths for all the folders in the data folder
folderpath = []
for item in cards:
    folderpath.append("data\\" + item)


for item in folderpath:
    files = (os.listdir(item))
    for file in files:
        if file == "input.json":
            path = item + "\\" + file
            r = open(path, "r")
            if r.mode == "r":
                contents = json.load(r)
                for value in contents.values():
                    data["repo"][contents.keys()[0]] = value
            r.close()
        else:
            pass


with open("data.json", "w") as outfile:
    json.dump(data, outfile)

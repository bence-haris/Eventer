import os
import wget
import requests
from PIL import Image
import PIL

lines = []
sor = []
firms = input("PATH TO COMPANY NAMES: ")
ids = input("PATH TO ID LIST: ")
with open(firms) as f:
    lines = f.readlines()
with open(ids) as r:
    sor = r.readlines()
i = 0

##############################################################################
#                   Put " " on the end of txt-s                              #
##############################################################################
while lines[i] != " ":
    darab = lines[i].split("\n")
    to = "https://www.google.com/search?q="+darab[0]+"+logo+400x400+twitter&tbm=isch"
    #Get request to the URL with the company name
    r = requests.get(to)
    link = r.text.split("src=\"")
    if "\"" in link[2]:
        path = link[2].split("\"")
        path_string = path[0]+".png"
        print(path[0])
        r = wget.download(path_string)
    else:
        print("NO IMAGE COULD BE DOWNLOADED")
    azon = sor[i].split("\n")
    full_name = azon[0] + ".png"
    os.rename("./images", "./" + full_name)
    kep = Image.open("./" + full_name)
    kep = kep.resize((400, 400), PIL.Image.NEAREST)
    kep.save(full_name)
    i = i + 1

ch = input("Want to rename IDs? (y/n)")
with open(ids, "r") as f:
    sor = f.read().splitlines()
if ch == "y":
    print("Renaming ID list")
    with open(ids, "w") as f:
        for line in sor:
            if line != " ":
                print(line + ".png", file=f)
    print("DONE")
else:
    print("IDs not renamed")

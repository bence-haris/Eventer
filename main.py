import os
import wget
import requests
from PIL import Image
import PIL

lines = []
sor = []
with open("firms.txt") as f:
    lines = f.readlines()
with open("./ids.txt") as olvas:
    sor = olvas.readlines()
i = 0

##############################################################################
#                   Put " " on the end of txt-s                              #
##############################################################################
while lines[i] != " ":
    darab = lines[i].split("\n")
    to = "https://www.google.com/search?q="+darab[0]+"+logo+400x400+twitter&tbm=isch"
    #Get request to the URL with the company name
    r = requests.get(to)
    if "src" in r.text:
        #Ha a keresesben van "forras":
        link = r.text.split("src=\"")
        if "\"" in link[2]:
            path = link[2].split("\"")
            path_string = path[0]+".png"
            print(path[0])
            r = wget.download(path_string)
    else:
        print("Error")

    azon = sor[i].split("\n")
    full_name = azon[0] + ".png"
    os.rename("./images", "./" + full_name)
    kep = Image.open("./" + full_name)
    print(kep.height)
    kep = kep.resize((400, 400), PIL.Image.NEAREST)
    kep.save(full_name)
    i = i + 1

import glob

directory = "/pfad/zum/ordner"
repalce = ["../", "/"]

def replacestring(string):
    for i in range(repalce):
        index = string.find(repalce[i*2])
        teile = string.split(repalce[i*2+1])
        for j in range(teile):
            

for filename in glob.glob(directory + "/*"):
    with open(filename, "r+") as file:
        

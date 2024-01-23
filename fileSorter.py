import os, shutil

path = 'F:/Downloads/'

file_name = os.listdir(path)


bilder = [".jpeg",".png",".jpg",".gif"] 
dokumente = [".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf"] 
videos = [".mp4",".mkv"] 
sounds = [".mp3",".wav",".m4a"] 
apps = [".exe",".lnk", ".iso"] 
rsbs = [".asm",".circ"]

folder = ["Bilder", "Dokumente", "Videos", "Sounds", "Apps", "RSBS"]

for i in range(0,6):
    if not os.path.exists(path + folder[i]):
        os.makedirs(path + folder[i])

for file in file_name:
    dest = ""
    for end in bilder:
        if file.endswith(end):
            dest='Bilder/'
            shutil.move(path + file,path + dest)
            break

for file in file_name:
    dest = ""
    for end in dokumente:
        if file.endswith(end):
            dest='Dokumente'
            shutil.move(path + file,path + dest)
            break

for file in file_name:
    dest = ""
    for end in videos:
        if file.endswith(end):
            dest='Videos'
            shutil.move(path + file,path + dest)
            break

for file in file_name:
    dest = ""
    for end in sounds:
        if file.endswith(end):
            dest='Sounds'
            shutil.move(path + file,path + dest)
            break

for file in file_name:
    dest = ""
    for end in apps:
        if file.endswith(end):
            dest='Apps'
            shutil.move(path + file,path + dest)
            break
for file in file_name:
    dest = ""
    for end in rsbs:
        if file.endswith(end):
            dest='RSBS/'
            shutil.move(path + file,path + dest)
            break
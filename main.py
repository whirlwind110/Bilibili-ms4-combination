import os, json, sys

path = sys.argv[1]
print(path)
dirs = os.listdir(path)
for d in dirs:
    with open(path + "\\" + d + "\\entry.json", encoding="utf8") as entry:
        name = json.load(entry)['page_data']['part']
    audio = path + "\\" + d + "\\64\\audio.m4s"
    video = path + "\\" + d + "\\64\\video.m4s"
    os.system('ffmpeg -i ' + audio + ' -i ' + video + ' -c copy "' + name + '.mp4"')

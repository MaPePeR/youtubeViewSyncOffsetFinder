import pafy
import os.path

videos = []
with open("urls.txt", "r") as h:
        for url in h:
                url = url.strip()
                videos.append(pafy.new(url))

apaths = []
ids = []
for i,v in enumerate(videos):
        print("{v.duration} {v.author:<10.10} {v.title}".format(v=v))
        audios = sorted(v.audiostreams, key=lambda a: a.get_filesize())
        a = audios[0]
        fname = "audiostream-%s.%s" % (v.videoid, a.extension)
        if not os.path.isfile(fname):
                apath = a.download(fname)
                print("")
        else:
                apath = os.path.abspath(fname)
                print("skipping download")
        apaths.append(apath)
        ids.append(v.videoid)

print("Searching offsets...")

#Use audio_offset_finder from local submodule
import sys
sys.path.append(os.path.join('.','audio-offset-finder'))

import numpy as np
from audio_offset_finder import find_offset
files = apaths

score = np.zeros((len(files), len(files)))
offset = np.zeros((len(files), len(files)))

for i, file1 in enumerate(files):
        for j, file2 in enumerate(files):
                if i == j:
                        continue
                offset[i,j], score[i,j] = find_offset(file1, file2, trim=60, skipFile2=10)

print("Scores:")
print(score)
print("Mean-Scores:")
print(score.mean(1))
print("Offsets:")
print(offset)

for i in range(len(files)):
        print("Option %d: (Mean Score: %f)" % (i, score.mean(1)[i]))
        s = "http://viewsync.net/watch?"
        for j in range(len(files)):
                videoOffset = offset.max(1)[i] - offset[i,j]
                print("https://www.youtube.com/watch?v={} Start at {} ({})".format(ids[j], offset[i,j], videoOffset))
                s += "v={}&t={}&".format(ids[j], videoOffset)
        print(s[:-1])

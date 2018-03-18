from vidpy import Clip, Composition

clips = []

for i in range(0,4):
    clip = Clip('videos/output.mp4', offset = i*0.07)
    clip.chroma(color='#000000')
    clips.append(clip)

comp = Composition(clips, bgcolor="red")
comp.preview()
# comp.save('videos/coolzucks.mp4')

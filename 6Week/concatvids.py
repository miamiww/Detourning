from vidpy import Clip, Composition



clip1 = Clip("videos/output.mp4", start=1, end=5)
clip2 = Clip("videos/zuck.mp4", start=0, end=6)

# clip1.fadein(1)
# clip2.fadeout(1)

# clip1.chroma(color='#000000')

clips = [clip1, clip2]

comp = Composition(clips, singletrack=True)
comp.preview()

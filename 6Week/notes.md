## Videos and stuff

### Youtube DL command line tool
* youtube-dl "url" -F ; gets all file types available to download
* youtube-dl -f # "url" -g ; gets secret url
* youtube will have subtitle files, search ",cc"
* can use subtitles for making automatic supercuts
* can check subscene.com for srt files
* vtt, srt, and self transcribed video texts

### videogrep command line tool
* good for making supercuts or transctriptions
* videogrep --input time.mp4  --search "time" --use-vtt --padding 0
* videogrep --input time.mp4 --transcribe


### ffmpeg command line tool
* https://www.ffmpeg.org/
* very powerful video editing tool
* transfer to gif or extract audio very easily
* ffmpeg -i supercut.mp4 -r 3 supercut.gif
* speed videos up
* resize videos
* use -vf for video effects
* edge detection ; ffmpeg -i zuck.mp4 -vf "edgedetect=low=0.1:high=0.4" output.mp4

### moviepy and vidpy
* python libraries for video stuff

Youtube [ViewSync](http://viewsync.net) Offset Finder
=====================================================

Provide a text file with YouTube URLs. The Script will then download the lowest quality audiostream using [pafy](https://github.com/mps-youtube/pafy) and then use a modified version of [bbcrd/audio-offset-finder](https://github.com/bbcrd/audio-offset-finder) to find the Audio Offset in the Audio Streams. 

If you provide `N` URLs it will generate `N` results by trying to find all offset of the all the other audio streams in a single one. It will print a Matrix of Offsets and Scores and each option will have a mean score calculated.

Requirements:

* `numpy`
* `pafy`
* `scikits.talkbox` (Apparently only works with Python 2)

You should be able to install all of these with `pip` - Windows might need some extra work to get it installed.

Also requires an installed `ffmpeg`!
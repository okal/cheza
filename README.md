## Cheza

Cheza is a commandline MP3 player written as part of a presentation for the
Nairobi Python User Group. It is intended, partly, as a survey of the Python
landscape as it pertains to media support, and perhaps more ambitiously, to
open the minds of new Python programmers to the possibilities available to
them, beyond web development frameworks and throwaway utility scripts.

### Features

It's feature set, if it's even worthy of that lofty title, consists entirely of:

* Displaying the metadata contained in an MP3 file in pretty colours :-)
* Playing the MP3 file
* Pausing playback when the space bar is pressed TODO
* Resuming playback when the space bar is pressed TODO
* Exiting gracefully with Ctrl-C

### Dependencies

* The Pygame library for game development
* The mutagen library for reading media file metadata
* The amazing clint library for nicer text interfaces
* The pydub library for audio file manipulation

### License

I'm compelled to release this under GPL v2, because of the mutagen dependency.
Feel free to use and abuse it under the terms of the WTFPL if you can yank it
out. I hadn't the time.

# AudioRec - A Python package

AudioRec is the most simple audio recorder for python. Record any sound from your standard recording device to WAV or MP3. Simply hit start, stop and save - done.

- Record sound from the standard input device
- Recording happens in another thread - stop the recording on command
- Save the sound as a wav
- Quickly convert it to MP3

# How to get it
To download AudioRec, you simply use pip:
```sh
pip install AudioRec
```

Or you clone [this](https://github.com/joelbarmettlerUZH/AudioRec) respository and add all the files contained in the *AudioRec* folder into your project folder.

# Usage

AudioRec is deadly simple. First, import the package and create a recorder instance.

```python
from AudioRec import Recorder

rec = Recorder()
```
## Start / Stopping a recording

To start a new recording, simply hit rec.start()

```python
rec.start()
```

Your recording starts in another thread, so you are free to continue with your main program. In the most simple case, just wait for X seconds before you stop the recording.

```python
time.sleep(5)   # Waits for 5 seconds
```
Then call the recording to stop.

```python
rec.stop()
```

## Save the recording and convert it to MP3

To save the recorded audio, specify a filename and call *save*.

```python
rec.save("test.wav")
```

Now that your file is saved, convert it to MP3 and delete the old file.

```python
Recorder.wavTomp3("test.wav")
Recorder.delete("test.wav")
```

# Coplete example
```python
rec = Recorder()
print("Start recording")
rec.start()
time.sleep(5)
print("Stop recording")
rec.stop()
print("Saving")
rec.save("test.wav")
print("Converting wav to mp3")
Recorder.wavTomp3("test.wav")
print("deleting wav")
Recorder.delete("test.wav")
```

# Optinal parameters
When you initialize a recorder, you can define the chunk-size, the channels (2 for stereo) and the bitrate (44100 Hz standard).

```python
rec = Recorder(chunk=1024, channels=2, rate=44100)
```

License
----

IMPORTANT: The file "ffmpeg.exe" is excluded from the MIT license and fall under the GNU2 License. Download the original [here](https://www.ffmpeg.org/)

MIT License

Copyright (c) 2018 Joel Barmettler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


By the way, I am an [AI Engineer from Zurich](https://joelbarmettler.xyz/) and do [AI research](https://joelbarmettler.xyz/research/), [AI Keynote Speaker](https://joelbarmettler.xyz/auftritte/) and [AI Webinars](https://joelbarmettler.xyz/auftritte/webinar-2024-rewind-2025-ausblick/) in Zurich, Switzerland!

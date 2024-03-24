# AudioRec - A Python package

AudioRec is the most simple audio recorder for python. Record any sound from your standard recording device to WAV or MP3. Simply hit start with given duration - done.

- Record sound from the default input device
- Recording happens in another thread
- Save the sound as a wav
- Quickly convert it to MP3
- Delete file after use

# How to get it
To download AudioRec, Clone [this](https://github.com/rudymohammadbali/AudioRec) repository and add *AudioRec* folder into your project folder:
```sh
git clone https://github.com/rudymohammadbali/AudioRec
```
```sh
cd AudioRec
```
```sh
pip install -r requirements
```

Install ffmpeg for converting
```sh
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

# Usage

```python
import os
from AudioRec import Recorder

output_name = os.path.join(os.path.expanduser('~'), 'Desktop', 'output.wav')

rec = Recorder(chunk=1024, channels=1, rate=16000)

rec.start(duration=3, filename=output_name)
```
## Convert wav to mp3

Make sure ffmpeg is installed

```python
mp3_file = rec.wav_to_mp3(output_name)
```

## Delete file
```python
rec.delete(output_name)
```

# Coplete example
```python
import os
import time
from AudioRec import Recorder

output_name = os.path.join(os.path.expanduser('~'), 'Desktop', 'output.wav')

rec = Recorder(chunk=1024, channels=1, rate=16000)

# Start recording
rec.start(duration=3, filename=output_name)

time.sleep(5)
# Convert to mp3
mp3_file = rec.wav_to_mp3(output_name)

time.sleep(5)
# Delete file
rec.delete(output_name)
```

# Optinal parameters
When you initialize a recorder, you can define the chunk-size, the channels (2 for stereo default) and the bitrate (44100 Hz default).

```python
rec = Recorder(chunk=1024, channels=1, rate=16000)
```
<h2 align="left">Support</h2>

###

<p align="left">If you'd like to support my ongoing efforts in sharing fantastic open-source projects, you can contribute by making a donation via PayPal.</p>

###

<div align="center">
  <a href="https://www.paypal.com/paypalme/iamironman0" target="_blank">
    <img src="https://img.shields.io/static/v1?message=PayPal&logo=paypal&label=&color=00457C&logoColor=white&labelColor=&style=flat" height="40" alt="paypal logo"  />
  </a>
</div>

###

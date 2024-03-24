# Contributor: https://github.com/rudymohammadbali/

import os
import pyaudio
import subprocess
import threading
import wave

from termcolor import cprint


class Recorder:
    """A class for recording audio."""

    def __init__(self, chunk: int = 1024, channels: int = 2, rate: int = 44100):
        self.chunk = chunk
        self.channels = channels
        self.rate = rate
        self.format = pyaudio.paInt16

    def start(self, duration: int = 5, filename: str = "output.wav"):
        """Start recording audio."""
        thread = threading.Thread(target=self.__recording, args=(duration, filename))
        thread.start()

    def __recording(self, duration, filename):
        """Private method for recording audio."""
        input_device = self.setup_mic()

        if not input_device:
            cprint("[!] No valid input device found.", color="red")
            return

        print(f"[!] Using input device {input_device}")

        frames = []
        p = pyaudio.PyAudio()
        stream = p.open(format=self.format,
                        channels=self.channels,
                        rate=self.rate,
                        input=True,
                        input_device_index=input_device,
                        frames_per_buffer=self.chunk)

        print(f"[!] Start recording for {duration} seconds...")
        for _ in range(0, int(self.rate / self.chunk * duration)):
            data = stream.read(self.chunk)
            frames.append(data)

        cprint(f"[!] Saving as {filename}", color="green")
        self.save_to_file(p, frames, filename)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def save_to_file(self, p, frames, filename):
        """Save recorded audio to a file."""
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()

    @staticmethod
    def setup_mic():
        """Setup microphone for recording."""
        p = pyaudio.PyAudio()
        default_device_index = None
        try:
            default_input = p.get_default_input_device_info()
            default_device_index = default_input["index"]
        except IOError:
            cprint("[!] Default input device not found. Printing all input devices:", color="yellow")
            for i in range(p.get_device_count()):
                info = p.get_device_info_by_index(i)
                if info['maxInputChannels'] > 0:
                    cprint(f"[-] Device index: {i}, Device name: {info['name']}", color="grey")
                    if default_device_index is None:
                        default_device_index = i
        return default_device_index

    @staticmethod
    def delete(filename):
        """Delete a file."""
        if os.path.exists(filename):
            os.remove(filename)

    @staticmethod
    def wav_to_mp3(wav_file):
        """Convert a .wav file to .mp3."""
        if not os.path.isfile(wav_file):
            cprint(f"[!] The file {wav_file} does not exist.", color="red")
            return None

        if not wav_file.endswith('.wav'):
            cprint(f"[!] The file {wav_file} is not a .wav file.", color="red")
            return None

        mp3_file = wav_file[:-3] + "mp3"
        if os.path.isfile(mp3_file):
            os.remove(mp3_file)

        try:
            subprocess.check_call(['ffmpeg', '-i', wav_file, mp3_file])
        except subprocess.CalledProcessError as e:
            cprint(f"[!] Error occurred while converting {wav_file} to mp3: {str(e)}", color="red")
            return None

        return mp3_file


if __name__ == "__main__":
    output_name = os.path.join(os.path.expanduser('~'), 'Desktop', 'output.wav')

    rec = Recorder(chunk=1024, channels=1, rate=16000)

    # Start recording
    rec.start(duration=3, filename=output_name)

    # Convert to MP3
    # mp3_file = rec.wav_to_mp3(output_name)

    # Delete file
    # rec.delete(output_name)

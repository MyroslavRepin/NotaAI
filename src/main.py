import pyaudio
import wave


def record_audio(filename, duration=5, sample_rate=44100, channels=1):
    audio = pyaudio.PyAudio()

    chunk = 1024
    format = pyaudio.paInt16

    stream = audio.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for i in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))


if __name__ == "__main__":
    record_audio("output.wav", duration=5)

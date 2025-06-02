import pyaudio
import wave
import threading

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
OUTPUT_FILENAME = "output.wav"

frames = []
is_recording = True


def record():
    global frames, is_recording

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("🎤 Запись началась. Введите 1 и нажмите Enter, чтобы остановить.")

    while is_recording:
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"✅ Запись сохранена: {OUTPUT_FILENAME}")


def wait_for_input():
    global is_recording
    while True:
        user_input = input()
        if user_input.strip() == "1":
            is_recording = False
            break


if __name__ == "__main__":
    record_thread = threading.Thread(target=record)
    record_thread.start()

    wait_for_input()

    record_thread.join()

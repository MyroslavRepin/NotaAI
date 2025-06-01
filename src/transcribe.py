import whisper
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def transcribe_audio(audio_path, output_path="transcription.txt"):
    print(f"🎧 Загружаю аудио: {audio_path}")
    # Можно заменить на "base" или "tiny" для скорости
    model = whisper.load_model("small")

    result = model.transcribe(audio_path, language="ru")
    text = result["text"]

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Транскрипция завершена. Сохранено в: {output_path}")


if __name__ == "__main__":
    audio_file = input("🔗 Введи путь к аудиофайлу: ").strip()
    transcribe_audio(audio_file)

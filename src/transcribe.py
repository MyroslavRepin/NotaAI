import whisper


def transcribe_audio(audio_path, output_path="transcription.txt"):
    print(f"🎧 Загружаю аудио: {audio_path}")

    # Загружаем модель (можно заменить на "base", "medium", "large")
    model = whisper.load_model("small")

    # Транскрибируем без указания языка — Whisper сам определит язык
    result = model.transcribe(audio_path)

    # Сохраняем каждую фразу на новой строке
    with open(output_path, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            text = segment["text"].strip()
            f.write(text + "\n")

    print(f"✅ Транскрипция завершена. Сохранено в: {output_path}")


if __name__ == "__main__":
    audio_file = input("🔗 Введи путь к аудиофайлу: ").strip()
    transcribe_audio(audio_file)

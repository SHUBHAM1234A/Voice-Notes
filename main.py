from voice.recorder import record_audio
from voice.transcriber import transcribe_audio
from notes.manager import save_note, load_notes, search_notes 
from datetime import datetime

def create_voice_note():
    audio = record_audio(timeout=5, phrase_time_limit=4)
    text = transcribe_audio(audio)
    print(f"Transcribed:\n{text}")
    
    title = input("Title for this note (leave blank to auto-generate): ").strip()
    if not title:
        title = text[:30].strip() + "..." if len(text) > 30 else text

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    note = {
        "title": title,
        "content": text,
        "timestamp": timestamp,
        "tags": []
    }

    save_note(note)
    print("Note saved successfully.")

def show_all_notes():
    notes = load_notes()

    for i, note in enumerate(notes, 1):
        print(f"\n{i}. {note['title']} ({note['timestamp']})")
        print(note['content'])

def search_voice_notes():
    keyword = input("Enter keyword to search: ").strip().lower()
    results = search_notes(keyword)

    if not results:
        print("No matching notes found.")
    else:
        for i, note in enumerate(results, 1):
            print(f"\n{i}. {note['title']} ({note['timestamp']})")
            print(note['content'])

def main():
    while True:
        print("\nVoice Notes Menu")
        print("1. Create new voice note")
        print("2. View all notes")
        print("3. Search notes")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == "1":
            create_voice_note()
        elif choice == "2":
            show_all_notes()
        elif choice == "3":
            search_voice_notes()
        elif choice == "4":
            print("Exit")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    # main()
    show_all_notes()
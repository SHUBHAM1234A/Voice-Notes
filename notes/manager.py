import json
import os

notes_file = "storage.json"

def load_notes() -> list[dict]:
    """Loads all of the saved notes."""

    if not os.path.exists(notes_file):
        return []
    else:
        with os.open(notes_file, "r", "utf-8") as f:
            return json.load(f)

def save_note(note: dict) -> None:
    """Save a note to the storage."""

    notes = load_notes()
    notes.append(note)

    with os.open(notes_file, "w", "utf-8") as f:
        json.dump(notes, f, indent=2)

def search_notes(kw: str) -> list[dict]:
    """Searches for specific notes depending on the keyword."""

    kw = kw.lower()
    notes = load_notes()
    result = []

    for note in notes:
        if kw in note["title"]:
            result.append(note)
        elif kw in note["content"]:
            result.append(note)
        else:
            continue
    
    return result
from fastapi import APIRouter, HTTPException
from models.notes import Note

router = APIRouter()

notes = []


@router.post("/")
def create_note(note: Note):
    notes.append(note)
    return {"message": "Note created", "data": note}

@router.get("/")
def get_notes():
    return notes

@router.get("/{note_id}")
def get_notes_by_id(note_id: int):
    for note in notes:
        if note.id == note_id:
            return note
    return {"error": "Note not found"}


@router.get("/user/{user_id}")
def get_notes_by_user(user_id: int):
    user_notes = []
    for note in notes:
        if note.user_id == user_id:
            user_notes.append(note)
    if not user_notes:
        raise HTTPException(status_code=404, detail="No notes found for this user")
    return user_notes

@router.delete("/{note_id}")
def delete_note(note_id: int):
    note_to_delete = None
    for note in notes:
        if note.id == note_id:
            note_to_delete = note
    if note_to_delete is None:
        raise HTTPException(status_code=404, detail="Note not found")
    notes.remove(note_to_delete) 
    return {"message": f"Note {note_id} deleted successfully"}


@router.put("/{note_id}")
def update_note(note_id: int, updated_note: Note):
    for index, note in enumerate(notes):
        if note.id == note_id:
            notes[index] = updated_note
            return {"message": "Note updated", "data": updated_note}
    
    raise HTTPException(status_code=404, detail="Note not found")
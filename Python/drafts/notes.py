class NoteDict:
    def __init__(self):
        # Initialize an empty dictionary to store notes
        self.notes = {}

    def add_note(self, date, note):
        # Add a note to the dictionary with the given date
        self.notes[date] = note

    def get_note(self, date):
        # Get the note for the given date
        return self.notes.get(date, "Note not found")

    def edit_note(self, date, new_note):
        # Edit an existing note for the given date
        if date in self.notes:
            self.notes[date] = new_note
            return True
        else:
            return False

    def delete_note_by_date(self, date):
        # Delete the note for the given date
        if date in self.notes:
            del self.notes[date]
            return True
        else:
            return False

    def delete_note_by_keyword(self, keyword):
        # Delete the note based on a keyword search
        notes_to_delete = [date for date, note in self.notes.items() if keyword.lower() in note.lower()]

        if notes_to_delete:
            for date in notes_to_delete:
                del self.notes[date]
            return True
        else:
            return False

    def find_notes_by_date(self, date):
        # Find notes for the given date
        matching_notes = {date: note for date, note in self.notes.items() if date == date}
        return matching_notes

    def find_notes_by_keyword(self, keyword):
        # Find notes based on a keyword search
        matching_notes = {date: note for date, note in self.notes.items() if keyword.lower() in note.lower()}
        return matching_notes

    def sort_notes_by_date(self):
        # Sort notes by date
        sorted_notes = dict(sorted(self.notes.items()))
        return sorted_notes

    def view_all_notes(self):
        # View all notes in the dictionary
        return self.notes

# Example Usage:

# Create an instance of the NoteDict class
note_dict = NoteDict()

# Add notes
note_dict.add_note("2023-01-01", "New Year's Day")
note_dict.add_note("2023-02-14", "Valentine's Day")
note_dict.add_note("2023-07-04", "Independence Day")

# View all notes
print("All Notes:", note_dict.view_all_notes())

# Find notes by date
found_by_date = note_dict.find_notes_by_date("2023-02-14")
print("Notes found by date:", found_by_date)

# Find notes by keyword
found_by_keyword = note_dict.find_notes_by_keyword("independence")
print("Notes found by keyword:", found_by_keyword)

# Sort notes by date
sorted_notes = note_dict.sort_notes_by_date()
print("Sorted Notes by Date:", sorted_notes)


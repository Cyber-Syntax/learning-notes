const noteTitlesList = document.getElementById('note-titles');
const noteTitleInput = document.getElementById('note-title');
const noteContentInput = document.getElementById('note-content');
const saveNoteBtn = document.getElementById('save-note');

let activeNoteIndex = -1;
let notes = [];

function renderNoteTitles() {
  noteTitlesList.innerHTML = '';
  notes.forEach((note, index) => {
    const listItem = document.createElement('li');
    const title = note.title || 'Untitled Note';
    listItem.textContent = title;
    if (index === activeNoteIndex) {
      listItem.classList.add('active');
    }
    noteTitlesList.appendChild(listItem);
  });
}

function renderActiveNote() {
  const activeNote = notes[activeNoteIndex];
  if (activeNote) {
    noteTitleInput.value = activeNote.title;
    noteContentInput.value = activeNote.content;
  } else {
    noteTitleInput.value = '';
    noteContentInput.value = '';
  }
}

function saveNotes() {
  localStorage.setItem('notes', JSON.stringify(notes));
}

function loadNotes() {
  const notesData = localStorage.getItem('notes');
  if (notesData) {
    notes = JSON.parse(notesData);
    renderNoteTitles();
  }
}

function createNote() {
  const newNote = { title: '', content: '' };
  notes.push(newNote);
  activeNoteIndex = notes.length - 1;
  renderNoteTitles();
  renderActiveNote();
}

function deleteNote() {
  if (activeNoteIndex >= 0) {
    notes.splice(activeNoteIndex, 1);
    activeNoteIndex = -1;
    renderNoteTitles();
    renderActiveNote();
  }
}

function updateActiveNoteTitle(title) {
  if (activeNoteIndex >= 0) {
    const note = notes[activeNoteIndex];
    note.title = title;
    renderNoteTitles();
  }
}

function updateActiveNoteContent(content) {
  if (activeNoteIndex >= 0) {
    const note = notes[activeNoteIndex];
    note.content = content;
  }
}

noteTitlesList.addEventListener('click', (event) => {
  const clickedNoteIndex = Array.from(noteTitlesList.children).indexOf(event.target);
  if (clickedNoteIndex >= 0) {
    activeNoteIndex = clickedNoteIndex;
    renderNoteTitles();
    renderActiveNote();
  }
});

noteTitleInput.addEventListener('input', (event) => {
  updateActiveNoteTitle(event.target.value);
});

noteContentInput.addEventListener('input', (event) => {
  updateActiveNoteContent(event.target.value);
});

saveNoteBtn.addEventListener('click', () => {
    saveNotes();
});


  

createNote();

loadNotes();

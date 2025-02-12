$(document).ready(function() {
    // Flask'dan gelen verileri JavaScript objesine dönüştürme
    var data = { data , tojson };
    var habits = { habits , tojson };

    // Tabloyu oluşturma
    createTable(data, habits);

    // Tablodaki değişiklikleri kaydetme
    $('table').on('change', 'td input', function() {
        var value = $(this).val();
        var date = $(this).closest('tr').find('.date').text();
        var habit = $(this).closest('td').attr('id');
        updateData(date, habit, value);
    });

    // Hücreleri düzenleme
    $('table').on('click', 'td button', function() {
        var habit = $(this).closest('td').attr('id');
        $(this).hide();
        $(this).siblings('.edit-input').show();
        $(this).siblings('.edit-input').val(habits[habit]);
    });

    // Düzenlenen hücreleri kaydetme
    $('table').on('blur', 'td input', function() {
        var habit = $(this).closest('td').attr('id');
        habits[habit] = $(this).val();
        $(this).siblings('.edit-button').show();
        $(this).hide();
        updateHabits(habits);
    });

    // Yeni satır ekleme
    $('.add-row').click(function() {
        addRow();
    });

    // Yeni sütun ekleme
    $('.add-column').click(function() {
        addColumn();
    });
});

function saveData() {
    var data = {};
    var rows = document.querySelectorAll("table tbody tr");
  
    rows.forEach(function(row) {
      var rowData = {};
      var cells = row.querySelectorAll("td");
  
      cells.forEach(function(cell) {
        rowData.push(cell.innerText.trim());
      });
  
      data.push(rowData);
    });
  
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/save", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        console.log("Data saved successfully");
      }
    };
  
    xhr.send(JSON.stringify(data));
  }  
  function updateData() {
    const data = getDataFromTable(); // Tablodaki verileri alın
    fetch('/save', { // Belirlediğiniz URL'e POST isteği gönderin
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      console.log('Data saved:', data);
    })
    .catch(error => {
      console.error('Error saving data:', error);
    });
  }   
  function getDataFromTable() {
    const data = [];
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach(row => {
      const rowData = {
        date: row.querySelector('.date').innerText,
        habit1: row.querySelector('.habit1 input').checked,
        habit2: row.querySelector('.habit2 input').checked,
        habit3: row.querySelector('.habit3 input').checked
      };
      data.push(rowData);
    });
    return data;
  }
// Load the data from localStorage when the page loads
function loadData() {
let tableData = localStorage.getItem('tableData');
if (tableData) {
    tableData = JSON.parse(tableData);
    let rows = document.querySelectorAll('table tbody tr');
    rows.forEach((row, rowIndex) => {
    let rowData = tableData[rowIndex];
    rowData.forEach((cellData, cellIndex) => {
        let cell = row.querySelectorAll('td')[cellIndex];
        let checkbox = cell.querySelector('input[type="checkbox"]');
        checkbox.checked = cellData;
    });
    });
}
}
// Add an event listener to save the data whenever the table changes
let table = document.querySelector('table');
table.addEventListener('change', saveData);
// Load the data when the page loads
loadData();
function editHabit(button) {
let cell = button.parentNode;
let habitText = cell.querySelector('.habit');
let editInput = cell.querySelector('.edit-input');

if (habitText.style.display === 'none') {
    // Düzenleme modundan görüntüleme moduna geçiş yapın
    habitText.textContent = editInput.value;
    habitText.style.display = 'inline';
    editInput.style.display = 'none';
    button.textContent = 'Edit';
} else {
    // Görüntüleme modundan düzenleme moduna geçiş yapın
    habitText.style.display = 'none';
    editInput.style.display = 'inline';
    editInput.value = habitText.textContent;
    // enter allowed to save
    editInput.addEventListener('keyup', function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            button.click();
        }
    });
    button.textContent = 'Save';
    }
}
function addColumn() {
    var table = document.querySelector('table');
    var habitCount = table.rows[0].cells.length - 2;
    var newHabitCount = habitCount + 1;
    
    // Add new header cell for the habit
    var newHeader = table.rows[0].insertCell(-1);
    newHeader.innerHTML = `
      <span class="habit">Habit ${newHabitCount}</span>   
      <input type="text" class="edit-input" style="display:none;" />
      <button class="edit-button" onclick="editHabit(this)">Edit</button>			
    `;
    
    // Add checkbox cells for all rows
    for (var i = 0; i < table.rows.length; i++) {
      var row = table.rows[i + 1];
      var checkboxCell = row.insertCell(-1);
      var checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.id = `habit${newHabitCount}_${i}`;
      checkboxCell.appendChild(checkbox);
    }
  
    updateData();
  }
  

function addRow() {
  var table = document.querySelector('table');
  var row = table.insertRow(-1);
  var dateCell = row.insertCell(0);

  // if column 1 is empty, add the column 
  if (table.rows[0].cells.length < 2) {
    addColumn();
  }

  var habitCell = row.insertCell(1);
  // Add the date to the first cell
  var date = new Date();
  var day = date.getDate();
  var month = date.getMonth() + 1;
  var year = date.getFullYear();
  dateCell.innerHTML = `${day}.${month}.${year}`;
  dateCell.classList.add('date');

  // add a checkbox to the last cell of the new row
  var cell = row.insertCell(1);
  var checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.id = `habit${row.rowIndex}${table.rows[0].cells.length}`;
  cell.appendChild(checkbox);

  updateData();
}

  

  
  
function updateCheckbox(checkbox) {
    const cell = checkbox.parentNode;
    cell.setAttribute('data-changed', 'true');
    updateData(); // Tablodaki verileri kaydet
  }
// Initialize the table with rows for each day of the week
for (let i = 0; i < days.length; i++) {
    addRow();
}


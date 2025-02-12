from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__, static_folder='static')
# Öntanımlı kayıt dosyası
save_file = "habits.json"

# Kayıt dosyası varsa yükle
if os.path.exists(save_file):
    with open(save_file, "r") as f:
        habits = json.load(f)
else:
    habits = []

# Tabloya satır ekleme fonksiyonu
@app.route('/add_row', methods=['POST'])
def add_row():
    data = request.json
    habits.append(data)
    with open(save_file, "w") as f:
        json.dump(habits, f)
    return jsonify(habits)

# Tabloya sütun ekleme fonksiyonu
@app.route('/add_column', methods=['POST'])
def add_column():
    data = request.json
    for habit in habits:
        habit[data['date']] = 0
    with open(save_file, "w") as f:
        json.dump(habits, f)
    return jsonify(habits)

@app.route('/', methods=['GET', 'POST'])
def index():
    items = []
    try:
        with open('data.json', 'r') as f:
            items = json.load(f)
    except FileNotFoundError:
        pass

    if request.method == 'POST':
        data = request.get_json()
        items = data['items']

        with open('data.json', 'w') as f:
            json.dump(items, f)

    return render_template('index.html', items=items)
    

@app.route('/save', methods=['POST'])
def save():
    try:
        data = request.get_json()
        with open('data.json', 'w') as f:
            json.dump(data, f)
            f.flush()
            os.fsync(f.fileno())
            f.close()
        return 'OK'
    except Exception as e:
        print('Error saving data:', e)
        return 'Error saving data'

if __name__ == '__main__':
    app.run(debug=True)

import sqlite3
from flask import Flask, render_template, request # pyright: ignore[reportMissingImports]

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO submissions (name, email, message) VALUES (?, ?, ?)',
                   (name, email, message))
    conn.commit()
    conn.close()
    
    return render_template('success.html', user_name=name)

# NEW: Route to display all submissions
@app.route('/submissions')
def submissions_page():
    conn = sqlite3.connect('feedback.db')
    conn.row_factory = sqlite3.Row # This allows accessing columns by name
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM submissions ORDER BY timestamp DESC')
    all_submissions = cursor.fetchall()
    
    conn.close()
    
    return render_template('submissions.html', submissions=all_submissions)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
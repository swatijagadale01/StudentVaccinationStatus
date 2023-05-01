from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Connect to the database
db = mysql.connector.connect(
    host="3307",
    user="root",
    password="",
    database="mydb"
)

# Define the route for the home page
@app.route('/')
def home():
    return '''
        <form method="POST" action="/vaccination">
            <label for="regno">Enter registration number:</label>
            <input type="text" id="regno" name="regno">
            <button type="submit">Get vaccination status</button>
        </form>
    '''

# Define the route for retrieving the vaccination status
@app.route('/vaccination', methods=['POST'])
def vaccination():
    regno = request.form['regno']
    cursor = db.cursor()
    cursor.execute(f"SELECT Vaccination_Status FROM students WHERE RegNo='{regno}'")
    result = cursor.fetchone()
    if result:
        return f"The vaccination status of student with registration number {regno} is {result[0]}"
    else:
        return f"No student found with registration number {regno}"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

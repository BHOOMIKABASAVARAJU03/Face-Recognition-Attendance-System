import csv
import signal
from flask import Flask, render_template, redirect, url_for
import os
import subprocess


app = Flask(__name__)
process = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/attendance')
def attendance():
    records = []
    with open('Attendance.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        for row in csvreader:
            print(row)
            records.append(row)
    enumerated_records = list(enumerate(records, start=1))
    return render_template('AttendancePage.html', records=enumerated_records)


@app.route('/start_recognition', methods=['POST'])
def start_recognition():
    global process
    if process is None:
        python_interpreter = r'C:\Users\Lata\PycharmProjects\pythonProject1\.venv\Scripts\python.exe'
        process = subprocess.Popen([python_interpreter, "AttendanceProject.py"])
    return redirect(url_for('index'))


@app.route('/stop_recognition', methods=['POST'])
def stop_recognition():
    global process
    if process is not None:
        process.terminate()
        process.wait()
        process = None
    return  redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
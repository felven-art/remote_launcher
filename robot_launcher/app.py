from flask import Flask
from flask import render_template
from flask import request
from flask import session
import json
import subprocess
import time

app = Flask(__name__)

def process_exist(process_name):
    '''
    process_name: Name of the process that will be checked whether it exists or not (eg. excel.exe).
    Function returns True/False.
    '''
    s = subprocess.check_output('tasklist', shell=True)
    if process_name.lower() in str(s).lower():
        return True
    else:
        return False

def process_status(process_name, process_path):
    '''
    process_name: Name of the process that is checked whether it's working or not.
    process_path: Path to the application that should be started.
    Returns json response for jQuery.
    '''
    try:
        if process_exist(process_name):
            return json.dumps({'status': 'OK'})
        else:
            subprocess.Popen(process_path)
            return json.dumps({'status':'OK'})
    except Exception:
        print(Exception)
        return None



@app.route('/')
def main_page():
    if process_exist('excel.exe') == True or process_exist('Calculator.exe') == True:
        # print('Process exists!')
        return render_template('layout.html', process_running=True)
    else:
        # print('No process.')
        return render_template('layout.html', process_running=False)

@app.route('/run_process', methods=['POST'])
def run_process():
    print(request.form)
    if 'excel' in request.form:
        return process_status('EXCEL.EXE', r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE')
    elif 'calc' in request.form:
        return process_status('Calculator.exe', r'C:\Windows\System32\calc.exe')
    return 'POST method invalid. ' + str(request.form)

@app.route('/status', methods=['POST'])
def status():
    print(request.get_json())

@app.route('/test_ajax', methods=['POST'])
def test_ajax():
    print(request.get_json())
    time.sleep(5)
    return json.dumps({'status:':'OK'})

app.run(threaded=True, host='0.0.0.0')
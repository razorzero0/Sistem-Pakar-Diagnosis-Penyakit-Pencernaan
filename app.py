from flask import Flask, session,  url_for, render_template, request
from helpers import diagnosis,symptoms
from questions import questions

app = Flask(__name__)
app.secret_key = 'iot'


@app.route("/")
def index():
       symptoms.clear()
       session['gejalaPasien'] = 1
       return render_template('index.html', link = url_for('index'))


@app.route('/diagnosa',methods = ['POST', 'GET'])
def diagnosa():
    symptoms.clear()
    if  request.form.get('Name'):
         session['name'] = request.form.get('Name').upper()
    pertanyaan = questions
    return render_template("diagnosa.html", pertanyaan = pertanyaan, name =  session['name'], link = url_for('hasil'))
            
@app.route('/hasil',methods = ['POST', 'GET'])
def hasil():   
    if request.form.get('threshold'): 
         session['threshold'] = int(request.form.get('threshold'))
    [r,m] = diagnosis()
    d = []
    for i in range(len(r)):
         d.append([r[i]['penyakit'],round(r[i]['nilai'],2),r[i]["gejala"]])
         
    maxNilai = str(m[1])[:4] if float(m[1]) >= session['threshold'] else False
    return render_template("result.html",threshold = session['threshold'], diagnosa=d,maxPenyakit = m[0],maxNilai = maxNilai,maxGejala =m[2] ,name=session['name'],awal = url_for('diagnosa'))


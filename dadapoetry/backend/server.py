import os
import sqlite3
from flask import (Flask, flash, request, redirect, url_for,
                   send_from_directory, render_template)
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/arnaldo/Imagens/imgs/'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def getDbConnection():
    conn = sqlite3.connect('dada.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        file = request.files['file']
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            conn = getDbConnection()
            conn.execute("INSERT INTO dada (filename, content) VALUES (?, ?)",
                (filename, path)
            )
            conn.close()
            # return redirect(url_for('downloadFile', name=filename))
            return redirect(url_for('downloadFile', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<name>')
def downloadFile(name):

    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

if __name__ == '__main__':
    app.run(host='localhost', port='8560', debug=True)

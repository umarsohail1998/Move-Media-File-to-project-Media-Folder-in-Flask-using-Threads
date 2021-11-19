from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_PATH'] = './uploads'

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)



@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['img']
    if uploaded_file.filename != '':
      uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)
 
if __name__ == '__main__':
   app.run(debug = True)


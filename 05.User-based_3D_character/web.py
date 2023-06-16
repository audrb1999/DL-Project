from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask import send_file
import os

import pickle

app = Flask(__name__)
# 홈페이지
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/home")
def file_home():
	return render_template("home.html")

#업로드 HTML 렌더링
@app.route('/upload')
def upload_page():
	return render_template('upload.html')


# 파일 업로드
@app.route("/file_upload", methods = ['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploads/' + secure_filename(f.filename))
        files = os.listdir("./uploads")

                
        return render_template('check.html')
    else:
        return render_template('index.html')


#다운로드 HTML 렌더링
@app.route('/downfile')
def down_page():
	files = os.listdir("./downloads")
	return render_template('filedown.html',files=files)


#파일 다운로드 처리
@app.route('/down_file', methods = ['GET', 'POST'])
def down_file():
	if request.method == 'POST':
		sw=0
		files = os.listdir("./downloads")
		for x in files:
			if(x==request.form['file']):
				sw=1

		path = "./downloads/"
		return send_file(path + request.form['file'] + '.zip',
				as_attachment=True)

#서버 실행
if __name__ == "__main__":
	app.run()
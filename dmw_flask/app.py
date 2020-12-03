import os
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import pandas as pd

#UPLOAD_FOLDER = '/home/sid/flask_tut/'

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('index.html')
	
	question=request.form.get('question')
	#	image = file.read()
	#filename = secure_filename(file.filename)
	

	
	from to_call import f
	li=f(question)
	
	print(li)

#		filename = 'http://127.0.0.1:5000/' + filename
		#return render_template('result.html',category=fin,filename=filename)
	return render_template('result.html', your_list=li)



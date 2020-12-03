import os
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import pandas as pd

#UPLOAD_FOLDER = '/home/sid/flask_tut/'

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def hello_world():

	if request.method == 'POST':
            if request.form['Recommend'] == 'Recommend':
            	question=request.form.get('question')
            	from to_call import f
            	li=f(question)
            	return render_template('result.html', your_list=li)
				
                
            elif  request.form['Recommend'] == 'predict':
            	
            	return render_template('graphs.html')
                
            else:
                
            	return render_template("index.html")
	elif request.method == 'GET':
            
            return render_template('index.html')



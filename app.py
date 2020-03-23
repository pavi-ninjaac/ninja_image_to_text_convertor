from flask import Flask,render_template,request
import os
from detect_text import Detect_text
image_folder=os.path.join('static','upload')
app=Flask(__name__)
app.config['uploaded_folder']=image_folder
@app.route('/')
def upload_image_html():
    return render_template('upload_image.html')
@app.route('/detect_image',methods=['GET','POST'])
def upload():
    file=request.files['file']
    name=request.files['file'].filename
    if name !='':
        file_path=os.path.join(app.config['uploaded_folder'], name)
        file.save(file_path)
        text=Detect_text.Detect_text_method(file_path)
        return render_template('display_image.html',text=text,img_src=file_path)


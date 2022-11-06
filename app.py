import download as aap
import logs
import pdftotxt
import kafkaProducer
from flask import Flask, render_template, request

app = Flask(__name__)
  
@app.route('/')
def hello_name():
    return render_template('index.html')

@app.route('/download/', methods = ['POST', 'GET'])
def download():
    if request.method == 'POST':
        aap.download()
        result="Downloaded Successfully"
        train = logs.demo()
        return render_template('index.html', airblueTextfiles=train[0], airindiaTextfiles=train[1], destinationTextfiles=train[2])


@app.route('/convert/', methods = ['POST', 'GET'])
def convert():
    if request.method == 'POST':
        pdftotxt.fileWriting()
        result="Converted Successfully"
        train = logs.demo()
        return render_template('index.html', airblueTextfiles=train[0], airindiaTextfiles=train[1], destinationTextfiles=train[2])

@app.route('/produce/', methods = ['POST', 'GET'])
def produce():
    if request.method == 'POST':
        kafkaProducer.producer()
        result="Produced Successfully"
        train = logs.demo()
        return render_template('index.html', airblueTextfiles=train[0], airindiaTextfiles=train[1], destinationTextfiles=train[2])


if __name__ == '__main__':
    app.run(debug=True)
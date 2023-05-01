from flask import Flask, render_template, redirect, url_for, request
from requestAPI import chat_completion, fix_spelling_mistake, create_image

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('request.html')

@app.route('/ask-gpt', methods=['POST', 'GET'])
def askGPT():
    content = request.form['ask-gpt']
    return render_template('response.html', completion=chat_completion(content), content=content)

@app.route('/edit-mistake', methods=['POST', 'GET'])
def editMistake():
    content = request.form['edit-mistake']
    return render_template('response.html', mistake=fix_spelling_mistake(content), content=content)

@app.route('/create-image', methods=['POST', 'GET'])
def createImage():
    content = request.form['create-image']
    return render_template('response.html', image=create_image(content), content=content)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
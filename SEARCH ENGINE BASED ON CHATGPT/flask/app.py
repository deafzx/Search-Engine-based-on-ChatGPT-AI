from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form['input_text']
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
    )
    return response["choices"][0]["text"]

if __name__ == '__main__':
    app.run(debug=True)
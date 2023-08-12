from transformers import pipeline
pipe = pipeline("question-answering", model="deepset/roberta-base-squad2")
def predict(question, context):
    result = 'You are welcome'
    result = pipe(question=question, context=context)
    result = result['answer']
    return result

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        context = request.form['context']
        question = request.form['question']
        if context == '':
            context = 'None'
        if question == '':
            question = 'None'
        pred = 'None'
        pred = predict(question,context)
        result = f"result : {pred}"
        return render_template('index.html', result=result,context=context, question=question)
    return render_template('index.html',context='', question='')

if __name__ == '__main__':
    app.run(debug=True)

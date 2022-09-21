from flask import Flask, render_template, request
import json
app=Flask(__name__)

hospital_list = []
with open('hospitals.json') as f:
        hospital_list = json.load(f)

@app.route('/')
def index():
    markers=hospital_list
    return render_template('index.html',markers=markers )

if __name__ == '__main__':
    app.run(debug=True)

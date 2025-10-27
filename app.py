from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    rollno = request.form['rollno']
    email = request.form['year_email']
    year = request.form['year']
    return render_template('result.html', name=name, rollno=rollno, email=email, year=year)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

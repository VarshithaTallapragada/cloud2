from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello',methods=['GET'])
def hello():
    # Renders an index.html file located in the 'templates' folder
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

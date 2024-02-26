from flask import Flask, request, jsonify , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    number = data['number']
    result = f'{number} not number.'
    return jsonify({'result': result})

if __name__ == '__main__':

    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, static_url_path='/')

@app.route('/')
def index():
    with open('./static/pevents.json', 'r') as f:
        data = json.load(f)
    return render_template('edit.html', data=json.dumps(data, indent=4))

@app.route('/update', methods=['POST'])
def update():
    new_data = request.json
    with open('./static/pevents.json', 'w') as f:
        json.dump(new_data, f)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)

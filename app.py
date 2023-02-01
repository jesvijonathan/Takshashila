from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import razorpay

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '<h1>TK-2023<h1>'


@app.route("/parameter/<parameter>", methods=['GET'])
def hello_name(parameter):
    return f'<h1>Some Random var - {parameter}</h1>'


@app.route("/create-payment", methods=['GET', 'POST'])
def payment_razor():
    if request.method == "POST":
        data = json.loads(request.data.decode('utf8').replace("'", '"'))
        print(data)
        client = razorpay.Client(auth=("rzp_test_pCtS1bVBcTs4hF", "F3RUI6Wye5uolFutMz8q7BDs"))
        data = client.order.create({
            "amount": data['amount'] * 100,
            "currency": "INR",
            "receipt": data['name']
        })
        return jsonify(data)
    else:
        data = {"first_name": "Rahul", "last_name": "Navneeth"}
        return render_template("create-payment.html", user=data)


if __name__ == '__main__':
    app.run()

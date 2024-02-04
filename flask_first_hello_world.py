from flask import Flask
import os
import requests,jsonify
s= requests.session()
app = Flask(__name__)


@app.route("/")
def hello():
   return "Hello world!!!"

'''def test_api_hello_world():
   response = s.get("http://127.0.0.1:5000/")
   print(response.text)'''


if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))
   app.run(debug=True, host='0.0.0.0', port=port)
   #test_api_hello_world()

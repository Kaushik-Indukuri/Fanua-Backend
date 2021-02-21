from flask import Flask, jsonify
from flask import request
import requests

app = Flask(__name__)

api_key = "0011918cf4msh9e040a715a98ae4p159e8cjsnb86d38750d44"
limit = 10

# /query?city=dublin&state=ca&proptype=single_family

@app.route('/query')
def query():
    global prop_type
    global state
    global city
    args = request.args

    if "city" in args:
        city = args.get("city")
    if "state" in args:
        state = args.get("state")
    if "proptype" in args:
        prop_type = args.get("proptype")

    # url for api
    url = "https://realtor.p.rapidapi.com/properties/v2/list-for-sale"

    # enter parameters
    querystring = {
        "sort": "relevance",
        "city": city,
        "offset": "0",
        "limit": limit,
        "state_code": state,
        "prop_type": prop_type
    }

    # header
    headers = {
        'x-rapidapi-host': "realtor.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    # response
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()




if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

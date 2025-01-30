from functools import wraps
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt


# This flask app is going to be an api
app = Flask(__name__)
api = Api(app)


# db setup
client = MongoClient("mongodb://mongodb:27017")
db = client.SentencesDatabase
users = db['Users']

# ***********************************************


# Register users
class Register(Resource):
    def post(self):
        # get posted data by the user
        postedData = request.get_json()

        # data
        username = postedData["username"]
        password = postedData["password"]

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        users.insert_one({
            "Username": username,
            "Password": hashed_pw,
            "Sentence": "",
            "Tokens": 6
        })

        retJson = {
            "status": 200,
            "msg": "You successfully signed up for the API"
        }
        return jsonify(retJson)


def UserExist(username):
    # if users.find({"Username":username}).count() == 0:
    if users.count_documents({"Username":username}) == 0:
        return False
    else:
        return True


def verifyPw(username, password):
    hashed_pw = users.find({
        "Username": username
    })[0]["Password"]
    if bcrypt.hashpw(password.encode('utf-8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False


def countTokens(username):
    tokens = users.find({
        "Username": username
    })[0]["Tokens"]
    return tokens


class Store(Resource):
    def post(self):
        # get the posted data
        postedData = request.get_json()

        # read the data
        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData["sentence"]

        # verify the username pw match
        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status": 302
            }
            return jsonify(retJson)

        # Verify user has enough tokens
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        # store the sentence, take one token away  and return 200OK
        users.update_one({
            "Username": username
        }, {
            "$set": {
                "Sentence": sentence,
                "Tokens": num_tokens-1
                }
        })

        retJson = {
            "status": 200,
            "msg": "Sentence saved successfully"
        }
        return jsonify(retJson)


class Get(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]

        # verify the username pw match
        correct_pw = verifyPw(username, password)
        if not correct_pw:
            retJson = {
                "status": 302
            }
            return jsonify(retJson)

        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        # MAKE THE USER PAY!
        users.update_one({
            "Username": username
        }, {
            "$set": {
                "Tokens": num_tokens-1
                }
        })

        sentence = users.find({
            "Username": username
        })[0]["Sentence"]
        retJson = {
            "status": 200,
            "sentence": str(sentence)
        }

        return jsonify(retJson)


# ************************************************


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Get, '/get')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

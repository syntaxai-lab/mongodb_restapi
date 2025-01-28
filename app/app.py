import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
import bcrypt


# Api Setup
app = Flask(__name__)
api = Api(app)


# db setup
client = MongoClient("mongodb://db:27017")
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


# ************************************************
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

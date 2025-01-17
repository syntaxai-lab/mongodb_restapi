from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from sentence_transformers import SentenceTransformer



# Api Setup
app = Flask(__name__)
api = Api(app)


# 



# ************************************************ 
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
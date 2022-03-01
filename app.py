from flask import Flask, request, jsonify
from transformers import pipeline
from flask_restx import Resource, Api


app = Flask(__name__)
api = Api(app)
@api.route("/sentiment", methods=['GET', 'POST'])
class SentmentAnalyser(Resource):
    def get(self):
        return jsonify({"message":"Welcome to sentiment analysier"})
    def post(self):
        classifier = pipeline('sentiment-analysis', model='test_trainer')
        text = request.get_json()['text']
        sentiment = classifier(text)
        return jsonify(sentiment)

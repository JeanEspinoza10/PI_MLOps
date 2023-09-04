from flask_restx import fields

class SentimentAnalysisRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace
    
    def count(self):
        return self.namespace.model("Reviews",
        {
            "año": fields.Integer()
        }
        )
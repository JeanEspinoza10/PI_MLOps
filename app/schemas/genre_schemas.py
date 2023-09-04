from flask_restx import fields

class GenreRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace
    def get(self):
        return self.namespace.model("Genre",
        {
            "género": fields.String(max_length=250, required=True)
        }
        )
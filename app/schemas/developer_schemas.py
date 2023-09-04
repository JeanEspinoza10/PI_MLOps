from flask_restx import fields

class DeveloperRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace
    def get(self):
        return self.namespace.model("Developer",
        {
            "developer": fields.String(max_length=200, required=True)
        }
        )
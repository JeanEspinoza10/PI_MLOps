from flask_restx import fields

class UserRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace
    
    def get(self):
        return self.namespace.model("User",
        {
            "user_id": fields.String(max_length=250)
        }
        )
    def userforgenre(self):
        return self.namespace.model("Género",
        {
            "género": fields.String(max_length=250, required=True)

        })
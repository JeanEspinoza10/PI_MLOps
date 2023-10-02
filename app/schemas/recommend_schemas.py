from flask_restx import fields

class RecommendRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace
    
    def fecha(self):
        return self.namespace.model("Recommend",
        {
            "Fecha": fields.Date(
                description="Fecha de inicio en formato YYYY.",
                example="2023",
                required=True
            )
        }
        )
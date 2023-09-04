from flask_restx import fields

class ReviewsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace
    
    def count(self):
        return self.namespace.model("Reviews",
        {
            "Inicio": fields.Date(
                description="Fecha de inicio en formato YYYY-MM-DD.",
                example="2023-09-04",
                required=True
            ),
            "Fin": fields.Date(
                description="Fecha de fin en formato YYYY-MM-DD.",
                example="2023-09-10",
                required=True
            )
        }
        )
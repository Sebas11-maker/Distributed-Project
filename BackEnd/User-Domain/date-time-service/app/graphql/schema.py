import strawberry
from datetime import datetime

@strawberry.type
class Query:
    @strawberry.field
    def current_time(self) -> str:
        # Devuelve la hora exacta en formato ISO 8601
        return datetime.now().isoformat()

schema = strawberry.Schema(query=Query)

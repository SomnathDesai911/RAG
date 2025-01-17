from pydantic import BaseModel,Field
from typing import List, Optional

class UserQuery(BaseModel):
    query: str=Field(description="User request")
    limit_context: Optional[int] = None 

class QueryResponse(BaseModel):
    query: str
    retrieved_contexts: List[str]=Field(description='List of context retirved')

    





    
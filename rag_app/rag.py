import random
from typing import List
from .mockstore import MockDataStoreGenAI


def retrieve_data(query:str,context_limit:int):
    retrieved=[]
    for key,context in MockDataStoreGenAI.items():
        if key.lower() in query.lower():
            retrieved.extend(context)
    return retrieved[:context_limit]

def generate_response(query:str,retirved_context:List):
    combined_context="\n".join(retirved_context)
    response = f"{query}\n{combined_context}"
    return response








            
        


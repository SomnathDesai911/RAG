import asyncio

async def stream_generator(response: str):
    splitted_response=response.split("\n")
    for chunk in splitted_response:
        await asyncio.sleep(1)
        yield f"{chunk}\n"


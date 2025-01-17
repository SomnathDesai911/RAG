from .import_libs import*


app = FastAPI()
set_logging(log_file="query.log", mode="w")
logger = get_logger(__name__)
app.add_exception_handler(ValidationError, validation_exception_handler)

@app.post("/query", response_model=QueryResponse,responses=responses)
async def query(request: UserQuery):
    logger.info(f"Received user query: {request.query}")

    if not request.query.strip():
        logger.error("Query is empty or invalid.")
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty or invalid."
        )
    
    if request.limit_context is not None and request.limit_context != 0:
        try:
            request.limit_context = int(request.limit_context)
        except ValueError:
            logger.error(f"Invalid limit_context value provided: {request.limit_context}")
            raise HTTPException(
                status_code=422,
                detail="Invalid value for limit_context. It should be an integer."
            )

        if request.limit_context <= 0:
            logger.error(f"Invalid limit_context value provided: {request.limit_context}. It should be a positive value.")
            raise HTTPException(
                status_code=422,
                detail="Invalid value for limit_context. It should be a positive integer."
            )
    limit_context_value = None if request.limit_context is None or request.limit_context == 0 else request.limit_context
    retrieved_contexts = retrieve_data(request.query, limit_context_value)

    if not retrieved_contexts:
        logger.warning(f"No relevant contexts found for query: {request.query}")
        raise HTTPException(status_code=404, detail="No relevant contexts found.")

    response_text = generate_response(request.query, retrieved_contexts)
    logger.info("Successfully delivered data to user.")
    return StreamingResponse(
        stream_generator(response_text), media_type="text/plain"
    )
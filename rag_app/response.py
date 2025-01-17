responses = {
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "example": {"detail": "Query cannot be empty or invalid."}
            }
        }
    },
    422: {
        "description": "Unprocessable Entity",
        "content": {
            "application/json": {
                "example": {"detail": "Invalid value for top_k. It should be an integer."}
            }
        }
    },
    404: {
        "description": "No Relevant Contexts Found",
        "content": {
            "application/json": {
                "example": {"detail": "No relevant contexts found."}
            }
        }
    }
}

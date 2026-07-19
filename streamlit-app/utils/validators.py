def validate_search(query):

    if not query:
        return False

    return len(query.strip()) >= 2


def validate_symbol(symbol):

    return bool(symbol)


def validate_response(response):

    return (
        isinstance(response, dict)
        and response.get("status") == "success"
    )
SERVER_ERROR = "TODO_API_0001"
ERRORS = [
    (SERVER_ERROR, "Server Error"),
]


def get_error_dict(error_code, message=None):
    if message is None:
        try:
            message = dict(ERRORS)[error_code]
        except KeyError:
            raise AttributeError(f"{error_code} error does not exist")

    return {"code": error_code, "message": message}

def auth_flow(fun):
    def wrapper(*args, **kwargs):
        if not kwargs.get("is_auth"):
            print("unauth")
            raise PermissionError("unauth")
        return fun(*args, **kwargs)
    return wrapper


@auth_flow
def auth(*args, **kwargs):
    print("authenticating")


auth(is_auth=True)

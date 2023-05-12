from cookiecutter.utils import simple_filter


@simple_filter
def greeting_filter(name: str) -> str:
    return f"Hello {name}!"

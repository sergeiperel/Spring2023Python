def get_greeting(name: str) -> str:
    return "Hello, " + name + "!"


if __name__ == "__main__":
    assert get_greeting("World") == "Hello, World!"
    assert get_greeting("Anonymous") == "Hello, Anonymous!"

    message = get_greeting("World")
    print(message)

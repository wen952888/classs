def convert_subscription(link: str) -> str:
    if not link.startswith("http"):
        raise ValueError("Invalid subscription link. Must start with 'http'.")

    converted_link = link.replace("old_format", "new_format")
    return converted_link
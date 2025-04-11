import requests

def translate_text(text: str, target_language: str = "en") -> str:
    """
    Translate the given text to the target language using a translation API.
    :param text: Text to translate.
    :param target_language: Target language code (default is 'en' for English).
    :return: Translated text.
    """
    api_url = "https://example-translate-api.com/translate"
    api_key = "your_api_key_here"

    try:
        response = requests.post(api_url, json={
            "text": text,
            "target_language": target_language,
            "api_key": api_key
        })
        response.raise_for_status()
        data = response.json()
        return data.get("translated_text", "Translation not available.")
    except requests.RequestException as e:
        raise RuntimeError(f"API request failed: {e}")
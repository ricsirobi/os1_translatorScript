import urllib.parse as up
import requests

# ./shellscript.sh -f hu -t en -w "eper"

# word = "eper"
# target = "en"
# source = "hu"


def csinald(source, target, word):
    if len(source) == 0:
        source = up.quote("hu")
    if len(target) == 0:
        target = up.quote("en")

    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = (
        "q="
        + up.quote(word.lower())
        + "&target="
        + up.quote(target.lower())
        + "&source="
        + up.quote(source.lower())
        + ""
    )

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "accept-encoding": "application/gzip",
        "x-rapidapi-key": "5cca084016msh3c02e2e347d45bcp1c478ajsne900a02d99c3",
        "x-rapidapi-host": "google-translate1.p.rapidapi.com",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    translation_data = response.json()
    translation = translation_data["data"]["translations"][0]["translatedText"]

    print(translation.lower())

import requests

def jokes():
    url = "https://official-joke-api.appspot.com/random_joke"

    r = requests.get(url)

    data = r.json()

    return {
        "setup": data['setup'],
        "punchline": data['punchline']
    }
    # print(f" Setup: {data['setup']}")
    # print(f"Punchline : {data['punchline']}")
print(jokes())
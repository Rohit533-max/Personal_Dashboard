import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        r = requests.get(url)
        r.raise_for_status()
        user = r.json()
        print("\n===== GitHub User Profile =====")
        print(f"Name           : {user.get('name')}")
        print(f"Username       : {user.get('login')}")
        print(f"Bio            : {user.get('bio')}")
        print(f"Company        : {user.get('company')}")
        print(f"Location       : {user.get('location')}")
        print(f"Public Repos   : {user.get('public_repos')}")
        print(f"Followers      : {user.get('followers')}")
        print(f"Following      : {user.get('following')}")
        print(f"Created At     : {user.get('created_at')}")
        print(f"Profile URL    : {user.get('html_url')}")
        print(f"Avatar URL     : {user.get('avatar_url')}")
        print("===============================\n")
    except requests.exceptions.RequestException as e:
        print("Error",e)
get_github_user("cz")
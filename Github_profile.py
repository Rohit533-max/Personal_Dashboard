import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        r = requests.get(url)
        if r.status_code == 404:
           return {f"User Not Found"}
        r.raise_for_status()
        if r.status_code == 200:
            user = r.json()
            return {
            "\n===== GitHub User Profile ====="
            "Name"           : user.get('name'),
            "Username"      : user.get('login'),
            "Bio"            : user.get('bio'),
            "Company"        : user.get('company'),
            "Location"       : user.get('location'),
            "Public Repos"   : user.get('public_repos'),
            "Followers"      : user.get('followers'),
            "Following"      : user.get('following'),
            "Created At"     : user.get('created_at'),
            "Profile URL"    : user.get('html_url'),
            "Avatar URL"     : user.get('avatar_url')
        }
    except requests.exceptions.RequestException as e:
        return f"Error,str(e)"

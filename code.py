import requests
import pandas as pd
import time


TOKEN = "Github token"
HEADERS = {"Authorization": f"token {TOKEN}"}

def fetch_users():
    users = []
    page = 1
    while True:
        url = f"https://api.github.com/search/users?q=location:Delhi+followers:>100&per_page=100&page={page}"
        response = requests.get(url, headers=HEADERS).json()

        if "items" not in response or not response["items"]:
            break  # Exit loop if no more items are returned

        users.extend(response["items"])
        page += 1
        time.sleep(1)  # Pause to avoid hitting rate limits

    return users

def fetch_user_details(login):
    url = f"https://api.github.com/users/{login}"
    response = requests.get(url, headers=HEADERS).json()
    time.sleep(1)  # To respect GitHub rate limits
    return {
        "login": response.get("login", ""),
        "name": response.get("name", ""),
        "company": clean_company(response.get("company", "")),
        "location": response.get("location", ""),
        "email": response.get("email", ""),
        "hireable": response.get("hireable", ""),
        "bio": response.get("bio", ""),
        "public_repos": response.get("public_repos", ""),
        "followers": response.get("followers", ""),
        "following": response.get("following", ""),
        "created_at": response.get("created_at", "")
    }

def fetch_user_details(login):
    url = f"https://api.github.com/users/{login}"
    response = requests.get(url, headers=HEADERS).json()
    time.sleep(1)  # To respect GitHub rate limits
    return {
        "login": response.get("login", ""),
        "name": response.get("name", ""),
        "company": clean_company(response.get("company", "")),
        "location": response.get("location", ""),
        "email": response.get("email", ""),
        "hireable": str(response.get("hireable", "")).lower(),  # Convert to lowercase
        "bio": response.get("bio", ""),
        "public_repos": response.get("public_repos", ""),
        "followers": response.get("followers", ""),
        "following": response.get("following", ""),
        "created_at": response.get("created_at", "")
    }

def fetch_user_repos(login):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{login}/repos?sort=pushed&per_page=100&page={page}"
        response = requests.get(url, headers=HEADERS).json()
        if not response or page > 5:  # Stop after 500 repos or no repos left
            break
        for repo in response:
            # Check if license exists before accessing 'key'
            license_key = repo.get("license").get("key", "") if repo.get("license") else ""
            repos.append({
                "login": login,
                "full_name": repo.get("full_name", ""),
                "created_at": repo.get("created_at", ""),
                "stargazers_count": repo.get("stargazers_count", 0),
                "watchers_count": repo.get("watchers_count", 0),
                "language": repo.get("language", ""),
                "has_projects": str(repo.get("has_projects", False)).lower(),  # Convert to lowercase
                "has_wiki": str(repo.get("has_wiki", False)).lower(),          # Convert to lowercase
                "license_name": license_key
            })
        page += 1
    return repos

def clean_company(company):
    company = company.strip() if company else ""
    if company.startswith("@"):
        company = company[1:]
    return company.upper()

def main():
    users_data, repos_data = [], []
    users = fetch_users()

    print(f"Found {len(users)} users in Delhi with more than 100 followers.")
    for idx, user in enumerate(users, start=1):
        print(f"Processing user {idx}/{len(users)}: {user['login']}")
        user_details = fetch_user_details(user['login'])
        users_data.append(user_details)
        user_repos = fetch_user_repos(user['login'])
        repos_data.extend(user_repos)

    # Create CSV files
    users_df = pd.DataFrame(users_data)
    repos_df = pd.DataFrame(repos_data)

    # Save CSV files
    users_df.to_csv("users.csv", index=False)
    repos_df.to_csv("repositories.csv", index=False)
    print("Data saved to users.csv and repositories.csv")

if __name__ == "__main__":
    main()

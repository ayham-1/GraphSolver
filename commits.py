import requests


def get_user_info():
    URL = "https://api.github.com/repos/realaltffour/GraphSolver/contributors"
    r = requests.get(URL)
    r = r.json()

    for contributor in r:
        get_user_commits(contributor['login'], contributor['url'])

def get_user_commits(login, github_profile):
    URL = "https://api.github.com/repos/realaltffour/GraphSolver/commits"
    # Filter by login
    r = requests.get(URL, {'author':login})
    r = r.json()
    
    with open('CONTRIBUTORS.md', 'a') as contributor_file:
        counter = 0
        for commits_by_user in r:
            counter += 1
        contributor_file.write(f"<br/>{login}, [Profile]({github_profile}). Made {counter} commits. <br/>")

    contributor_file.close()

get_user_info()

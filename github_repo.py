import requests
import json
import sys

username = str(sys.argv[1])

github_url = 'https://api.github.com'


def github():
    r = requests.get(url=github_url + '/users/' + username)
    result = json.loads(r.text)
    print(result)
    print(result.get('login'))
    fileUpdate(result)


def fileUpdate(info):
    print(info.get('avatar_url'))
    with open(file='user.md', mode='r') as fr:
        content = fr.read()
        print(content)
        print(type(content))
        handler = content.format(
            avatar_url=info.get('avatar_url'),
            username=info.get('login'),
            html_url=info.get('html_url'),
            public_repos=info.get('public_repos'), )
        fw = open('user_re.md', 'w+')
        fw.write(handler)
        fw.flush()
        fw.close()
        fr.close()
        print(handler)


if __name__ == '__main__':
    headers = {}
    query = {
        'type': 'owner',
        'sort': 'full_name'
    }
    # r = requests.request('get', base_url + github_api_default)
    # r = requests.request('get', base_url + github_api_repo, params=query)
    github()

import sys
import os
import re
import json
import urllib.request
import urllib.error

cmd = lambda x: f'git log -1 --pretty=oneline {x}'
performance_ptrn = re.compile(r'Time:[^-]*')
title_ptrn = re.compile(r'[^\[\]]+')

git_diff = 'git_diff.txt'

def main(cookie):
    if not os.path.exists(git_diff):
        return
    
    with open(git_diff, 'r', encoding='utf-8') as f:
        paths = ''.join(f.readlines()).strip().split(' ')
        dirname = os.path.dirname(paths[0])
        platform = dirname.split('/')[0]
    file_names = os.listdir(dirname)
    files = {}

    for file_name in file_names:
        file_path = f'{dirname}/{file_name}'        
        with open(file_path, 'r', encoding='utf-8') as f:
            files[file_name] = f.readlines()
    
    README = files.pop('README.md')
    title, problem_link = map(lambda x: x.strip(), (README[0], README[2]))
    title = f'[{platform}]{title[2:]}' 
  
    content = f'{problem_link}\n\n'

    performance = ''
    for file_name, lines in files.items():
        extension = file_name.split('.')[-1]
        file_path = f'{dirname}/{file_name}'
        performance = performance_ptrn.findall(os.popen(cmd(file_path)).read())[0]
        code = ''.join(lines)

        content += f'### .{extension}\n\n'
        content += f'{performance}\n\n'
        content += f'```{extension}\n{code}\n```\n\n'

    post = f'# {title}\n\n{content}'

    post_path = 'posts'
    tokens = title_ptrn.findall(title)
    for token in tokens:
        post_path += f'/{token}'
    
    post_markdown_path = f'{post_path}.md'
    post_json_path = f'{post_path}.json'
    post_dirname = os.path.dirname(post_json_path)

    if not os.path.exists(post_dirname):
        os.makedirs(post_dirname)

    with open(post_markdown_path, 'w', encoding='utf-8') as f:
        f.writelines(post)

    with open('WritePost.json', 'r', encoding='utf-8') as f:
        writePost = json.load(f)
    
    is_private = True
    url_slug = ''.join(char if char not in r'''!*'();:@&=+$,/?#[]%"<>\\{}|^~`''' else '-' for char in title[1:]).replace(' ', '-')

    variables = {'body': content,
        'is_markdown': True,
        'is_private': is_private,
        'is_temp': False,
        'meta': {
            'short_description': f'{title} {performance}'
        },
        'series_id': None,
        'tags': ['알고리즘 문제풀이', tokens[0]],
        'thumbnail': None,
        'title': title,
        'token': None,
        'url_slug': url_slug
    }

    writePost['variables'] = variables
    writePost.pop('operationType')
    writePost.pop('variablesSchema')

    with open(post_json_path, 'w', encoding='utf-8') as f:
        json.dump(writePost, f)

    with open('headers.json', 'r', encoding='utf-8') as f:
        headers = json.load(f)
        headers['cookie'] = cookie

    try:
        data = json.dumps(writePost).encode('utf-8')
        req = urllib.request.Request('https://v2.velog.io/graphql', data=data, method='POST', headers=headers)
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            print(json.loads(response_data))
    except urllib.error.URLError as e:
        print(e)

if __name__ == '__main__':
    main(sys.argv[1])
git config --global core.quotepath False;
if [[ $(echo $(git log -1 --pretty=oneline | awk -F '-' '{print $NF}' )) == 'BaekjoonHub' ]]; then 
    echo $(git diff --color --name-only HEAD~1 HEAD~0 ) > git_diff.txt
    python main.py "$1"
    git add posts
    git commit -m "add post: $(echo $(git diff --name-only --cached) | sed 's/[^\/]*\///' | sed 's/\.json[^\n]*$//')"
    git push
fi

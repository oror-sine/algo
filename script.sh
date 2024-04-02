git config --global core.quotepath False;
if [[ $(echo $(git log -1 --pretty=oneline | cut -d '-' -f 2 )) == 'BaekjoonHub' ]]; then 
    echo $(git diff --color --name-only HEAD~1 HEAD~0 ) > git_diff.txt;
fi
# `Pygithub ImportError`

### `Description`
`This error frequently when improperly installing the github API. Most often, users will install the library github rather than the library pygithub.`

### `Problem`
```
Traceback (most recent call last):
  File "/Users/highlander/Desktop/Project-Heimir/main.py", line 5, in <module>
    from github import Github
ImportError: cannot import name 'Github' from 'github'
```

### `Solution`
```
pip3 uninstall github
pip3 uninstall pygithub

pip3 install pygithub
```

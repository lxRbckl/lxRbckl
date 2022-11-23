### `Problem`
```
Traceback (most recent call last):
  File "/Users/highlander/Desktop/Project-Heimir/main.py", line 5, in <module>
    from github import Github
ImportError: cannot import name 'Github' from 'github' (/Users/highlander/Desktop/Project-Heimir/venv/lib/python3.10/site-packages/github/__init__.py)
```

### `Solution`
```
python -m pip install pygithub
```

### `Resources`
[PyGithub/issues/#856](https://github.com/PyGithub/PyGithub/issues/856#issuecomment-421110639) [`https://stackoverflow.com/a/50821379`](https://stackoverflow.com/a/50821379) [pythonpool.com/python-m-flag/](https://www.pythonpool.com/python-m-flag/)

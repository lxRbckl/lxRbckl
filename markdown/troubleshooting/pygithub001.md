# `Pygithub ImportError`

### `Description`
`The following error occurs most often in virtual environments. This error occurs when your interpreter cannot find a
package. The command in the traling box ensures that the package you are installing is tied to the pip installer used
with the executable Python file. The final box contains all the related resources I used to find the solution to this
problem.`

### `Problem`
```
Traceback (most recent call last):
  File "/Users/highlander/Desktop/Project-Heimir/main.py", line 5, in <module>
    from github import Github
ImportError: cannot import name 'Github' from 'github' (/Users/highlander/Desktop/Project-Heimir/venv/lib/python3.10/site-packages/github/__init__.py)
```

### `Solution`
```
pip3 uninstall github
pip3 uninstall pygithub

pip3 install pygithub
```

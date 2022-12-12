# `Pygithub ImportError`

#### `Description`
The following error occurs most often in virtual environments. This error occurs when your interpreter cannot find a
package. The command in the traling box ensures that the package you are installing is tied to the pip installer used
with the executable Python file. The final box contains all the related resources I used to find the solution to this
problem.

#### `Problem`
```
Traceback (most recent call last):
  File "/Users/highlander/Desktop/Project-Heimir/main.py", line 5, in <module>
    from github import Github
ImportError: cannot import name 'Github' from 'github' (/Users/highlander/Desktop/Project-Heimir/venv/lib/python3.10/site-packages/github/__init__.py)
```

#### `Solution`
```
python3 -m pip install pygithub
```

#### `Resources`
#### `1. `[`PyGithub/issues/#856`](https://github.com/PyGithub/PyGithub/issues/856#issuecomment-421110639) `2. `[`https://stackoverflow.com/a/50821379`](https://stackoverflow.com/a/50821379) `3. `[`pythonpool.com/python-m-flag/`](https://www.pythonpool.com/python-m-flag/) `4. `[`appdividend.com/python-m-flag/`](https://appdividend.com/2022/06/15/python-m-flag/) `5. `[`pyquestions.com/meaning-of-python-m-flag`](https://pyquestions.com/meaning-of-python-m-flag)

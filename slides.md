---
marp: true
---

![bg left:40% 80%](images/python.png)

# Python Workshop

---

# What I learned by adding tests to `search-analytics`
 
- Use the right tools - Python is `batteries included`
- Virtualise the environment
- Structure the project - properly and consistently
- Test your code
- Use a code coverage tool
- Lint your code - not necessarily the tests

---

# Use the right tools

- `pyenv` - for Python and dependency versioning
- `venv` - the Python virtual environment
- `pip` - the Python package manager
- `unittest` - the test module that's included in the Python standard library
- `coverage` - a code coverage tool
- `pylint` - your code should conform to [PEP-8 - the Python Style Guide](https://peps.python.org/pep-0008) - this helps you keep it that way

---

# Getting setup

```shell
$ cd ~
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```
### For `bash`

```shell
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
$ cat .bashrc
```

```shell
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
$ echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
$ echo 'eval "$(pyenv init -)"' >> ~/.profile
$ cat .profile
```
---

# Getting setup

### For `zsh`

```shell
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

---

# Getting setup

```shell
$ exec "$SHELL"

$ pyenv install 3.11.1
$ pyenv global 3.11.1
$ pyenv versions

$ python --version
```

---

# Creating a project

$ mkdir <path_to_source_code>/python-workshop
$ cd <path_to_source_code>/python-workshop 
$ pyenv local 3.11.1 # creates a `.python-version` file
$ python rehash

$ touch requirements.txt
$ mkdir src 
$ mkdir test

---

# Virtual Environment

```shell
$ python -m venv venv
$ source venv/bin/activate
```

### To `deactivate` 

```shell
(venv) $ deactivate
```

---

# Add your dependencies

(venv) $ echo 'coverage' >> requirements.txt 
(venv) $ echo 'pylint' >> requirements.txt
(venv) $ pip install -r requirements.txt

---

![bg left:40% 80%](images/code.png)

# Time for some code

---

# test/test_string_utils.py

```python
import unittest

from src.string_utils import count

class TestStringUtils(unittest.TestCase):
  def test_count(self):
    self.assertEqual(count("Monty Python"), 12)
```

---

# Run the test

```shell
(venv) $ python -m unittest discover
```

You sould get some errors.

--- 

# src/string_utils.py

```python
def count(string):
  return len(string)
```

This is the code the tests are looking for!

---

# Run the tests again

```shell
(venv) $ python -m unittest discover
```

AND... Nothing!

```shell 

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```

What?

---

# Can you `discover` the clue?

We ran...

```shell
(venv) $ python -m unittest discover
```

The discover option on the end of that command means we need to tell Python where to find stuff.

To do that we need to create an empty file named `__init__.py` (that's double underscore either side of init).

```shell
(venv) $ touch test/__init__.py
```

---

# Let's try again

```shell
(venv) $ python -m unittest discover
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

SUCCESS!

---

# test/test_string_utils.py

```python

  def test_contains(self):
    self.assertEqual(contains("Monty", "Monty Python and the Holy Grail"), True)
    self.assertEqual(contains("Monty", "Star Wars"), False) 
```

# src/string_utils.py

```python
def contains(text, string):
  return text in string
```

---

# And test...

```shell
(venv) $ python -m unittest discover 
E.
======================================================================
ERROR: test_contains (test.test_string_utils.TestStringUtils.test_contains)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/gcl/code/python-workshop/test/test_string_utils.py", line 10, in test_contains
    self.assertEqual(contains("Monty", "Monty Python and the Holy Grail"), True)
                     ^^^^^^^^
NameError: name 'contains' is not defined

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (errors=1)
```

It's trying to tell us that it can't find the `contains` method.

---

# So, we'll tell it where to find it 

Update `test/test_string_utils.py`...


```python
from src.string_utils import count, contains
```

Now that's fixed we can try again...

```shell
(venv) $ python -m unittest discover 
```

---

# It'd be nice about now to see how much code coverage we have

```shell 
(venv) $ coverage run -m unittest discover
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

Uh! That it?

---

# Turns out coverage needs two commands

One to produce the data, and one to produce the report. I know, don't blame me!!!

```shell
(venv) $ coverage report -m
```

---

# As for linting


```shell 
(venv) $ pylint --recursive=y ./src ./test
```

And you should see a bunch of warnings and errors with references which bit of the code to fix.

But, I know what you're thinking - an we auto fix these issues right?

Kinda... partly, yes...

---

# But, we need another tool

Remember PEP-8? Here's a tool that make sure your code complies to PEP-8.

```shell
(venv) $ echo 'autopep8' >> requirements.txt
(venv) $ pip install -r requirements.txt
(venv) $ pyenv rehash
(venv) $ autopep8 --in-place --aggressive --aggressive src/*.py test/*.py
```

So, what did it fix?

```shell
(venv) $ pylint --recursive=y ./src ./test
```

---

# Now, I don't know about you...

I find these commands a tad ... spammy. 

But, we can fix that. 

How about some `aliases`?

```shell
alias py-up='source venv/bin/activate'
alias py-down='deactivate'
alias py-bundle='pip install -r requirements.txt'
alias py-test='python -m unittest discover'
alias py-cov='coverage run -m unittest discover && coverage report -m'
alias py-cop='pylint --recursive=y ./src ./test'
```

Add these to your `.bashrc` or `.zshrc` file and relax.

---

# TODO

Add section on py debugger
Add API mock example
Add exercise

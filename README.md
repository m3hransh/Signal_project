This is a simple Signal and System project for implementing some basic concepts and examples in Python programming language.
## Installation
Make sure to have python3 installed in your machine.
then install this package by pip or simply use Anaconda. this is how you can install them with pip:
``` bash
$pip install matplotlib
$pip install numpy
$pip install scipy
```

## Project structure
The codes for each question are in .py file with name of the question (e.g Q1.py).
In the doc/ folder you can find my report in latex and pdf format of that is also available.
The script.py is a script for transfering and copying sections that I specified in python files of question into speretate file in the directory of /doc/codes to reffering to those section in my document.To use that you just run this command against a python file, as an example consider this:
``` bash
$python script.py Q1.py
```
that will find codes between #section:<name> and #endsection and create a file <name>.py file in doc/codes folder.
  
## Runing codes
I have saved graphs in .pgf format in doc/images dir. For runing and seeing graphs in defferent backend use the code below at top of the python scripts to spcify your backend:
```python
import matplotlib
matplotlib.use('<your_backend>')
```
if you don't know what I am talking about, click [here](https://matplotlib.org/faq/usage_faq.html) for more information.

# Egypts tech scene salaries
Scrapping data from vacancies & career opportunities website

## Table of Content
- [Egypts tech scene salaries](#egypts-tech-scene-salaries)
  * [Tools](#tools)
  * [How to run](#how-to-run)
  * [URL](#URL)
  * [Author](#author)

## Tools
1. Python
2. Beautiful Soup
3. Streamlit


## How to run
* Enter the directory where the script is located then type the following to the console
```sh
$ git clone https://github.com/sherif-abdallah/web-scraping-wuzzuf web-scraping-wuzzuf
```

* Install Python 3.8 venv, pip and compiler
```sh
$ sudo apt-get install python3.8 python3.8-venv python3-venv
```

* Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.8 -m venv venv
$ source venv/bin/activate
```

* Then install the dependencies:

```sh
(venv)$ cd web-scraping-wuzzuf
(venv)$ python -m pip install --upgrade pip
(venv)$ python -m pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.


* Finally run The App:
```sh
(venv)$ python -m streamlit run main.py
```
* And navigate to `http://127.0.0.1:8501`.


## URL
* You can also navigate to the main website without needing to install python, you can navigate it from [here](https://share.streamlit.io/sherif-abdallah/web-scraping-wuzzuf/main/main.py)

## Author
[Sherif Abdullah](https://github.com/sherif-abdallah)

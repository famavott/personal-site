# Personal Website
---
### Description

Personal portfolio site to showcase skills and projects.

### Authors
---
* [famavott](https://github.com/famavott/personal-site)

### Dependencies
---
* flask

### Getting Started
---
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository. To accomplish this, execute these commands:

`$ git clone https://github.com/famavott/personal-site.git`

`$ cd personal-site`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment named "ENV", and install the project requirements into your VE.

`$ python3 -m venv ENV`

`$ source ENV/bin/activate`

`$ pip install -r requirements.txt`
##### *Serving Locally*
Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command from your terminal, on the same level as `run.py`.
`$ flask run`
Once you have executed this command open your browser, and go to `locahost:5000/`.

### URLs
---
The URLS for this project can be found in the following modules:

| URL module | Description |
|:---:|:---:|
| ./app/routes.py | Routes for personal portfolio site. |

### Development Tools
---
* *python* - programming language
* *flask* - web framework

### License
---
This project is licensed under MIT License - see the LICENSE.md file for details.

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*

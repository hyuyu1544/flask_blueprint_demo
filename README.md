# Flask Blueprint Demo
An Demo for flask blueprint. 


## Set Up

1. Clone the repository: `git clone https://github.com/hyuyu1544/flask_blueprint_demo.git`

2. Prepare you develop environ. (e.g.`venv`,`pyenv`)

3. Install `pkg` the app needs `pip install -r requirements.txt` 

4. Run flask app server: `python -m server`

5. Go check on browser:
```
http://127.0.0.1:5000/blueprint1/blueprint1_api
http://127.0.0.1:5000/blueprint2/blueprint2_api
```

## The Tree
```
flask_blueprint_demo
├── README.md
├── requirements.txt
└── server
    ├── __init__.py
    ├── __main__.py
    ├── app.py
    ├── blueprint1
    │   ├── __init__.py
    │   └── view
    │       ├── __init__.py
    │       └── blueprint1_api.py
    └── blueprint2
        ├── __init__.py
        └── view
            ├── __init__.py
            └── blueprint2_api.py
```

#### app.py
The main application is defination here. Developer can add many blueprint here by using `register_blueprint`, and using `url_prefix` to setting blueprint prefix url.

#### blueprint1/__init__.py
Blueprint route here. 

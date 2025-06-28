### To Create a virtual environment
- First install virtualenv
```
pip install virtualenv
```

- To create named as env
```
virtualenv env
```

- To Activate the given environment
```
.\env\Scripts\activate
```

# Install Flask
```
pip install flask
```

- Import Flask
```
from flask import Flask
```

- Create an app
```
app=Flask(__name__)
```

- Create a route and render something
```
@app.route("/")
def homepage():
    return "<p>Hello, World</p>"
```

- To start the server
```
if __name__=="__main__":
    app.run(debug=True,port=3000)
```

- This will start the given **app.py** on localhost server on port 3000


## To render a HTML page
- Create 2 folders on named as **Static** and **Templates**
- Put static files like audio, video, css, js in Static Folder
- Put HTML files in Templates folder
- Render the given HTML File
```
from flask import Flask, render_template
...
@app.route("/")
def homepage():
    return render_template("index.html")
```
- This will render **index.html** file from the given **templates** folder

## To create a sqlite database and models in it
- First Install SQLAlchemy for Flask
```
pip install flask-sqlalchemy
```

- Config the database in app and then create the model
```
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"

db=SQLAlchemy(app)

class Todo(db.Model):
    # Class Variables
    sno=db.Column(db.Integer,primary_key=True)
    todoTitle=db.Column(db.String(200),nullable=False)
    todoDescription=db.Column(db.String(400),nullable=False)
    dateTime=db.Column(db.DateTime,default=datetime.datetime.now)

    def __repr__(self):
        return f"{self.todoTitle} - {self.todoDescription}"
```

- To create this model, add the below code
```
with app.app_context():
    db.create_all()
```

## To fetch the records from the database
```
todos=Todo.query.all()
return render_template("index.html",todos=todos)
```
- Then print there using jinja templates

- I we have used the following method
```
db.session.execute(db.select(Todo))
```
- Then use the jinja templates as following
```
{% for todo in todos %}    
    <tr>
        <th scope="row">{{todo[0].sno}}</th>
        <td>{{todo[0].todoTitle}}</td>
        <td>{{todo[0].todoDescription}}</td>
        <td>{{todo[0].dateTime}}</td>
    </tr>                    
{% endfor %}
```

- Else use below code
```
{% for todo in todos %}    
    <tr>
        <th scope="row">{{todo.sno}}</th>
        <td>{{todo.todoTitle}}</td>
        <td>{{todo.todoDescription}}</td>
        <td>{{todo.dateTime}}</td>
    </tr>                    
{% endfor %}
```

## For Jinja2 Snippets
- Install **Jinja2 Snippets Kit** Extension
- Write snippets by writing 'j' before keywords like 'if', 'for' and write like - 'jif', 'jfor' for snippets
- '|' -> apply this kind of 'filter' in jinja if required

## Redirect to the other route
```
return redirect("/")
```

## To Find any instance from a url - Dynamic Routing
```
@app.route("/delete/<int:sno>")
def deleteTask(sno):
    pass
```
- And then pass the parameter to the given function


# Use Template Inheritance for better page renders

# Read the Documentation well.

from flask import Flask, render_template, request, redirect
# from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

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

@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        task=request.form['task']
        taskDesc=request.form['taskDesc']
        todo=Todo(todoTitle=task,todoDescription=taskDesc)
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    # todos=list(db.session.execute(db.select(Todo)))
    # print(list(todos))
    todos=Todo.query.all()
    
    return render_template("index.html",todos=todos)

# @app.route("/products")
# def products():
#     return "<h1>This is a Product Page</h1>"

@app.route("/delete/<int:sno>")
def deleteTask(sno):
    deleteTodo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(deleteTodo)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>", methods=["GET","POST"])
def updateTask(sno):
    if request.method=="POST":
        task=request.form['task']
        taskDesc=request.form['taskDesc']
        todo=Todo.query.filter_by(sno=sno).first()
        todo.todoTitle=task
        todo.todoDescription=taskDesc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    updateTodo=Todo.query.filter_by(sno=sno).first()
    return render_template("/update.html",todo=updateTodo)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True,port=3000)
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from scraper import Bookscrape

test = Bookscrape()
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
    
@app.route('/scrape', methods=['POST', 'GET'])
def scrape():
    test.scrape_books()
    return redirect(url_for('index'))

@app.route('/showbooks', methods=['POST', 'GET'])
def showBooks():
    # print(test.all_books)
    book_1 = test.all_books[0]
    print(book_1)
    return render_template('index.html', book_1=book_1)
    
    
    
    
 
@app.route('/quit', methods=['POST', 'GET'])
def quit():
    test.quit()
    return redirect(url_for('index'))   
    
    
if __name__ == "__main__":
    app.run(debug=True)
    test = Bookscrape()   
    
    
    
    
    # for book in test.all_books:
    #     book_title = book['title']
    # return render_template('index.html', book=book)

    # print(book['title'])
    # book_title = test.all_books[book]['title']
    # print(book_title)
    #return render_template('index.html', book=book)
    # return redirect(url_for('index' book=book))
    


    
    



# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         task_content = request.form['content']
#         new_task = Todo(content=task_content)

#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue adding your task'

#     else:
#         tasks = Todo.query.order_by(Todo.date_created).all()
#         return render_template('index.html', tasks=tasks)


# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)

#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that task'

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)

#     if request.method == 'POST':
#         task.content = request.form['content']
#         task.price = request.form['price']

#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue updating your task'

#     else:
#         return render_template('update.html', task=task)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<book %r>' % self.id


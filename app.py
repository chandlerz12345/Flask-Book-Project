from flask import Flask, render_template, url_for, request, redirect
from scraper import Bookscrape

book_scrap = Bookscrape()
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
    
@app.route('/scrape', methods=['POST', 'GET'])
def scrape():
    book_scrap.scrape_books()
    return render_template('items.html', content = book_scrap.data)
    
@app.route('/items')
def items():
    return render_template('items.html', content = book_scrap.data)


@app.route('/search<title>', methods=['POST', 'GET'])
def search(title):
    return render_template('search.html', content = book_scrap.data, title=title)
   

@app.route('/update')
def update():
    book_scrap.update_availabilty()
    book_scrap.update_price()
    book_scrap.update_title()
    return render_template('items.html', content = book_scrap.data)
    
 
@app.route('/quit', methods=['POST', 'GET'])
def quit():
    book_scrap.quit()
    return redirect(url_for('index'))   
    
    
if __name__ == "__main__":
    app.run(debug=True)
     
    

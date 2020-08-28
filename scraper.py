import requests
from bs4 import BeautifulSoup
from time import sleep
import sys
import boto3
import json

class Bookscrape:
    def __init__(self):
        self.save_s3 = AWSConnect()
        self.base_url = "http://books.toscrape.com/catalogue/page-{}.html"
        self.all_books = []
        self.read()
        
        

    def scrape_books(self):

        for n in range(1,51):
            self.scrap_url = self.base_url.format(n)
            print(f"scrapping page {n} of website")
            # sleep(1)
            self.response = requests.get(self.scrap_url)


            self.soup = BeautifulSoup(self.response.text, "html.parser")


            self.books = self.soup.find_all(class_ = "product_pod")

            for self.book in self.books:

                self.all_books.append({
                    # 'title': book.find('img', alt = True),
                    'title': self.book.find('img')['alt'].lower(),
                    "price": self.book.find(class_ = "price_color").get_text(),
                    "availability": self.book.find(class_ = "instock").get_text()

                }
                )

            # sleep(1)
        # self.read()
        all_books = self.all_books
        self.save_json(all_books)
        self.read()



    def search(self):
        self.to_search = input("what is the title of the item you would like to search: ").lower()
        for self.book in self.data:
            if self.book['title'] == self.to_search:
                print(self.book['title'])
                print(f"the price of the book if {self.book['price']}")
                print(f"the item is currently {self.book['availability']}")
            
            


    def delete(self):
        self.counter = 0
        self.to_search = input("what is the title of the item you would like to  delete: ").lower()
        for self.book in self.data:
            if self.book['title'] == self.to_search:
                self.book.clear()
                print("the book listing has been removed")
            else:
                self.counter +=1




    def update_price(self):
        self.counter = 0
        self.search = input("what is the item would you like to update: ").lower() 
        for self.book in self.data:
            if self.book['title'] == self.search:
                print(f"the current price of the item is {self.book['price']}")
                self.new_price = input("what is the new price of the item: ")
                self.book['price'] = self.new_price
                print (self.data[self.counter])
            else:
                self.counter += 1
            

    def update_title(self):
        self.counter = 0
        self.search = input("what is the item would you like to update: ").lower() 
        for self.book in self.data:
            if self.book['title'] == self.search:
                print(f"the current title of the item is {self.book['title']}")
                self.new_title = input("what is the new title of the item: ")
                self.book['title'] = self.new_title
                print (self.data[self.counter])
            else:
                self.counter += 1


    def update_availabilty(self):
        self.counter = 0
        self.search = input("what is the item would you like to update: ").lower() 
        for self.book in self.data:
            if self.book['title'] == self.search:
                print(f"the current availability of the item is {self.book['availability']}")
                self.new_availability = input("what is the new availability of the item: ")
                self.book['availability'] = self.new_availability
                print (self.data[self.counter])
            else:
                self.counter += 1


    def save_json(self, all_books):
        with open('app.json', "w") as fp:
            json.dump(all_books, fp)

    def quit(self):
        all_books = self.data
        self.save_json(all_books)
        self.save_s3.save2s3()
        # sys.exit(0)
        
    def read(self):
        with open('app.json') as json_file:
           self.data = json.load(json_file)
           
        

class AWSConnect:
        def __init__(self):
            self.s3 = boto3.client('s3')
        def save2s3(self):
            self.s3.upload_file('app.json', 'lmtd-team-delta','AWSave.json')
           




# test = Bookscrape()
# test.scrape_books()

# test.search()
# test.quit()

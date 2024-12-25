from fastapi import FastAPI, Body
from book import Book
from pydantic import BaseModel,Field

class BookRequest(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    category: str = Field(min_length=1)
    description: str = Field(min_length=1,max_length=50)




books = [
    Book(1, "book1", "author1", "science","book1 description"),
    Book(2, "book2", "author2", "math","book2 description"),
    Book(3, "book3", "author3", "english","book3 description"),
    Book(4, "book4", "author4", "fiction","book4 description"),
    Book(5, "book5", "author5", "science","book5 description"),
]

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books")
async def get_books():
    return {"books": books}

@app.post("/books/create")
async def create_book(book:BookRequest):
    payload = Book(**book.model_dump())
    books.append(payload)
    return {"message": "Book created","book":payload}

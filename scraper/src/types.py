from dataclasses import dataclass

@dataclass
class BookItem:
    title: str
    price: str
    availability: str
    rating: str
    category: str
    url: str

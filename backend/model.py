from pydantic import BaseModel
from typing import List
class CartItem(BaseModel):
    product_id: int
    quantity: int

class CheckoutItem(BaseModel):
    user_id: int
    discount_code: str = None

class ProductDetails(BaseModel):
    product_id: int
    price: float
    description: str
    reviews: List[str]

class FilterParams(BaseModel):
    category: str = None
    min_price: float = None
    max_price: float = None
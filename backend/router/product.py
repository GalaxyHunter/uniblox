from fastapi import APIRouter, HTTPException
from typing import List
from model import ProductDetails, FilterParams, ProductCreate
from database import conn, cursor

router = APIRouter(tags=["Product"])

# Endpoint to add a new product to the store

@router.post("/add-product/", response_model=ProductDetails)
async def add_product(product: ProductCreate):
    # Add the new product to your database
    cursor.execute("SELECT * FROM products WHERE name = ?", (product.name,))
    existing_product = cursor.fetchone()

    if existing_product:
        raise HTTPException(status_code=400, detail="Product with the same name already exists")

    cursor.execute("INSERT INTO products (name, price, description, category, reviews) VALUES (?, ?, ?, ?, ?)",
                   (product.name, product.price, product.description, product.category, ""))
    conn.commit()
    
    # Fetch the added product for confirmation
    cursor.execute("SELECT * FROM products WHERE name = ?", (product.name,))
    product_data = cursor.fetchone()

    if not product_data:
        raise HTTPException(status_code=500, detail="Product could not be added")

    # Convert product data to ProductDetails model
    added_product = {
        "product_id": product_data[0],
        "name": product_data[1],
        "price": product_data[2],
        "description": product_data[3],
        "reviews": product_data[4].split(';')
    }
    return added_product

# Endpoint to retrieve product details by product_id
@router.get("/product/{product_id}", response_model=ProductDetails)
async def get_product_details(product_id: int):
    cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
    product_data = cursor.fetchone()
    if not product_data:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_details = {
        "product_id": product_data[0],
        "name": product_data[1],
        "price": product_data[2],
        "description": product_data[3],
        "category": product_data[4],
        "reviews": product_data[5].split(';')  # Assuming reviews are semicolon-separated
    }
    return product_details

# Endpoint for searching and filtering products
@router.get("/search")
async def search_and_filter_products(
    category: str = None,
    min_price: float = None,
    max_price: float = None,
):
    query = "SELECT * FROM products WHERE 1"
    query_params = []

    if category:
        query += " AND category = ?"
        query_params.append(category)

    if min_price is not None:
        query += " AND price >= ?"
        query_params.append(min_price)

    if max_price is not None:
        query += " AND price <= ?"
        query_params.append(max_price)

    cursor.execute(query, tuple(query_params))
    products = cursor.fetchall()

    product_details_list = []
    for product_data in products:
        product_details = {
        "product_id": product_data[0],
        "name": product_data[1],
        "price": product_data[2],
        "description": product_data[3],
        "category": product_data[4],
        "reviews": product_data[5].split(';')  # Assuming reviews are semicolon-separated
    }
        product_details_list.append(product_details)

    return product_details_list


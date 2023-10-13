from fastapi import FastAPI
from router import cart, checkout, admin, statistics

app = FastAPI()

app.include_router(cart.router)
app.include_router(checkout.router)
app.include_router(admin.router)
app.include_router(statistics.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
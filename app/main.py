from fastapi import FastAPI
from app.routers import products, recommend
from app.database import Base, engine
from app import models

app = FastAPI(title="Product Recommender API")

app.include_router(products.router, prefix="/products")
app.include_router(recommend.router, prefix="/recommendations")



Base.metadata.create_all(bind=engine)

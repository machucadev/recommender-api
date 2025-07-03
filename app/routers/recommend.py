from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Product
from app.schemas import RecommendationRequest, RecommendationResponse, ProductOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RecommendationResponse)
def recommend_products(request: RecommendationRequest, db: Session = Depends(get_db)):
    if not request.product_ids:
        return {"recommended": []}
    input_products = db.query(Product).filter(Product.id.in_(request.product_ids)).all()
    categories = {p.category for p in input_products}
    recommendations = (
        db.query(Product)
        .filter(Product.category.in_(categories), ~Product.id.in_(request.product_ids))
        .limit(5)
        .all()
    )
    return {"recommended": recommendations}

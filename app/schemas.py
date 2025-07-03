from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    category: str
    description: str

class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True

class RecommendationRequest(BaseModel):
    product_ids: list[int]

class RecommendationResponse(BaseModel):
    recommended: list[ProductOut]

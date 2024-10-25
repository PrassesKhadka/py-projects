# the default encoding for MongoDB IDs 
from beanie import PydanticObjectId
from fastapi import APIRouter,HTTPException
from typing import List

from app.server.model import ProductReview,UpdateProductReview

#
router=APIRouter()

@router.post("/",response_description="Review added to the database")
async def add_product_review(review:ProductReview)->dict:
    await review.create()
    return {"message":"Review added successfully"}

@router.get("/{id}",response_description="Review record retrieved")
async def get_review_record(id:PydanticObjectId)->ProductReview:
    review=await ProductReview.get(id)
    return review

@router.get("/",response_description="Review records retrieved")
async def get_reviews()->List[ProductReview]:
    # .to_list() method is appended so the results are returned in a list
    reviews=await ProductReview.find_all().to_list()
    return reviews

@router.get("/{rating}",response_description="Review record with the specified rating retrieved")
async def get_review_with_rating(rating:float)->ProductReview:
    review=await ProductReview.find_one(ProductReview.rating==rating)
    return review 


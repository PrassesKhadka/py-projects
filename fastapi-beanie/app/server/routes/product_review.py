from fastapi import APIRouter,HTTPException
# the default encoding for MongoDB IDs 
from beanie import PydanticObjectId
from typing import List

from server.model import ProductReview,UpdateProductReview

# Controllers
# using router instead of app.get() for modularity 
router=APIRouter()

# The @ is known as decorators in python 
@router.post("/",response_description="Review added to the database")
async def add_product_review(review:ProductReview)->dict:
    await review.create()
    return {"message":"Review added successfully"}

# the function parameters will be called as Query Parameters, you can make it optional using Optional[] pydantic annotation 
@router.get("/{id}",response_description="Review record retrieved")
async def get_review_record(id:PydanticObjectId)->ProductReview:
    review=await ProductReview.get(id)
    return review

@router.get("/",response_description="Review records retrieved")
async def get_reviews()->List[ProductReview]:
    # .to_list() method is appended so the results are returned in a list
    reviews=await ProductReview.find_all().to_list()
    return reviews

# For optional-query-parameter use None as default
@router.get("/ratings/",response_description="Review record with the specified rating retrieved")
async def get_review_with_rating(rating:float|None=None)->List[ProductReview]:
    # review=await ProductReview.find_one(ProductReview.rating==4.9)
    if rating is None:
        rating=5.0

    review=await ProductReview.find_many(ProductReview.rating==rating).to_list()
    return review

@router.put("/{id}",response_description="Update review record")
async def put_review_to_record(id:PydanticObjectId,req:UpdateProductReview)->ProductReview:
    req={k:v for k,v in req.dict().items() if v is not None}
    update_query={
        "$set":{
            field:value for field,value in req.items() 
        }
    }

    review=await ProductReview.get(id)

    if review is None:
        raise HTTPException(status_code=404,detail="Review record not found")

    await review.update(update_query)
    return review


@router.delete("/{id}",response_description="Delete specified review record")
async def delete_review(id:PydanticObjectId)->dict:
    review=await ProductReview.find_one(ProductReview.id==id)

    if review is None:
        raise HTTPException(status_code=404,detail="Review record not found")

    await review.delete()
    return {"message":f"Successfully deleted {review.id}"} 
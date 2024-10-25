import datetime
from typing import Optional
from beanie import Document
from pydantic import BaseModel

"""
Document -> tuples/schema
Collection -> tables
How document will be stored in DB
"""
class TestDrivenArticle(Document):
    title:str
    content:str
    date:datetime
    author:str

    """
    To associate a collection,you need to add a Settings class as a subclass
    """
    class Settings:
        name="testdriven_collection"

class ProductReview(Document):
    name:str
    product:str
    rating:float
    review:str
    data:datetime=datetime.now()

    class Settings:
        name="product_review"

    class Config:
        schema_extra={
            "example":{
                "name":"Prasses",
                "product":"Football",
                "rating":4.9,
                "review":"Thikthak",
                "date":datetime.now()
            }
        }
    
class UpdateProductReview(BaseModel):
    name:Optional[str]
    product:Optional[str]
    rating:Optional[float]
    review:Optional[str]
    date:Optional[datetime] 

    class Config:
        schema_extra={
            "example":{
                "name":"Prasses",
                "product":"Cricket",
                "rating":5.0,
                "review":"Gazab",
                "date":datetime.now()
            }
        }
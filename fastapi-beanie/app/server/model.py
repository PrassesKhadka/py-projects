from datetime import datetime
from typing import Optional
from enum import Enum 
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


"""
Defining an enum
"""
class Statuses(str, Enum):
    DELETED = "DELETED"

"""
Settings -> collection to associate the schema/document with 
Config -> schema example in swagger-docs 
"""
class ProductReview(Document):
    name:str
    product:str
    rating:float
    review:str
    data:datetime=datetime.now()

    # to associate a collection
    class Settings:
        name="product_review"

    class Config:
        schema_extra={
            "example":{
                "name":"Prasses",
                "product":"Smartphone",
                "rating":4.9,
                "review":"Good!!!",
                "date":datetime.now()
            }
        }

# The Pydantic model that represents the data
# To be sent in body #BaseModel
class UpdateProductReview(BaseModel):
    name:Optional[str]
    product:Optional[str]
    rating:Optional[float]
    review:Optional[str]
    date:Optional[str]=datetime.now()

    class Config:
        schema_extra={
            "example":{
                "name":"Prasses",
                "product":"Book",
                "rating":5.0,
                "review":"Great!!!",
                "date":datetime.now()
            }
        }
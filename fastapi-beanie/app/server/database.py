from beanie import init_beanie
import motor.motor_asyncio

from app.server.model import ProductReview

async def init_db():
    client=motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017/productreviews"
    )
    # Params -> name of the database to be used, list of document models defined
    await init_beanie(database=client.db_name,document_models=ProductReview)


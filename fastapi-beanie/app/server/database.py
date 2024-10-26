from beanie import init_beanie
import motor.motor_asyncio

from server.model import ProductReview

# Initialise the Database
async def init_db():
    client=motor.motor_asyncio.AsyncIOMotorClient(
        # connection-url:
        # protocol://user_name:password@host:port/Database(optional)
        "mongodb://root:example@localhost:27017"
    )
    # database=client.get_database("beanie_example")
    # Params -> name of the database to be used, list of document models defined
    # The db_name-> will be the name of the database generated/or if already created then that will be used 
    await init_beanie(database=client.db_name,document_models=[ProductReview])

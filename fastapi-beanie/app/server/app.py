from contextlib import asynccontextmanager
from fastapi import FastAPI
from server.database import init_db
from server.routes.product_review import router as ProductReviewRouter

# write-code that should be executed before the application starts up. 
# This means that this code will be executed once, before the application starts receiving requests.
# more about lifespan-events on fast-api docs: https://fastapi.tiangolo.com/advanced/events/#lifespan
@asynccontextmanager
async def any_name_lifespan(app:FastAPI):
    # Load the ML models and as such jazz...
    # Here we initialise the Database
    print("Init lifespan")
    try:
        await init_db()
        print("Successfully connected to the MongoDB database")
    except Exception as e:
        print("Failed connection to MongoDB database: ",e)

    # code after yield runs after app shuts down -> #Required
    yield
    print("Clean up lifespan")

app=FastAPI(lifespan=any_name_lifespan)

# we can make api routes using just @app as well but
# routes/controllers for modularisation
# prefix -> route initial path
# tags -> group routes in the OpenAPI(Swagger)docs under a specific label
app.include_router(ProductReviewRouter,tags=["Product Reviews"],prefix="/reviews")

@app.get("/",tags=["Root"])
async def read_root()->dict:
    return {"message":"Welcome to beanie powered app!"}
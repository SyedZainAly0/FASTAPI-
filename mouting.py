from fastapi import FastAPI

# Main app
app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Welcome to the main app!"}

# Mounted app
blog_app = FastAPI()

@blog_app.get("/posts")
async def posts():
    return {"message": "These are blog posts"}

# Mount blog_app at path /blog
app.mount("/blog", blog_app)
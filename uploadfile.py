from typing import List, Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

# Single File Upload (Required)

@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    contents = await file.read() 
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(contents)
    }


# Single File Upload (Optional)

@app.post("/uploadfile/optional/")
async def upload_file_optional(file: UploadFile | None = None):
    if not file:
        return {"message": "No file uploaded"}
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(contents)
    }


# Multiple File Uploads

@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile]):
    file_infos = []
    for file in files:
        contents = await file.read()
        file_infos.append({
            "filename": file.filename,
            "content_type": file.content_type,
            "size_bytes": len(contents)
        })
    return {"files": file_infos}


# HTML Form to Test Uploads

@app.get("/")
async def main():
    content = """
    <html>
        <body>
            <h2>Single File Upload</h2>
            <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                <input type="file" name="file">
                <input type="submit">
            </form>

            <h2>Optional File Upload</h2>
            <form action="/uploadfile/optional/" enctype="multipart/form-data" method="post">
                <input type="file" name="file">
                <input type="submit">
            </form>

            <h2>Multiple Files Upload</h2>
            <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                <input type="file" name="files" multiple>
                <input type="submit">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=content)
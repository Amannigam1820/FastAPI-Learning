from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from pydantic import BaseModel


class schema1(BaseModel):
    Name:str
    Class:str
    Roll_No:int

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}


# path parameter

@app.get("/item/{item}")
def pathparams(item):
    var_name = {"heeelo": item}
    return {"Message":var_name}


# Query parameter

@app.get("/query")
def queryParams(name:str, roll_no:int):
    var_name = {"name" : name, "roll_no":roll_no}
    return (var_name)

    
@app.post("/items")
async def create_item(item:schema1):
    return item

 

# form data

@app.post("/form-data")
async def formData(username:str = Form(), password:str=Form()):
    return {"username":username, "Password":password}


# file upload
@app.post("/file")
async def file_bytes_length(file:bytes = File()):
    return ({"file":len(file)})



@app.post("/file/upload")
async def file_upload(file:UploadFile):
    return({"file":file})

###################################################################################################################################

@app.get("/error/handle")
async def handleError(item:int):
    if item==2:
        return HTTPException(status_code=400, detail="Item is not equal to 2, try another value")
    return {"value":item}
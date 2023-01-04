from fastapi import FastAPI, Path, Query, UploadFile, File
import shutil as st
from fastapi.responses import HTMLResponse
import speech_to_text as sp
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     nick_name: Optional[str] = None
#
# class UpdateItem(BaseModel):
#     name: Optional[str] = None
#     price: Optional[float] = None
#     nick_name: Optional[str] = None
#
# sp = {}

@app.post("/upload/")
async def root(file: UploadFile = File(...)):
    i=+1
    with open('file_'+str(i)+'.wav', 'wb') as buffer:
        st.copyfileobj(file.file, buffer)
        sp.stt(buffer)
    return {'file_name': file.file_name}


@app.get("/")
async def main():
    content = """
<body>
<h1>Chọn file Audio</h1>
<form action="/upload/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


# @app.get('/get-item/{item_id}/{name}')
# def get_item(item_id: int = Path(None, description='The ID of the item you would like to view: ', gt = 0)):
#     return sp[item_id]
#
# @app.get('/get-by-name')
# def get_item(name: str = Query(None, title='name', description='Name of item', max_length=10, min_length=2)):
#     for item_id in sp:
#         if sp[item_id].name == name:
#             return sp[item_id]
#     return {'Data': 'Not found'}
#
# @app.post('/create-item/{item_id}')
# def create_item(item_id: int, item: Item):
#     if item_id in sp:
#         return {'Error': 'Item ID already exists.'}
#     sp[item_id] = item
#     return sp[item_id]
#
# @app.put('/update-item/{item_id}')
# def update_item(item_id: int, item: UpdateItem):
#     if item_id not in sp:
#         return {'Error', 'Item ID does not exists'}
#     if item.name != None:
#         sp[item_id].name = item.name
#     if item.price != None:
#         sp[item_id].price = item.price
#     if item.nick_name != None:
#         sp[item_id].nick_name = item.nick_name
#     return sp[item_id]


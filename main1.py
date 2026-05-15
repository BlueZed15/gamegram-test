from fastapi import FastAPI,APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse, HTMLResponse
import json
from typing import Annotated
import uuid


app=FastAPI()
router=APIRouter(prefix="/test",tags=["bootstrap_testing"])
json_data=dict()


@router.post("/create")
#ellipsis ... means that you expect data
async def save_json(level_file: UploadFile = File(...),sandbox_id=Form(...),creator_id=Form(...)):
    global json_data
    json_data["game_id"]=str(1234)
    json_data["sandbox_id"],json_data["creator_id"]=sandbox_id,creator_id
    json_data["json_data"]=json.loads(level_file.file.read()) #converts bytes to dict
    return JSONResponse(json_data,status_code=200) #takes the dict as single json value for output


@router.get("/getjson")
def get_json(game_id=Form(...)):
    if game_id!=json_data["game_id"]:
        return HTMLResponse(content="Incorrect game_id",status_code=422)
    else:
        return JSONResponse(json_data["json_data"],status_code=200) if json_data else JSONResponse(status_code=500)

app.include_router(router)



#
#sandbox_id_param= func()
#level_id= <>


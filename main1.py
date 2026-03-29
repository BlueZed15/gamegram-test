from fastapi import FastAPI,APIRouter, File, UploadFile
from fastapi.responses import JSONResponse 
import json




app=FastAPI()
router=APIRouter(prefix="/test",tags=["bootstrap_testing"])
json_data=None

@router.post("/saveleveljson")
async def save_json(level_file: UploadFile = File(...)):
    global json_data
    json_data=json.loads(level_file.file.read())
    return JSONResponse(json_data,status_code=200)


@router.get("/getjson")
def get_json():
    return JSONResponse(json_data,status_code=200) if json_data else JSONResponse(status_code=500)

app.include_router(router)



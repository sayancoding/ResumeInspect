from fastapi import (FastAPI,
                     APIRouter, 
                     UploadFile,
                     File,
                     Body,
                     HTTPException)
from fastapi.responses import StreamingResponse

import os
import shutil
import logging

from core.AppFeature import AppFeature

app = FastAPI()
core = AppFeature()
router = APIRouter()

RESUME_DIR = 'data' # uploaded resume store path
os.makedirs(RESUME_DIR,exist_ok=True) # create that directory is not exist

@app.get("/api/welcome")
def welcome():
    return {'message' : 'Welcome to ResumeAI tools!!'}

@app.post("/api/uploadResume")
async def upload_resume(file : UploadFile = File(...)):
    """
    Upload resume 
    """
    if(file.content_type != "application/pdf"):
        raise HTTPException(status_code=400,detail="Only PDF files are allowed!")
    
    file_location  = os.path.join(RESUME_DIR, 'resume.pdf')
    
    try: 
        with open(file_location,"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
        logging.info("Resume is uploaded")

        await core.embedding_resume()
        logging.info("Resume is embedded and store at vectorStore")

        return {"message" : "Resume is uploaded & embedded successfully"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"{ex}")
    finally:
        file.file.close()

@app.post("/api/uploadJd")        
async def upload_jd(jd:str = Body(...)):
    """
    JD Upload 
    """
    await core.upload_jd(jd)
    logging.info("JD is embedded and store at vectorStore")

    return {"message" : "JD is embedded & store at vectorStore"}

@app.get("/api/matching")        
def match_resume_jd_trigger():
    """
    matching JD & resume 
    """
    logging.info("Analyzing Resume & JD...")
    res = core.matching_resume_jd()
    logging.info(res)
    return res

@router.get('/api/matchingJdResume')
def match_resume_jd():
    """
    matching JD & resume
    with SSE (Server Side Event) 
    """
    def event_generator():
        for log in core.matching_resume_jd():
            yield f"data: {log}\n\n"
    
    return StreamingResponse(event_generator(), media_type="text/event-stream")
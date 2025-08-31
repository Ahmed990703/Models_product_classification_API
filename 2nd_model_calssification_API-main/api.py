from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import io
import numpy as np
import os


app=FastAPI()
@app.post("/predict/")
async def predict(file : UploadFile=File(...)) :
    content= await file.read()
    image=Image.open(io.BytesIO(content))
    image.save("image.jpg")
    return{"message":"Image uploaded successfully"}
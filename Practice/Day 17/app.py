from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import os
import shutil
from rag import process_pdf, generate_answer
app = FastAPI(
    title="Day 17 RAG API",
    description="Upload PDF documents and ask questions using RAG",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Day 17 RAG API is running"
    }

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    try:

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        if os.path.getsize(file_path) == 0:
            os.remove(file_path)

            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        result = process_pdf(
            file_path,
            file.filename
        )

        return {
            "status": "success",
            "message": "PDF uploaded and processed successfully.",
            "file": result
        }

    except HTTPException:
        raise

    except Exception as e:

        if os.path.exists(file_path):
            os.remove(file_path)

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

from pydantic import BaseModel
from rag import generate_answer


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(request: QuestionRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:

        result = generate_answer(request.question)

        return {
            "status": "success",
            "question": request.question,
            "answer": result["answer"],
            "sources": result["sources"]
        }

    except Exception as e:

        print("ASK ERROR:", repr(e))

    raise HTTPException(
        status_code=500,
        detail=str(e)
    )
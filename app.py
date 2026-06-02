from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

from rag.load_embeddings import load_chunks, load_embeddings
from rag.retriever import retrieve
from rag.generator import generate_answer

app = FastAPI(title="EduMind AI Backend", version="1.0.0")

templates = Jinja2Templates(directory="templates")

# Global memory initialization for RAG vector elements
chunks = load_chunks()
embeddings = load_embeddings()


# --- Pydantic Data Verification Schemas ---

class QuestionRequest(BaseModel):
    question: str

class UserRegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


# --- Core Template View Routers (GET) ---

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/chatbot", response_class=HTMLResponse)
async def chatbot(request: Request):
    # In production, check for active session cookies here before rendering
    return templates.TemplateResponse("chatbot.html", {"request": request})


# --- Authentication Processing Endpoints (POST) ---

@app.post("/api/register")
async def handle_registration(user_data: UserRegisterRequest):
    """
    Processes new user creation records.
    Connect your database hashing mechanics (e.g., passlib/bcrypt) here.
    """
    # Placeholder validation check
    if not user_data.email:
        raise HTTPException(status_code=400, detail="Invalid data footprint.")
    
    # After saving to DB, redirect user to the login screen
    return {"status": "success", "message": "Account created successfully."}


@app.post("/api/login")
async def handle_login(user_data: UserLoginRequest):
    """
    Validates user credentials and issues secure authorization cookies.
    """
    # Add your database lookup and password verification layer here
    response = RedirectResponse(url="/chatbot", status_code=status.HTTP_303_SEE_OTHER)
    
    # Production Cookie Setup Example:
    # response.set_cookie(key="session_token", value="secure_token_string", httponly=True, secure=True)
    return response


@app.get("/logout")
async def handle_logout():
    """
    Clears active user authentication cookies and terminates sessions.
    """
    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.delete_cookie(key="session_token")
    return response


# --- Core RAG Execution Pipeline (POST) ---

@app.post("/chat")
def chat(request: QuestionRequest):
    # Retrieve top match contexts relative to input matrix dimensions
    retrieved_chunks = retrieve(
        request.question,
        chunks,
        embeddings
    )

    # Autoregressive generation pass via TinyLlama pipeline
    answer = generate_answer(
        request.question,
        retrieved_chunks
    )

    return {
        "question": request.question,
        "answer": answer
    }
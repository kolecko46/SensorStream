from fastapi import APIRouter ,Depends, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from modules import schemas, oauth2

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    tags=["Utilities"]
)

@router.get("/calculator")
async def show_calculator(request: Request,
                          user_id: int = Depends(oauth2.get_current_user)):

    return templates.TemplateResponse("web_utilities/calculator.html", {"request": request})

@router.post("/calculator")
async def calculator_logic(data: schemas.CalculatorData,
                           user_id: int = Depends(oauth2.get_current_user)):
    if data.operation == "add":
        result = data.num1 + data.num2
    elif data.operation == "substract":
        result = data.num1 - data.num2
    elif data.operation == "multiply":
        result = data.num1 * data.num2
    elif data.operation == "divide":
        result = data.num1 / data.num2
    else:
        return JSONResponse(content={"error":"Invalid Operation"}, status_code=400)
    
    return JSONResponse(content={"result": result})
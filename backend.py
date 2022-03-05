from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Calculation(BaseModel):
    expression: str


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/calculate/")
async def solve_calculation(calculation: Calculation):
    try:
        calc = eval(calculation.expression)
        return {"result": str(calc)}
    except Exception:
        raise HTTPException(status_code=404, detail="not valid calculation")

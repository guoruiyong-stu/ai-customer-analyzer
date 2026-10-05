from fastapi import FastAPI
from pydantic import BaseModel
from ai import analyze_customer
from database import supabase

app = FastAPI()


class Customer(BaseModel):
    company: str
    need: str
    budget: int



@app.get("/")
def home():
    return {
        "message": "AI customer analyzer"
    }



@app.post("/analyze")
def analyze(customer: Customer):

    customer_data = customer.model_dump()

    # 1. 保存客户
    customer_result = (
        supabase
        .table("customers")
        .insert(customer_data)
        .execute()
    )

    customer_id = customer_result.data[0]["id"]

    # 2. AI分析
    analysis = analyze_customer(customer_data)

    # 3. 保存AI分析结果
    analysis_data = {
        "customer_id": customer_id,
        "level": analysis["level"],
        "score": analysis["score"],
        "reason": analysis["reason"],
        "action": analysis["action"]
    }

    supabase.table(
        "analyses"
    ).insert(
        analysis_data
    ).execute()

    # 4. 返回结果
    return {
        "customer_id": customer_id,
        "analysis": analysis
    }
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):

    customer_result = (
        supabase
        .table("customers")
        .select("*")
        .eq("id", customer_id)
        .execute()
    )

    analysis_result = (
        supabase
        .table("analyses")
        .select("*")
        .eq("customer_id", customer_id)
        .execute()
    )

    return {
        "customer": customer_result.data,
        "analyses": analysis_result.data
    }
from database import supabase



result = (
    supabase
    .table("customers")
    .delete()
    .eq("id", 8)
    .execute()
)

print(result.data)
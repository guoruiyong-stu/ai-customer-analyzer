import pandas as pd
import json
from ai import analyze_customer


df = pd.read_csv("customer.csv")


results = []


for index, row in df.iterrows():

    customer = {
        "company": row["company"],
        "need": row["need"],
        "budget": row["budget"]
    }

    try:
        result = analyze_customer(customer)

    except Exception as e:
        result = {
            "error": str(e)
        }


    results.append({
        "customer": customer,
        "analysis": result
    })


with open("batch_result.json", "w", encoding="utf-8") as f:
    json.dump(
        results,
        f,
        ensure_ascii=False,
        indent=4
    )


print("保存完成")
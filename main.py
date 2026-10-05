from ai import analyze_customer


customer = {
    "company":"ABC科技",
    "need":"AI客服系统",
    "budget":50000
}


result = analyze_customer(customer)


print(result['reason'])
print("客户等级:", result["level"])
print("评分:", result["score"])
print("建议:", result["action"])
import json


with open("result.json", "w", encoding="utf-8") as f:
    json.dump(
        result,
        f,
        ensure_ascii=False,
        indent=4
    )
from database import supabase


customer = {
    "company": "XX教育",
    "need": "智能客服系统",
    "budget": 20000
}


result = supabase.table(
    "customers"
).insert(customer).execute()


print(result.data)
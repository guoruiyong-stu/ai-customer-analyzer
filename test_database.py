from database import supabase


result = supabase.table(
    "customers"
).select("*").execute()


print(result.data)
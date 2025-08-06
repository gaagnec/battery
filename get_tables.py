import requests

# ✅ Вставь свои значения
SUPABASE_URL = "https://yolfklentkyczxkwenis.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlvbGZrbGVudGt5Y3p4a3dlbmlzIiwicm9zZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Mjc5MDU3MiwiZXhwIjoyMDY4MzY2NTcyfQ.JgEm_pM3TGIzDP8U9wtTL3fM95M-GYI8d4ZaXEvg1lo"  # Внимание: использовать ТОЛЬКО на backend

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

# 🔍 Мы запрашиваем только таблицы из схемы public
url = f"{SUPABASE_URL}/rest/v1/information_schema.tables?select=table_name&table_schema=eq.public"

def get_tables():
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        tables = [item['table_name'] for item in response.json()]
        print("📦 Таблицы в Supabase (схема public):")
        for table in tables:
            print(f" - {table}")
        return tables
    except requests.exceptions.RequestException as e:
        print("❌ Ошибка при запросе к Supabase:", e)
        print("📎 Ответ:", response.text if 'response' in locals() else None)
        return []

if __name__ == "__main__":
    get_tables()
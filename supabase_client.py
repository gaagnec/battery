import requests

# URL и anon ключ из твоего Supabase проекта
SUPABASE_URL = "https://yolfklentkyczxkwenis.supabase.co"
SUPABASE_ANON_KEY = "sb_secret__h6oE"  # Замените на ваш действительный ключ

# Заголовки для запроса
headers = {
    "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
    "apikey": SUPABASE_ANON_KEY,
    "Content-Type": "application/json"
}

# Получение данных из таблицы payments
response = requests.get(f"{SUPABASE_URL}/rest/v1/payments", headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    payments_data = response.json()
    print(payments_data)
else:
    print(f"Error: {response.status_code}, {response.text}")
# URL и anon ключ из твоего Supabase проекта
SUPABASE_URL = "https://yolfklentkyczxkwenis.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlvbGZrbGVudGt5Y3p4a3dlbmlzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI3OTA1NzIsImV4cCI6MjA2ODM2NjU3Mn0.xHlX0A9yeTcaGDkeZkmDmVBk1zALA1PnXLK5urQov-k"  # вставь свой реальный ключ

# Создаём клиент один раз
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
import requests

# URL и anon ключ из твоего Supabase проекта
SUPABASE_URL = "https://yolfklentkyczxkwenis.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlvbGZrbGVudGt5Y3p4a3dlbmlzIiwicm9zZSI6ImFub24iLCJpYXQiOjE3NTI3OTA1NzIsImV4cCI6MjA2ODM2NjU3Mn0.xHlX0A9yeTcaGDkeZkmDmVBk1zALA1PnXLK5urQov-k"

# Заголовки для запроса
headers = {
    "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
    "apikey": SUPABASE_ANON_KEY,
    "Content-Type": "application/json"
}

# Получение данных из таблицы payments
response = requests.get(f"{SUPABASE_URL}/rest/v1/payments", headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    payments_data = response.json()
    print(payments_data)
else:
    print(f"Error: {response.status_code}, {response.text}")

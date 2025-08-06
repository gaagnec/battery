from supabase import create_client, Client

# URL и anon ключ из твоего Supabase проекта
SUPABASE_URL = "https://yolfklentkyczxkwenis.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlvbGZrbGVudGt5Y3p4a3dlbmlzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI3OTA1NzIsImV4cCI6MjA2ODM2NjU3Mn0.xHlX0A9yeTcaGDkeZkmDmVBk1zALA1PnXLK5urQov-k"  # вставь свой реальный ключ

# Создаём клиент один раз
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
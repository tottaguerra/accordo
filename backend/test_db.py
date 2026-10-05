import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

try:
    # SQLAlchemy com psycopg2
    engine = create_engine(f'{DATABASE_URL}', echo=False)
    
    with engine.connect() as conn:
        result = conn.execute(text('SELECT 1'))
        print('✅ Conexão com Supabase OK!')
except Exception as e:
    print(f'❌ Erro: {e}')
    print(f'URL: {DATABASE_URL}')

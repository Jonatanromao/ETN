import sqlite3
from collections import Counter

# Função para conectar ao banco de dados
def connect_db(db_path):
    conn = sqlite3.connect(db_path)
    return conn

# Função para detectar perguntas duplicadas
def detect_duplicate_questions(db_path):
    # Conectar ao banco de dados
    conn = connect_db(db_path)
    cursor = conn.cursor()

    # Consulta todas as perguntas
    cursor.execute("SELECT question_text FROM questions")
    questions = cursor.fetchall()

    # Contador para verificar repetições
    question_texts = [question[0] for question in questions]
    question_counter = Counter(question_texts)

    # Filtrar as perguntas duplicadas
    duplicates = {question: count for question, count in question_counter.items() if count > 1}

    # Fechar a conexão
    conn.close()

    # Exibir perguntas duplicadas, se houver
    if duplicates:
        print("Perguntas duplicadas encontradas:")
        for question, count in duplicates.items():
            print(f"Pergunta: '{question}' - Aparece {count} vezes.")
    else:
        print("Nenhuma pergunta duplicada encontrada.")

# Exemplo de uso
db_path = "quiz.db"  # Altere para o caminho correto
detect_duplicate_questions(db_path)

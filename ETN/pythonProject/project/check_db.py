import sqlite3

def check_db():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    # Verifique se as perguntas estão no banco de dados
    c.execute("SELECT * FROM questions")
    questions = c.fetchall()

    if not questions:
        print("Nenhuma pergunta disponível no banco de dados.")
    else:
        for question in questions:
            print(question)

    conn.close()

if __name__ == '__main__':
    check_db()

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import random
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'


def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'quiz.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def get_questions():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Pergunta forçada
    forced_question_id = 78  # ID da pergunta forçada

    # Obter perguntas aleatórias
    cursor.execute('''
        SELECT * FROM questions WHERE id != ? ORDER BY RANDOM() LIMIT 19
    ''', (forced_question_id,))
    random_questions = cursor.fetchall()

    # Adicionar pergunta forçada
    cursor.execute('SELECT * FROM questions WHERE id = ?', (forced_question_id,))
    forced_question = cursor.fetchone()

    if forced_question:
        random_questions.insert(random.randint(0, len(random_questions)), forced_question)

    conn.close()
    return random_questions


@app.route('/')
def index():
    return redirect(url_for('quiz'))


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'questions' not in session:
        # Buscar as perguntas e iniciar o quiz
        session['questions'] = [q['id'] for q in get_questions()]
        session['current'] = 0
        session['answers'] = {}

    if request.method == 'POST':
        question_id = request.form.get('question_id')
        answer = request.form.get('answer')

        # Garantir que a resposta seja armazenada corretamente
        if question_id and answer:
            session['answers'][question_id] = answer

        # Forçar a seleção de uma resposta
        if not answer:
            return "Por favor, selecione uma resposta antes de continuar."

        if 'next' in request.form:
            # Próxima pergunta
            if session['current'] < len(session['questions']) - 1:
                session['current'] += 1
            return redirect(url_for('quiz'))

        elif 'previous' in request.form:
            # Pergunta anterior
            if session['current'] > 0:
                session['current'] -= 1
            return redirect(url_for('quiz'))

        elif 'finish' in request.form:
            # Verificar se todas as perguntas foram respondidas
            if len(session['answers']) == len(session['questions']):
                return redirect(url_for('result'))
            else:
                return "Você precisa responder todas as perguntas antes de finalizar."

    # Buscar a pergunta e as opções atuais
    conn = get_db_connection()
    question_id = session['questions'][session['current']]
    question = conn.execute('SELECT * FROM questions WHERE id = ?', (question_id,)).fetchone()
    options = conn.execute('SELECT * FROM options WHERE question_id = ?', (question_id,)).fetchall()
    conn.close()

    total_questions = len(session['questions'])

    # Renderizar a pergunta atual
    return render_template('quiz.html', question=question, options=options, current=session['current'], total=total_questions)


@app.route('/result')
def result():
    conn = get_db_connection()
    total_correct = 0
    total_questions = len(session['questions'])
    results = []

    for question_id in session['questions']:
        question = conn.execute('SELECT * FROM questions WHERE id = ?', (question_id,)).fetchone()
        options = conn.execute('SELECT * FROM options WHERE question_id = ?', (question_id,)).fetchall()

        # Resposta correta
        correct_answer = question['correct_answer']
        correct_option = next(opt for opt in options if opt['option_label'] == correct_answer)

        # Resposta do usuário
        user_answer = session['answers'].get(str(question_id), None)
        user_option = next((opt for opt in options if opt['option_label'] == user_answer), None)

        # Verificar se o usuário acertou
        if user_answer == correct_answer:
            total_correct += 1
            result = {
                'question_text': question['question_text'],
                'correct': True,
                'correct_option': correct_option['option_text'],
                'user_option': user_option['option_text'] if user_option else 'Nenhuma',
            }
        else:
            result = {
                'question_text': question['question_text'],
                'correct': False,
                'correct_option': correct_option['option_text'],
                'user_option': user_option['option_text'] if user_option else 'Nenhuma',
            }

        results.append(result)

    conn.close()

    # Calcular a pontuação
    score = (total_correct / total_questions) * 10

    return render_template('result.html', results=results, score=score, total=total_questions)


@app.route('/restart')
def restart_quiz():
    # Limpar a sessão ao reiniciar o quiz
    session.clear()
    return redirect(url_for('quiz'))


if __name__ == '__main__':
    app.run(debug=True)

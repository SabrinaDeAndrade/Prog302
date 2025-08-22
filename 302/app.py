from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

CSV_FILE = "users.csv"

# Função para ler os usuários do arquivo CSV
def read_users():
    if not os.path.exists(CSV_FILE):
        return []
    
    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

# Função para adicionar novo usuário ao CSV
def add_user(name, email):
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email])

# Exemplo de rota para adicionar usuário via formulário
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        add_user(name, email)
        return redirect(url_for('list_users'))
    return render_template('add_user.html')

# Exemplo de rota para listar usuários
@app.route('/users')
def list_users():
    users = read_users()
    return render_template('list_users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)

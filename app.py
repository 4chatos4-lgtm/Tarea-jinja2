from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo que simularemos que vienen de una base de datos
datos = {
    "titulo": "Mi Proyecto Jinja2 con Flask",
    "usuario": "Estudiante",
    "mensaje": "¡Bienvenido a la generación dinámica de páginas usando un servidor real!"
}

@app.route('/')
def index():
    # Renderiza index.html y pasa el diccionario de datos
    return render_template('index.html', **datos)

@app.route('/pagina2')
def pagina2():
    # Renderiza pagina2.html que está dentro de la carpeta variantes
    return render_template('variantes/pagina2.html', **datos)

@app.route('/pagina3')
def pagina3():
    # Renderiza pagina3.html que está dentro de la carpeta variantes
    return render_template('variantes/pagina3.html', **datos)

if __name__ == "__main__":
    print("Servidor corriendo en http://127.0.0.1:5000")
    app.run(debug=True)

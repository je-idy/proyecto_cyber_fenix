from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Inventario - Cyber Fenix Tecnología"

@app.route('/item/<codigo>')
def item(codigo):
    return f"Producto con código {codigo} registrado en el inventario de Cyber Fenix"

if __name__ == '__main__':
    app.run(debug=True)
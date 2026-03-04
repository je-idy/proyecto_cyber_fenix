from flask import Flask, render_template, url_for, request, redirect, flash
from form import ProductoForm

app = Flask(__name__)
app.config['SECRET_KEY']='Mi clave secreta'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/item/<codigo>')
def item(codigo):
    return render_template('item.html', codigo=codigo)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/productos')
def productos():
    lista_productos = [
        {"codigo": "A1", "nombre": "Laptop"},
        {"codigo": "B2", "nombre": "Mouse"},
        {"codigo": "C3", "nombre": "Teclado"}
    ]
    return render_template('productos.html', productos=lista_productos)

@app.route('/productos/nuevo', methods=['get','post'])
def producto_nuevo():
    form = ProductoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        cantidad = form.cantidad.data
        precio = form.precio.data

        # Aqui puedes agregar la lógica para guardar el producto en la base de datos
        flash('Producto agregado exitosamente', 'success')
        return redirect(url_for("inicio"))
    return render_template("producto_form.html", form=form, titulo='Nuevo producto')

if __name__ == '__main__':
    app.run(debug=True)

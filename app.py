from flask import Flask, render_template, url_for, request, redirect, flash
from form import ProductoForm
from inventario.bd import init_db, get_db_connection
from inventario.inventario import Inventario
from inventario.productos import Producto
from flask_sqlalchemy import SQLAlchemy
from inventario.inventario_persistencia import guardar_csv, leer_csv, guardar_json,leer_json, guardar_txt,leer_txt
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Mi clave secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invent.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
init_db()
inventario = Inventario()
inventario.cargar_desde_db()

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Bienvenido, {nombre}!'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# ruta de productos
@app.route('/productos/nuevo', methods=['GET', 'POST'])
def producto_nuevo():
    form = ProductoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        cantidad = form.cantidad.data
        precio = form.precio.data
        inventario.agregar_producto(nombre, descripcion, cantidad, precio)
        flash('Producto agregado exitosamente', 'success')
        return redirect(url_for('productos_listar'))
    return render_template('producto_form.html', form=form)

# ruta para listar productos
@app.route('/productos')
def productos_listar():
    inventario.cargar_desde_db()  # Asegurarse de cargar los productos más recientes
    productos = list(inventario.productos.values())
    return render_template('productos.html', productos=productos)

# ruta para editar producto
@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def producto_editar(id):
    producto = inventario.productos.get(id)
    if not producto:
        flash('Producto no encontrado', 'danger')
        return redirect(url_for('productos_listar'))
    
    form = ProductoForm(obj=producto)
    if form.validate_on_submit():
        nombre = form.nombre.data
        descripcion = form.descripcion.data
        cantidad = form.cantidad.data
        precio = form.precio.data
        inventario.actualizar_producto(id, nombre, descripcion, cantidad, precio)
        flash('Producto actualizado exitosamente', 'success')
        return redirect(url_for('productos_listar'))
    
    return render_template('producto_form.html', form=form, producto=producto)

# ruta para eliminar producto
@app.route('/productos/eliminar/<int:id>', methods=['POST'])
def producto_eliminar(id):
    inventario.eliminar_producto(id)
    flash('Producto eliminado exitosamente', 'success')
    return redirect(url_for('productos_listar'))

# ruta para los datos persistentes
@app.route('/datos',methods=['get','post']) # Cambios methods=['get','post']
def datos():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        cantidad = request.form.get('cantidad')
        precio = request.form.get('precio')

        # Registrar en base
        dic = {
        'nombre': nombre,
        'descripción': descripcion,
        'cantidad': cantidad,
        'precio': precio
        }

        # guardar en 3 formatos
        guardar_txt(f"{nombre}, {descripcion}, {cantidad}, {precio}")
        guardar_json(dic)
        guardar_csv(dic)
        flash('Datos guardados exitosamente', 'success')
        return redirect(url_for('datos'))
    
    # leer datos de los 3 formatos
    datos_txt = leer_txt()
    datos_json = json.dumps(leer_json(), ensure_ascii=False, indent=2)
    datos_csv = leer_csv()
    return render_template('datos.html', datos_txt=datos_txt, datos_json=datos_json, datos_csv=datos_csv)
    
if __name__ == '__main__':
    app.run(debug=True)

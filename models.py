import sqlite3

# -------------------------
# Clase Producto
# -------------------------

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio


# -------------------------
# Clase Inventario
# -------------------------

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario {id: Producto}

    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        return list(self.productos.values())
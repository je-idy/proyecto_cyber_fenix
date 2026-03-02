from models import Producto, Inventario
from database import conectar, crear_tabla

crear_tabla()

def añadir_producto_db(producto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO productos (id, nombre, cantidad, precio) VALUES (?, ?, ?, ?)",
        (producto.get_id(), producto.get_nombre(), producto.get_cantidad(), producto.get_precio())
    )

    conn.commit()
    conn.close()

def mostrar_productos_db():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    conn.close()
    return productos

def buscar_producto_db(nombre):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM productos WHERE nombre LIKE ?",
        ('%' + nombre + '%',)
    )

    resultado = cursor.fetchall()
    conn.close()
    return resultado

def actualizar_producto_db(id, cantidad, precio):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE productos SET cantidad = ?, precio = ? WHERE id = ?",
        (cantidad, precio, id)
    )

    conn.commit()
    conn.close()

def eliminar_producto_db(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def menu():
    while True:
        print("\n--- SISTEMA DE INVENTARIO CYBER FENIX ---")
        print("1. Añadir producto")
        print("2. Mostrar productos")
        print("3. Eliminar producto")
        print("4. Actualizar producto")
        print("5. Buscar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            añadir_producto_db(producto)
            print("Producto agregado.")

        elif opcion == "2":
            productos = mostrar_productos_db()
            for p in productos:
                print(p)

        elif opcion == "3":
            id = int(input("ID a eliminar: "))
            eliminar_producto_db(id)
            print("Producto eliminado.")

        elif opcion == "4":
            id = int(input("ID a actualizar: "))
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            actualizar_producto_db(id, cantidad, precio)
            print("Producto actualizado.")

        elif opcion == "5":
            nombre = input("Nombre a buscar: ")
            resultados = buscar_producto_db(nombre)
            for r in resultados:
                print(r)

        elif opcion == "6":
            break


if __name__ == "__main__":
    menu()
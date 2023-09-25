import psycopg2

# Parámetros de conexión
parametros = {
    "host": "direccion_servidor",
    "port": "puerto",
    "user": "nombre_del_usuario",
    "password": "contraseña",
    "database": "nombre_de_la_base_de_datos"
}

conn = psycopg2.connect(**parametros)

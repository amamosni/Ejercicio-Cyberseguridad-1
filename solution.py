# Author: Amir Mosquera
# Discord blindma1den  - Elocanelon/Ejercicio-Cyberseguridad-1

#Se importa la libreria md5
import hashlib

#Se creo manualmente un diccionario con la informacion de los hash de los archivos
dictHashes = {
    'copia.sh' : '90965b0eb20e68b7d0b59accd2a3b4fd',
    'log.txt' : '0b29406e348cd5f17c2fd7b47b1012f9',
    'pass.txt' : '6d5e43a730490d75968279b6adbd79ec',
    'plan-A.txt' : '129ea0c67567301df1e1088c9069b946',
    'plan-B.txt' : '4e9878b1c28daf4305f17af5537f062a',
    'script.py' : '66bb9ec43660194bc066bd8b4d35b151',
}

# Script para generar hash md5 - Tomado del mismo ejercicio
def calcular_md5sum(ruta_archivo, tamano_bloque=65536):
    md5 = hashlib.md5()
    try:
        with open(ruta_archivo, 'rb') as archivo:
            for bloque in iter(lambda: archivo.read(tamano_bloque), b''):
                md5.update(bloque)
        return md5.hexdigest()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al calcular el hash MD5: {e}")
        return None

# Se crea la funcion para comprar le hash obtenido con el hash del backup, para ello se usa un ciclo for
# que itere sobre el diccionario y que tambien se usa para buscar el archivo a validar
def comparar():
    for x, y in dictHashes.items():
        hash_md5 = calcular_md5sum(f'PyJ Systems/{x}')
        if hash_md5:
            print(f"El hash MD5 del archivo '{x}' es: {hash_md5} - backup: {y}")
            if hash_md5 != y:
                print("Los hash son diferentes")

comparar()

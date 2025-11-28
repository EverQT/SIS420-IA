import cv2
import os
import time

# 1. Configuración de la carpeta de destino

# --- MODIFICACIÓN CLAVE AQUÍ PARA SOLUCIONAR EL PROBLEMA DE RUTA ---
nombre_carpeta = "Fotos_Capturadas"

# Obtiene la ruta del directorio donde se encuentra este script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Combina la ruta del script con el nombre de la carpeta para crear la ruta completa
ruta_completa = os.path.join(script_dir, nombre_carpeta)
# -------------------------------------------------------------------

# Si la carpeta no existe, la crea automáticamente
if not os.path.exists(ruta_completa):
    os.makedirs(ruta_completa)
    print(f"Carpeta creada: {ruta_completa}")

# 2. Iniciar la cámara
cap = cv2.VideoCapture(0)  # Cambia a 0 si no abre

# Opcional: Establecer resolución (ancho y alto)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("--- Cámara iniciada ---")
print("Mostrando vista previa durante 5 segundos...")

# Guardar el tiempo inicial
tiempo_inicio = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al acceder a la cámara. Verifica DroidCam.")
        break

    # Mostrar la imagen en una ventana
    cv2.imshow('Vista Previa - Celular', frame)

    # Verificar si han pasado 5 segundos
    if time.time() - tiempo_inicio >= 5:
        nombre_foto = f"foto_{int(time.time())}.jpg"
        ruta_archivo = os.path.join(ruta_completa, nombre_foto)
        cv2.imwrite(ruta_archivo, frame)
        print(f"¡Foto guardada en: {ruta_archivo}!")
        break

    # Permitir cerrar manualmente con 'q' si se desea
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Cerrando programa manualmente...")
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
print("Programa finalizado.")
import csv
#Datos relacionados con ingresos, pasivos, gastos y activos
def ingresar_datos():
    ingresos = input("Ingrese el monto de ingresos: ")
    pasivos = input("Ingrese el monto de pasivos: ")
    gastos = input("Ingrese el monto de gastos: ")
    activos = input("Ingrese el monto de activos: ")
    
    return ingresos, pasivos, gastos, activos

def guardar_datos_en_csv(datos):
    with open('datos_financieros.csv', 'a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(datos)

# Obtener los datos del usuario
datos = ingresar_datos()

# Guardar los datos en el archivo CSV
guardar_datos_en_csv(datos)



import cv2
import pytesseract

def scan_receipts(image_paths):
  receipts_data = []
  
  for image_path in image_paths:
    # Cargar la imagen
    image = cv2.imread(image_path)
    
    # Preprocesamiento de la imagen (si es necesario)
    # image = preprocess_image(image)
    
    # Realizar OCR en la imagen
    text = pytesseract.image_to_string(image)
    
    # Extraer datos específicos del texto OCR
    receipt_info = extract_receipt_info(text)
    
    # Agregar los datos del recibo a la lista
    receipts_data.append(receipt_info)
  
  return receipts_data

# Función para extraer datos específicos del texto OCR



import re

def extract_receipt_info(text):
  # Implementar la lógica para extraer los datos específicos como fecha, monto total, impuesto, etc.
  # Puede usar expresiones regulares u otras técnicas de procesamiento de texto para esto
  
  # Ejemplo: Extraer la fecha del texto utilizando una expresión regular
  date_regex = r"(\d{2}/\d{2}/\d{4})"
  date_match = re.search(date_regex, text)
  if date_match:
    date = date_match.group(1)
  else:
    date = None
    
  # Ejemplo: Extraer el monto total del texto utilizando una expresión regular
  amount_regex = r"Total: (\d+\.\d+)"
  amount_match = re.search(amount_regex, text)
  if amount_match:
    amount = float(amount_match.group(1))
  else:
    amount = None
    
  # Devolver un diccionario con los datos extraídos
  receipt_info = {
    "date": date,
    "amount": amount
  }
  
  return receipt_info




from PIL import Image

def scan_receipts(image_paths):
  receipts_data = []
  
  for image_path in image_paths:
    # Cargar la imagen utilizando la biblioteca PIL
    image = Image.open(image_path)
    
    # Convertir la imagen a escala de grises (opcional)
    image = image.convert("L")
    
    # Realizar OCR en la imagen
    text = pytesseract.image_to_string(image)
    
    # Extraer datos específicos del texto OCR
    receipt_info = extract_receipt_info(text)
    
    # Agregar los datos del recibo a la lista
    receipts_data.append(receipt_info)
  
  return receipts_data
  
  
  
import pytesseract
from PIL import Image

# Ruta de la imagen escaneada
ruta_imagen = ""
# Cargar la imagen
imagen = Image.open(ruta_imagen)

# Utilizar Tesseract para extraer el texto
texto_extraido = pytesseract.image_to_string(imagen, lang='eng')

# Imprimir el texto extraído
print(texto_extraido)




import re

def extract_data_from_ocr(text):
    # Extraer la fecha utilizando una expresión regular
    fecha_pattern = r"\d{2}/\d{2}/\d{4}"
    fecha = re.search(fecha_pattern, text).group()

    # Extraer el monto total utilizando una expresión regular
    monto_total_pattern = r"Total: (\d+\.\d+)"
    monto_total_match = re.search(monto_total_pattern, text)
    monto_total = monto_total_match.group(1) if monto_total_match else None

    # Extraer el impuesto utilizando una expresión regular
    impuesto_pattern = r"Impuesto: (\d+\.\d+)"
    impuesto_match = re.search(impuesto_pattern, text)
    impuesto = impuesto_match.group(1) if impuesto_match else None

    # Extraer los artículos comprados utilizando una expresión regular
    articulos_pattern = r"Artículos: (.+)"
    articulos_match = re.search(articulos_pattern, text)
    articulos_comprados = articulos_match.group(1) if articulos_match else None

    # Devolver los datos extraídos en un diccionario
    return {
        "fecha": fecha,
        "monto_total": monto_total,
        "impuesto": impuesto,
        "articulos_comprados": articulos_comprados
    }

# Ejemplo de uso
ocr_output = "Fecha: 12/05/2022\nTotal: 50.00\nImpuesto: 5.00\nArtículos: Producto 1, Producto 2"
datos_extraidos = extract_data_from_ocr(ocr_output)

# Imprimir los datos extraídos
print("Fecha:", datos_extraidos["fecha"])
print("Monto Total:", datos_extraidos["monto_total"])
print("Impuesto:", datos_extraidos["impuesto"])
print("Artículos Comprados:", datos_extraidos["articulos_comprados"])




import re

def validate_date(date):
    # Validar si la fecha sigue el formato deseado
    date_pattern = r"\d{2}/\d{2}/\d{4}"
    return re.match(date_pattern, date) is not None

def normalize_data(data):
    # Eliminar caracteres especiales y espacios adicionales
    data = re.sub(r"[^\w\s]+", "", data)
    data = re.sub(r"\s+", " ", data)
    return data.strip()

def calculate_subtotal(total, tax):
    # Calcular el subtotal a partir del monto total y el impuesto
    if total and tax:
        return float(total) - float(tax)
    return None

# Ejemplo de datos extraídos
fecha = "12/05/2022"
monto_total = "50.00"
impuesto = "5.00"
articulos_comprados = "Producto 1, Producto 2"

# Validar la fecha
if validate_date(fecha):
    print("Fecha válida:", fecha)
else:
    print("Fecha inválida")

# Normalizar los artículos comprados
articulos_comprados = normalize_data(articulos_comprados)
print("Artículos comprados:", articulos_comprados)

# Calcular el subtotal
subtotal = calculate_subtotal(monto_total, impuesto)
print("Subtotal:", subtotal)




import csv

def export_to_csv(data, filename):
    # Exportar los datos a un archivo CSV
    headers = ["Fecha", "Monto Total", "Impuesto", "Artículos Comprados"]

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(data.values())

# Ejemplo de datos extraídos
fecha = "12/05/2022"
monto_total = "50.00"
impuesto = "5.00"
articulos_comprados = "Producto 1, Producto 2"

# Organizar los datos en un diccionario
data = {
    "Fecha": fecha,
    "Monto Total": monto_total,
    "Impuesto": impuesto,
    "Artículos Comprados": articulos_comprados
}

# Exportar los datos a un archivo CSV
export_to_csv(data, "datos_extraidos.csv")




def validate_data(data):
    # Implementa la lógica de validación para cada campo de datos
    # Retorna True si los datos son válidos, False de lo contrario
    pass
   


def correct_data(data):
    # Implementa la lógica de corrección para cada campo de datos
    # Retorna los datos corregidos
    pass



def interact_with_user(data):
    # Interactúa con el usuario para revisar y corregir manualmente los datos
    # Implementa una interfaz de usuario para mostrar los datos y solicitar correcciones
    pass
    
    
    
    
    # Ejemplo de datos extraídos
    fecha = "12/05/2022"
    monto_total = "1000"

# Validar los datos
if not validate_data(fecha, monto_total):
    print("Datos inválidos")

# Corregir los datos
fecha_corregida, monto_total_corregido = correct_data(fecha, monto_total)

# Interactuar con el usuario para revisar y corregir manualmente los datos, si es necesario
fecha_final, monto_total_final = interact_with_user(fecha_corregida, monto_total_corregido)

# Imprimir los datos finales
print("Fecha:", fecha_final)
print("Monto Total:", monto_total_final)
import requests
import matplotlib.pyplot as plt

def fetch():
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'
    response = requests.get(url)
    
    if response.status_code == 200:
        json_response = response.json()
        dataset = [
            {"price": item.get("price", 0), "condition": item.get("condition", "not_specified")}
            for item in json_response.get("results", [])
            if item.get("currency_id") == "ARS"
        ]
        return dataset
    else:
        print(f"Error en la solicitud: {response.status_code}")
        return []

def transform(dataset, min_precio, max_precio):
    debajo_min = [item for item in dataset if item['price'] < min_precio]
    entre_min_max = [item for item in dataset if min_precio <= item['price'] <= max_precio]
    arriba_max = [item for item in dataset if item['price'] > max_precio]
    
    min_count = len(debajo_min)
    min_max_count = len(entre_min_max)
    max_count = len(arriba_max)
    
    return [min_count, min_max_count, max_count]

# Función para generar el reporte gráfico
def report(data):
    labels = ['Debajo Min', 'Entre Min y Max', 'Arriba Max']
    plt.pie(data, labels=labels)
    plt.title('Distribución de Precios de Alquileres')
    plt.show()

# Flujo principal del programa
if __name__ == "__main__":
    # Definir rango de precios
    min_price = 10000 # Modificar según preferencias
    max_price = 40000  # Modificar según preferencias

    # Paso 1: Consumo de datos
    dataset = fetch()

    # Paso 2: Transformación de datos
    data = transform(dataset, min_price, max_price)

    # Paso 3: Generación del reporte
    report(data)

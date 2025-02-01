from kafka import KafkaProducer # pour la production de messages
import requests #requêtes HTTP
import json #pour manipuler des objets JSON
import time #pour gérer les délais d'attente

# ---------------------------------------------------------------------------
# Étape 1 : Configuration
# ---------------------------------------------------------------------------
# TODO : Remplacez par votre clé personnelle d'API OpenWeather
API_KEY = '1ad47d9c0af333bf88bb58a112e100eb'

# TODO : Ajouter deux autres villes de votre choix pour atteindre 5 villes
CITIES = ['Paris', 'Toulon', 'Lille', 'Corse', 'Lille']  # Exemple : Ajoutez ici vos villes

# TODO : Remplacez par le nom du topic Kafka utilisé dans votre projet
KAFKA_TOPIC = 'topic-weather' # Nom du topic Kafka où seront envoyées les données

# Adresse du serveur Kafka
KAFKA_SERVER = 'localhost:9092' # Adresse du broker Kafka

# ---------------------------------------------------------------------------
# Étape 2 : Initialisation du producteur Kafka
# ---------------------------------------------------------------------------
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_SERVER], # Connexion au serveur Kafka
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Sérialisation en JSON
)

# ---------------------------------------------------------------------------
# Étape 3 : Fonction pour récupérer les données météo
# ---------------------------------------------------------------------------
def get_weather_data(city):
    """
    Fonction qui récupère les données météo d'une ville depuis l'API OpenWeather.
    :param city: Nom de la ville
    :return: Données JSON de la météo
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric" # URL de l'API avec la clé API
    response = requests.get(url) # Requête HTTP GET à l'API
    return response.json() if response.status_code == 200 else None # Retourne les données JSON si la requête réussit

# ---------------------------------------------------------------------------
# Étape 4 : Envoi des données en continu vers Kafka
# ---------------------------------------------------------------------------
# TODO : Remplacez par le bon nom de topic Kafka
while True:
    for city in CITIES:
        data = get_weather_data(city)  # Récupération des données météo
        if data:
            producer.send(KAFKA_TOPIC, key=city.encode('utf-8'), value=data)  # Envoi au topic Kafka
            print(f"Données envoyées pour {city}: {data}") # Affichage des données envoyées dans la console
    time.sleep(60)  # Pause d'une minute entre chaque envoi

# TODO : exécuter le code sur un terminal et s'assurer qu'il fonctionne comme souhaité

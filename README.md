# projet_esme

## Projet Individuel - Real Time Data Streaming ##

**Description**

Ce projet met en place un pipeline de traitement de données météo en temps réel à l'aide de Kafka et Spark Streaming. Il permet de collecter, transformer et analyser les données météorologiques provenant de l'API OpenWeatherMap et de les diffuser en continu via Kafka.

**Objectifs du projet**

- Collecter des données météo en temps réel et les envoyer dans un topic Kafka (topic-weather).

- Traiter les données avec Spark Streaming, calculer des indices météorologiques et nettoyer les données.

- Stocker et diffuser les résultats transformés dans un second topic Kafka (topic-weather-final).

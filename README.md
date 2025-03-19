📸 Backend de Photo Parfaite

Ce projet est une API Django permettant d'uploader plusieurs photos et de déterminer la meilleure photo en fonction d'un score.
🚀 Fonctionnalités

    📤 Upload de plusieurs images via une API REST
    🏆 Sélection automatique de la meilleure photo
    📂 Stockage des images sur le serveur
    🔍 Accès aux URLs des images téléchargées

🛠️ Installation
1️Cloner le projet

git clone https://github.com/OTISDav/photo-parfaite-backend.git
cd photo-parfaite-backend

2️⃣réer et activer un environnement virtuel

python -m venv venv
source venv/bin/activate  #  Mac/Linux
venv\Scripts\activate  #  Windows


 3 Lancer le serveur

python manage.py runserver

📡 API Endpoints
Méthode	Endpoint	Description
POST	/api/upload/	Upload de plusieurs images et récupération de la meilleure photo
📤 Exemple de requête pour uploader des images
Requête (cURL)

curl -X POST http://127.0.0.1:8000/api/upload/ \


🏗️ Technologies utilisées

    Python 3.x
    Django & Django REST Framework
    SQLite/PostgreSQL (selon la configuration)

📜 Licence

Ce projet est sous licence MIT.
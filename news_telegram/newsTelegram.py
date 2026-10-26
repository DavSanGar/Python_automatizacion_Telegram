import requests
import schedule
import time

# Credenciales

TELEGRAM_TOKEN = '**********qrZA';
CHAT_ID = '********5';
GNEWS_API_KEY = "**********037b"

# Categorias

def enviar_noticias():
    print('Recopilando noticias diarías...')
    categorias = ['sports', 'general', 'entertainment', 'world', 'nation', 'business', 'technology'];
    mensaje_final = '¡Buenos días!🤖 Aquí tienes las noticias diarias:\n\n'

# Buscador de noticias

    for cat in categorias:
        url = f"https://gnews.io/api/v4/top-headlines?category={cat}&lang=es&country=es&max=5&apikey={GNEWS_API_KEY}"
        respuesta = requests.get(url).json()

        print(f"Respuesta cruda de {cat}:", respuesta)

        mensaje_final += f"--- {cat.upper()} ---\n"
    # Extraer el primer titular
        if 'articles' in respuesta and len(respuesta['articles']) > 0:
            for articulo in respuesta['articles']:
                titular = articulo['title']
                enlace = articulo['url']

                mensaje_final += f'🔹 {titular}\n🔗 {enlace}\n\n'
            
        else:
            mensaje_final += "No se encontraron noticias en esta categoría.\n\n"

    # 2. Enviar a Telegram
    url_telegram = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url_telegram, data={'chat_id': CHAT_ID, 'text': mensaje_final})
    print('Noticias enviadas con éxito.')

#Programamos hora de envío exacta:

schedule.every().day.at('07:30').do(enviar_noticias)

print('🤖 Contenedor creado. Esperando a la hora programada...')

while True:
    schedule.run_pending()
    time.sleep(60)
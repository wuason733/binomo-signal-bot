
import logging
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

API_TOKEN = "7698322344:AAFAOgiv2797EaRHn0yj7-l5t1EuecRFbPc"
GROUP_ID = "-1002131488392"

bot = Bot(token=API_TOKEN)
logging.basicConfig(level=logging.INFO)

async def send_signal():
    try:
        message = "Señal Binomo:\n\nActivo: Crypto IDX\nDirección: ALZA\nTiempo: 5 minutos"

Activo: Crypto IDX
Dirección: ALZA
Tiempo: 5 minutos

#Binomo #Señal"
        await bot.send_message(chat_id=GROUP_ID, text=message, parse_mode=ParseMode.HTML)
        logging.info("Señal enviada con éxito.")
    except Exception as e:
        logging.error(f"Error al enviar la señal: {e}")

if __name__ == "__main__":
    asyncio.run(send_signal())

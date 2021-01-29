import os

"""
Gustavo Julião     300725185529511936
SharkStriker       242333420120702976
Andoniel           228668654412234762
jukabala           293595056831594496
Gulak              242333420120702976
"""
users = [300725185529511936,
         228668654412234762,
         293595056831594496,
         260438475822596097]
try:
  import discord
except ImportError:
  print ("Trying to Install required module: discord\n")
  os.system('py -3 -m pip install -U discord.py')
# -- above lines try to install requests module if not present
# -- if all went well, import required module again ( for global access)
import discord
from datetime import datetime


print("Inicializando o Tranco no serverino")
print("Aguardando Comandos")

class MyClient(discord.Client):
  async def on_message(self, message):
    #[NOME,NICK,VALOR,PRODUTO,INICIADO,GPS]
    cadastro = [0,0,0,0,0,0]
    autor_cadastro = ""


    if message.content == '!cadastro':
      autor_cadastro = message.author.id
      if message.author.id in users:
        await message.channel.send('Digire o Nome')
      else:
        await message.channel.send('Você não tem acesso a isso')

    if message.content == '!fstart':
      if message.author.id in users:
        print("user name:",message.author.name)
        print("user id:",message.author.id)
        os.system("killstart.bat")
        await message.channel.send('Fechando e Iniciando o Server')
        dha = datetime.now()
        dht = dha.strftime('%d/%m/%Y %H:%M')
        print(dht)
        print("---------------------------------")
        
      else:
        print("user name:",message.author.name)
        print("user id:",message.author.id)
        await message.channel.send('Você não tem acesso a isso')
        dha = datetime.now()
        dht = dha.strftime('%d/%m/%Y %H:%M')
        print(dht)
        print("---------------------------------")
        
    if message.content == '!start':
      print("user name:",message.author.name)
      print("user id:",message.author.id)  
      print("Verificando se o Server está off caso sim iniciará automaticamente")
      os.system("verf.bat")
      await message.channel.send('Verificando se o Server está off caso sim iniciará automaticamente')
      dha = datetime.now()
      dht = dha.strftime('%d/%m/%Y %H:%M')
      print(dht)
      print("---------------------------------")
      
      
client = MyClient()
client.run('')



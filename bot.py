import discord
import requests

# Inicializando o cliente do bot
intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

# Evento de quando o bot é iniciado
@client.event
async def on_ready():
    print(f"Bot iniciado!")


# Enviar mensagens no servidor
@client.event
async def on_message(message):
    # Não responda a mensagens do próprio bot, evita loops infinitos
    if message.author == client.user:
        return

    # Verifica se a mensagem começa com o prefixo "!message"
    if message.content.startswith("!message"):
        # Separando o comando da mensagem
        command, *message_content = message.content.split(" ")

        # Juntando a mensagem separada
        message_content = " ".join(message_content)

        # Verifica se a mensagem está vazia
        if not message_content:
            await message.channel.send("Nenhuma mensagem fornecida para enviar.")
        else:
            # Envia a mensagem para o canal
            await message.channel.send(f"{message_content}")
        # O comando original é deletado
        await message.delete()

    # Verifica se a mensagem começa com o prefixo "!price"
    if message.content.startswith("!price"):
        # Separando o comando e o token da mensagem
        command, symbol = message.content.split(" ")

        # Obtém o preço do token na Binance
        price = get_price(symbol)

        # Verifica se foi possível obter o preço do token
        if price:
            await message.channel.send(f"O preço atual de {symbol} é de US$ {price}")
        else:
            await message.channel.send(f"Não foi possível obter o preço de {symbol}")
        # O comando original é deletado
        await message.delete()


# Obter o valor de criptos e tokens da Binance em USDT
def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return float(data["price"])


# Token do bot
client.run("Token")

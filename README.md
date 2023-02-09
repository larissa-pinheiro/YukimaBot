# YukimaBot - Discord

O YukimaBot é um bot desenvolvido para o [Discord](https://discord.com).<br>
A proposta é simples, serve para envio de mensagens no servidor através do bot por meio do próprio Discord utilizando o comando _!message_ seguido da mensagem. <br>
Ele também faz cotações de criptomoedas e tokens em formato USDT utilizando a API da Binance, basta enviar o comando _!price_ seguido da sigla da criptomoeda a ser cotada com final USDT. Exemplo: _!price BTCUSDT_ <br>
Após enviar a resposta aos comandos, o bot apaga o comando original enviado pelo usuário, evitando "spam".

## Tecnologias utilizadas

- [Python](https://www.python.org)
- [Discord.py](https://pt-br.reactjs.org).

## Inicializando

- Clonar repositório com ```git clone https://github.com/larissa-pinheiro/YukimaBot.git```

- Criar uma nova aplicação no site ```https://discord.com/developers/applications/```

- No site, ir até a guia ```Bot```:
  - Copiar e colar o Token no espaço indicado no final do código Python
  - Adicionar as permissões para ```SERVER MEMBERS INTENT``` e ```MESSAGE CONTENT INTENT```

- Em ```OAuth2``` acessar a opção ```URL Generator```:
  - Em ```SCOPES``` dar check na opção ```bot```
  - Em ```BOT PERMISSIONS``` dar check na opção ```Administrator```
  - Copiar o link gerado no final da página e colar no navegador

- Adicionar o Bot ao seu servidor
- Rodar o código

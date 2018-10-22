# DesafioPontoTel


A API disponibiliza uma url "/search", que onde se você fizer umas POST request, com um body contendo uma palavra, e uma lista de URLs,

ela te retornará o número de ocorrências dessa palavra em cada uma das URLs dessa lista.

Para usar o sistema:

Para startar a aplicação, vá ao diretório principal, e utilize o comando python main.py.

Um servidor entrará em escuta no endereço 127.0.0.1/8000.

Envie um post:
  *Content-type : application/json
  *No body, envie um objeto semelhante à esse: 
    {
      "word": "python",
      "urls": [{
              "url": "https://python.org/",
              "occurrences": 25
          }]
    }
   
Para a utilização do teste, rode o comando pytest no diretório principal.

Os teste se encontrar no arquivo test_sample.py


   

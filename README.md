# Spotify_API

* Vamos costruir um pipeline de dados utilizando os dados da API do Spotify.

* Faremos o processo de ETL completo, desde a extração dos dados, transformação e carregamento dos dados para um banco de dados.

* A API do Spotify retorna os dados das músicas que foram tocadas em uma determinada conta, no caso a minha mesmo, durante os últimos 7 dias e após a coleta dessas informações, vamos selecionar somente aquelas que consideramos importantes para uma rápida visualização. Após esta transformação, vamos armazenas os dados em um banco de dados SQLite simples. 

* Para finzalizar vamos automatizar esse processo executando uma TAG no Airflow, para que essa coleta seja feita automaticamente, todos os dias.

* Só uma um problema: o Spotify muda seu token de autorização após um determinado período de tempo.

* Após a conclusão vou tentar resolver esse problema.

* Esse projeto segue os mesmos padrões do projeto demonstrado no Youtube: https://www.youtube.com/watch?v=dvviIUKwH7o

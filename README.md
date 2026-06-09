#API de Web Scraping e Agregação de Preços

Desenvolvi este projeto para aprofundar meu conhecimento em construção de APIs, com foco em coleta e tratamento de dados reais extraídos da web.

#Tecnologias utilizadas

- Python 3.11
- FastAPI: escolhido pela performance e pela geração automática de documentação
  interativa, o que acelera bastante o ciclo de desenvolvimento.
- BeautifulSoup4: Responsável pelo parsing do HTML e pela extração dos dados.
- Requests: Foco na manipulação de requisições HTTP.
- Uvicorn: Servidor ASGI que roda a aplicação em produção.

#Conceitos aplicados

- Extração e Mineração de dados através da localização de tags específicas do HTML
- Tratamento de strings específicas (textuais para numéricas), para que fiquem legíveis no banco de dados.
- Uso de padrões de arquitetura REST como a separação de responsabilidades.

#Para rodar o projeto

1. Clone o repositório

```Bash
git clone https://github.com/EuAlec/meu-scraper-api.git
```

O maior desafio foi transformar dados requisitados através do HTML em dados úteis e informativos. Houve a necessidade de formatar preços apresentados como textos para formato numérico para a interpretação correta de Banco de Dados.

Também me preocupei com a organização do código, separando responsabilidades seguindo princípios REST, onde cada camada possui uma função definida.

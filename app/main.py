from fastapi import FastAPI
from app.scraper import raspar_preco

app = FastAPI(
  title="API de Web Scraping de Preços",
  description="Desenvolvida para fins de portfólio de estágio de Análise e Desenvolvimento de Sistemas (ADS)"
)

@app.get("/preco")
def obter_preco(url:str):
  """
  Endpoint que recebe uma URL via parâmetro, aciona o scraper e devolve o preço sanitizado em formato JSON  
  """

  preco_final = raspar_preco(url)

  return{
    "status": "sucesso",
    "url_analisada": url,
    "preco": preco_final
  }
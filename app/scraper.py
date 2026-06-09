from bs4 import BeautifulSoup
import requests

def raspar_preco(url: str) -> float:
  "Acessa uma URL, extrei o preço, faz a limpeza de dados e retorna float."
  #Simulando o HTML que o 'requests' traria de um site real
  try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    #Parse do HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    #Encontra a tag span com a classe preco e pega o texto
    tag_preco = soup.find('span', class_='preco')
    if tag_preco is None:
      raise ValueError("Tag de preço não encontrada")
    
    #limpeza dos dados
    preco_limpo = tag_preco.text.replace("R$", "").strip().replace(",", ".")
    return float(preco_limpo)
  
  except requests.RequestException as e:
    raise Exception(f"Erro de:{e}")
  except ValueError as e:
    raise Exception(f"Erro ao procurar o preço:{e}")
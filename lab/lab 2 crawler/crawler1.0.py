import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin, urlparse
import time
import json

class CrawlerEstudo:
    def __init__(self, url_semente, limite_paginas=5, delay=1):
        self.url_semente = url_semente
        self.dominio = f"{urlparse(url_semente).scheme}://{urlparse(url_semente).netloc}"
        self.limite_paginas = limite_paginas
        self.delay = delay
        self.user_agent = "MeuCrawlerEstudantil/1.0 (+https://meusite.com/contato)"
        
        self.visitados = set()
        self.fila = [url_semente]
        self.dados_finais = []
        
        # Inicializa o parser de robots.txt
        self.rp = RobotFileParser()
        self.rp.set_url(urljoin(self.dominio, "robots.txt"))
        try:
            self.rp.read()
        except:
            print("⚠️ Aviso: Não foi possível ler o robots.txt. Usando modo cauteloso.")

    def pode_visitar(self, url):
        """Verifica regras do robots.txt e se a URL é do mesmo domínio."""
        mesmo_dominio = url.startswith(self.dominio)
        permitido_robots = self.rp.can_fetch(self.user_agent, url)
        return mesmo_dominio and permitido_robots

    def extrair(self):
        print(f"🚀 Iniciando crawler em: {self.url_semente}\n")
        
        while self.fila and len(self.visitados) < self.limite_paginas:
            url_atual = self.fila.pop(0)

            if url_atual in self.visitados:
                continue

            if not self.pode_visitar(url_atual):
                print(f"🚫 Ignorada (Robots/Domínio): {url_atual}")
                continue

            try:
                headers = {'User-Agent': self.user_agent}
                res = requests.get(url_atual, headers=headers, timeout=10)
                
                if res.status_code == 200:
                    soup = BeautifulSoup(res.text, 'html.parser')
                    self.visitados.add(url_atual)
                    
                    # 1. Extrair Título
                    titulo = soup.title.string.strip() if soup.title else "Sem Título"
                    
                    # 2. Extrair Links
                    links_encontrados = []
                    for a in soup.find_all('a', href=True):
                        link_completo = urljoin(url_atual, a['href'])
                        links_encontrados.append(link_completo)
                        
                        # Adiciona à fila se for novo e do mesmo site
                        if link_completo not in self.visitados and link_completo.startswith(self.dominio):
                            self.fila.append(link_completo)

                    # Guardar dados na lista
                    self.dados_finais.append({
                        "url": url_atual,
                        "titulo": titulo,
                        "links": list(set(links_encontrados)) # set para remover duplicados na página
                    })

                    print(f"✅ [{len(self.visitados)}] Visitada: {url_atual}")
                    
                    # 3. Delay Ético
                    time.sleep(self.delay)

            except Exception as e:
                print(f"❌ Erro em {url_atual}: {e}")

        self.salvar_dados()

    def salvar_dados(self):
        with open("resultado_crawler.json", "w", encoding="utf-8") as f:
            json.dump(self.dados_finais, f, indent=4, ensure_ascii=False)
        print(f"\n💾 Pronto! {len(self.dados_finais)} páginas salvas em 'resultado_crawler.json'.")

# --- Execução do Exercício ---
if __name__ == "__main__":
    # Exemplo com o site oficial do Python
    meu_crawler = CrawlerEstudo("https://www.bbc.com/portuguese", limite_paginas=50, delay=1)
    meu_crawler.extrair()
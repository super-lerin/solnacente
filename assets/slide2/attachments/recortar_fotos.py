import os
from PIL import Image

def recortar_prints_locais():
    """
    Corta os prints do Instagram diretamente da pasta atual,
    salvando os resultados em uma subpasta 'recortadas'.
    """
    # A pasta de origem é o diretório atual (.)
    pasta_origem = "."
    pasta_destino = "./recortadas"

    # Cria a pasta de destino se ela não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Extensões de imagem suportadas
    extensoes_validas = ('.jpg', '.jpeg', '.png', '.webp')

    # Lista os arquivos da pasta atual
    arquivos = [f for f in os.listdir(pasta_origem) if f.lower().endswith(extensoes_validas)]

    if not arquivos:
        print("Nenhuma imagem encontrada nesta pasta.")
        return

    print(f"Encontradas {len(arquivos)} imagens. Iniciando o corte...")

    for arquivo in arquivos:
        try:
            with Image.open(arquivo) as img:
                largura, altura = img.size

                # Remove os ~11% do topo (barra de usuário) e ~11% da base (botão responder)
                topo = int(altura * 0.11)
                base = int(altura * 0.89)
                
                caixa_corte = (0, topo, largura, base)
                img_recortada = img.crop(caixa_corte)
                
                # Salva na pasta 'recortadas' mantendo o nome original
                caminho_salvar = os.path.join(pasta_destino, arquivo)
                img_recortada.save(caminho_salvar, quality=95)
                
                print(f" ✓ Processado: {arquivo} -> recortadas/{arquivo}")
                
        except Exception as e:
            print(f" ✕ Erro ao processar {arquivo}: {e}")

    print("\nTodo o lote foi processado com sucesso!")

if __name__ == "__main__":
    recortar_prints_locais()

import os
from PIL import Image

def recortar_stories(pasta_origem, pasta_destino):
    """
    Remove as barras pretas de prints de stories do Instagram,
    mantendo apenas a foto centralizada.
    """
    # Cria a pasta de destino se ela não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Pasta de destino criada: {pasta_destino}")

    # Extensões de imagem suportadas
    extensoes_validas = ('.jpg', '.jpeg', '.png', '.webp')

    # Lista os arquivos da pasta
    arquivos = [f for f in os.listdir(pasta_origem) if f.lower().endswith(extensoes_validas)]

    if not arquivos:
        print("Nenhuma imagem encontrada na pasta de origem.")
        return

    for arquivo in arquivos:
        caminho_original = os.path.join(pasta_origem, arquivo)
        
        try:
            with Image.open(caminho_original) as img:
                largura, altura = img.size

                # Define as margens de corte (proporções baseadas em prints padrão)
                # Remove os ~11% do topo e ~11% da base
                topo = int(altura * 0.11)
                base = int(altura * 0.89)
                
                # O corte mantém a largura total (da esquerda 0 até a direita total)
                caixa_corte = (0, topo, largura, base)
                
                # Realiza o recorte
                img_recortada = img.crop(caixa_corte)
                
                # Salva a nova imagem na pasta de destino
                caminho_salvar = os.path.join(pasta_destino, f"cropped_{arquivo}")
                img_recortada.save(caminho_salvar, quantity=95) # Mantém boa qualidade para a web
                
                print(f"Processado com sucesso: {arquivo} -> cropped_{arquivo}")
                
        except Exception as e:
            print(f"Erro ao processar o arquivo {arquivo}: {e}")

# --- Configuração dos Caminhos ---
# Você pode usar caminhos relativos ou absolutos
PASTA_ENTRADA = "./prints_originais"
PASTA_SAIDA = "./fotos_recortadas"

if __name__ == "__main__":
    # Certifique-se de colocar seus prints na pasta configurada antes de rodar
    if not os.path.exists(PASTA_ENTRADA):
        os.makedirs(PASTA_ENTRADA)
        print(f"Criada a pasta '{PASTA_ENTRADA}'. Coloque seus prints dentro dela e rode o script novamente.")
    else:
        print("Iniciando o corte das imagens...")
        recortar_stories(PASTA_ENTRADA, PASTA_SAIDA)
        print("\nProcesso concluído!")

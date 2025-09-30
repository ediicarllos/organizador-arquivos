import os
import shutil

def organizar_pasta(pasta_origem):
    """
    Organiza os arquivos de uma pasta em subpastas de acordo com a extensão.
    """

    tipos_arquivos = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
        "Áudios": [".mp3", ".wav"],
        "Vídeos": [".mp4", ".avi", ".mov"],
        "Compactados": [".zip", ".rar"],
        "Outros": []
    }

    # Criar subpastas caso não existam
    for pasta in tipos_arquivos.keys():
        caminho_pasta = os.path.join(pasta_origem, pasta)
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

    # Mover arquivos
    for arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)

        if os.path.isfile(caminho_arquivo):
            movido = False
            for pasta, extensoes in tipos_arquivos.items():
                if any(arquivo.lower().endswith(ext) for ext in extensoes):
                    shutil.move(caminho_arquivo, os.path.join(pasta_origem, pasta, arquivo))
                    movido = True
                    break
            if not movido:
                shutil.move(caminho_arquivo, os.path.join(pasta_origem, "Outros", arquivo))

    print("✅ Organização concluída!")


if __name__ == "__main__":
    # Altere aqui para a pasta que você deseja organizar
    pasta_alvo = r"C:\Users\ediic\Downloads"
    organizar_pasta(pasta_alvo)

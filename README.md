# Organizador de Arquivos em Python 🗂️

Um script em Python para organizar automaticamente os arquivos de uma pasta em subpastas de acordo com a extensão.  
Ideal para manter sua pasta **Downloads**, **Documentos** ou qualquer outra organizada sem esforço.

---

## Pré-requisitos

- Python 3.x instalado
- (Opcional) Ambiente virtual `venv` para isolar dependências

---

## Como usar

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/organizador-arquivos.git
cd organizador-arquivos
```
2. (Opcional) Crie e ative um ambiente virtual:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3. Rode o script:

```bash
python -m organizador.main
```

---

## Funcionalidades

- Organiza arquivos por categorias:
  - Imagens (jpg, png, gif, etc.)
  - Documentos (pdf, docx, txt, xlsx, etc.)
  - Áudios (mp3, wav, flac)
  - Vídeos (mp4, avi, mov, mkv)
  - Compactados (zip, rar, 7z, tar.gz)
  - Outros (arquivos que não se encaixam nas categorias acima)
- Pergunta ao usuário qual pasta deseja organizar.
- Cria automaticamente as subpastas caso não existam.
- Mostra mensagem de conclusão após organizar os arquivos.
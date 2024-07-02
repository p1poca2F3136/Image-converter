
---

# Conversor de Imagens

Este é um aplicativo de conversão de imagens desenvolvido com Python e Tkinter. Ele permite que os usuários selecionem uma imagem de entrada, escolham o formato de saída desejado e convertam a imagem para o novo formato. O aplicativo também inclui um modo claro/escuro para melhor usabilidade.

## Funcionalidades

- Suporta múltiplos formatos de imagem: PNG, JPEG, BMP, GIF, TIFF, WebP, ICO, EPS, PDF.
- Interface gráfica simples e fácil de usar.
- Alternância entre modo claro e escuro.
- Arrastar e soltar para seleção rápida de arquivos.

## Pré-requisitos

- Python 3.x
- Bibliotecas necessárias:
  - `tkinter`
  - `PIL` (Pillow)
  - `tkinterdnd2`

## Instalação

1. Clone este repositório para o seu computador local:
   ```bash
   git clone https://github.com/p1poca2F3136/conversor-de-imagens.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd conversor-de-imagens
   ```

3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Para Windows use: venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Execute o aplicativo:
   ```bash
   python conversor_de_imagens.py
   ```

2. Na interface do usuário, você pode:
   - Clicar no botão "Selecionar" para escolher a imagem de entrada.
   - Clicar no botão "Selecionar" ao lado de "Salvar como:" para escolher o destino e o formato da imagem de saída.
   - Alternar entre o modo claro e escuro clicando no botão "Modo Escuro".
   - Clicar no botão "Converter" para iniciar a conversão da imagem.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma `issue` ou enviar um `pull request`.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### Exemplo de `requirements.txt`:

Certifique-se de criar um arquivo `requirements.txt` no mesmo diretório do seu projeto com o seguinte conteúdo:

```plaintext
Pillow
tkinterdnd2
```

# Letreco

Jogo de adivinhar palavras de 5 letras, feito em Python com **pygame**, no estilo do Motus / Wordle. Projeto de Algoritmos e Programação (INSA, 2022).

Você tem 6 tentativas para descobrir a palavra secreta. Depois de cada tentativa, as casas mudam de cor:

- 🟩 **verde**: a letra está na palavra e na posição certa
- 🟨 **amarelo**: a letra está na palavra, mas em outra posição
- ⬜ **sem cor**: a letra não está na palavra

## Idiomas

Português, inglês, francês e espanhol. O idioma é escolhido no menu inicial (teclas 1 a 4).

## Como jogar

```bash
pip install pygame
python menu.py
```
Ou apenas baixando todos os arquivos presentes nesse repositório e rodando normalmente com o botão de Run do VScode ou do seu IDE de preferência

Também existe uma versão para o terminal, sem interface gráfica: `python jogo_no_terminal.py`.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `menu.py` | Menu inicial e escolha do idioma |
| `jeu_de_mots.py` | Tabuleiro e regras do jogo (pygame) |
| `jogo_no_terminal.py` | Versão para o terminal |
| `DICIONARIO.py` | Listas de palavras de 5 letras por idioma |

## Autores

Daniel, Pablo e Bernardo

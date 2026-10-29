# Estatística Aplicada e Probabilidade para Engenheiros — Python

Repositório de estudo independente para reproduzir exemplos e resolver exercícios em Python, acompanhando os **15 capítulos** do livro. O sumário usado para organizar o projeto foi fornecido pelo estudante. O projeto **não inclui** o PDF do livro nem enunciados protegidos.

## Estrutura

- `capitulos/`: 15 capítulos, com exemplos, exercícios, notebooks e índice de seções.
- `src/estatistica_eng/`: funções reutilizáveis e testáveis, independentes dos capítulos.
- `tests/`: testes automatizados do código reutilizável.
- `dados/raw/`: conjuntos de dados originais que você tem permissão para compartilhar.
- `dados/processed/`: transformações reproduzíveis a partir de `raw/`.
- `docs/`: convenções, diário de estudo e decisões técnicas.
- `.github/workflows/`: integração contínua (lint e testes).

## Instalação

Requer Python >= 3.11 e Git.

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e '.[dev]'
pytest
ruff check .
```

> No PowerShell, para instalar o extra de desenvolvimento use: `python -m pip install -e ".[dev]"`.

## Fluxo de estudos

1. Escolha uma seção no `README.md` do capítulo correspondente.
2. Reproduza o exemplo em `exemplos/` e resolva exercícios em `exercicios/`.
3. Extraia para `src/` somente funções que fizerem sentido reutilizar.
4. Escreva testes de validação em `tests/` quando possível.
5. Registre fontes, resultados e decisões no capítulo e em `docs/diario_de_estudos.md`.
6. Execute `ruff check .` e `pytest` e faça um commit com escopo bem definido.

## Organização de nomes

Exemplo: `capitulos/capitulo_02_probabilidade/exercicios/questao_02_05_01.py` corresponde ao exercício 1 da seção 2.5 **somente se essa for a numeração real utilizada por você**. Se o livro adota outra numeração, adapte o nome.

## Git

Veja `docs/convencoes.md` para branches, commits, dados, notebooks e reproduzibilidade.

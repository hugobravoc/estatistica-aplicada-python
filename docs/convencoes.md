# Convenções de trabalho

## Um assunto por commit

Formato recomendado: `tipo(escopo): descrição curta` (estilo Conventional Commits).

- `docs(cap02): registra notas sobre probabilidade condicional`
- `feat(cap03): implementa distribuicao binomial`
- `test(cap03): valida funcao de massa binomial`
- `fix(cap07): corrige calculo da variancia`
- `chore(ci): atualiza verificacoes`

## Branches e GitHub

- `main`: código estável, exemplos revisados.
- Branch curta por capítulo ou tarefa: `study/cap02-bayes`, `fix/cap03-binomial`.
- Abra pull request para consolidar um conjunto de alterações, mesmo em projeto individual, quando desejar registrar revisões.
- Tags opcionais para marcos: `cap01-concluido`, `cap02-concluido`.

## Reprodutibilidade

- Indique versão do Python e dependências no `pyproject.toml`.
- Use `numpy.random.default_rng(42)` quando a simulação exigir resultados repetíveis.
- Preserve dados originais em `dados/raw` e descreva origem, licença e transformações.
- Não suba arquivos pesados, tokens, credenciais, ambientes virtuais nem o livro em PDF.
- Execute notebooks do início ao fim antes de publicar e retire saídas enormes/sensíveis.
- Prefira algoritmos didáticos em `.py` e gráficos/análises exploratórias em `.ipynb`.

## Publicação dos exercícios

Identifique capítulo, seção, número do exercício e página quando aplicável. Faça paráfrases curtas da proposta em vez de copiar enunciados ou figuras inteiros. Se o exercício usa dados externos, indique a fonte e a autorização de uso.

## Fluxo padrão

```bash
git checkout -b study/cap02-bayes
# edite os arquivos
ruff check .
pytest
git add .
git commit -m "feat(cap02): implementa exemplo de Bayes"
git push -u origin study/cap02-bayes
```

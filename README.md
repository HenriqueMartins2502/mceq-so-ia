# Uso de ferramentas de IA e satisfação no trabalho de desenvolvedores

Projeto final da disciplina **MCEQ 12576 – Métodos de Computação Experimental e Quantitativa**
PUC-Campinas · Engenharia de Software · 2026

**Equipe:** Gabriel Angeli Capovilla (RA 24003637) e Henrique Della Guardia de Azevedo Martins (RA 24003251)

> **Mudança de tema (24/11/2026):** a base usada no início do projeto (Heshmati e Tullis, Zenodo) não foi aceita na orientação de 19/11. O projeto foi refeito com o Stack Overflow Developer Survey 2025. O plano da análise atual está em [`docs/protocolo.pdf`](docs/protocolo.pdf).

## Pergunta de pesquisa

Entre desenvolvedores profissionais, a satisfação no trabalho difere conforme a frequência de uso de ferramentas de IA no processo de desenvolvimento?

- **H0:** a satisfação no trabalho tem a mesma média (e distribuição) nos 5 grupos de frequência de uso de IA.
- **H1:** pelo menos um grupo difere.
- **Desenho:** k = 5 grupos independentes; estudo **observacional** (associação, não causa).
- **Teste previsto:** ANOVA de um fator (α = 0,05); alternativo: Kruskal-Wallis. Comparações par a par com Tukey HSD ou Mann-Whitney com correção de Bonferroni.

## Origem dos dados

**Stack Overflow Annual Developer Survey 2025** (Stack Overflow / Stack Exchange Inc.)

| Item | Valor |
| --- | --- |
| Página oficial | https://survey.stackoverflow.co/ |
| Arquivo | `results.csv` do repositório oficial [StackExchange/Survey](https://github.com/StackExchange/Survey), pasta `packages/archive/2025` |
| Tamanho | 49.191 linhas × 172 colunas (~141 MB) |
| SHA-256 | `2d1f65308877282edfb4470520eabbc08cb499118432a3dcec6a66c086aa2baa` (idêntico ao publicado) |
| Coleta | 2025 (questionário on-line, respondentes autosselecionados) |
| Data de acesso | 24/11/2026 |
| Licença | [Open Database License (ODbL) 1.0](https://opendatacommons.org/licenses/odbl/1-0/) |

O CSV **não está no repositório**, porque passa do limite de 100 MB do GitHub. Para obtê-lo, rode `python baixar_dados.py`. O script baixa o arquivo oficial e confere o checksum.

### Variáveis usadas

| Coluna | Pergunta original | Uso |
| --- | --- | --- |
| `MainBranch` | Are you someone who writes code? | Filtro: só "I am a developer by profession" |
| `AISelect` | Do you currently use AI tools in your development process? | **VI**, 5 níveis: diário; semanal; mensal ou raro; não usa, pretende; não usa, não pretende |
| `JobSat` | How satisfied are you in your current professional developer role? | **VD**, escala de 0 a 10 |
| `Country`, `WorkExp`, `AISent` | País; anos de experiência profissional; sentimento sobre IA | Só nas análises exploratórias |

O questionário completo e o dicionário de variáveis (`schema.csv`) estão na mesma pasta do repositório oficial.

## Estrutura do repositório

```
README.md               este arquivo
requirements.txt        bibliotecas necessárias
baixar_dados.py         baixa o CSV oficial e confere o checksum
analise.ipynb           análise completa, do dado bruto ao resultado
dados/brutos/           CSV original (baixado pelo script; fora do Git)
dados/limpos/           tabelas geradas pelo notebook
figuras/                figuras geradas pelo notebook
docs/protocolo.pdf      protocolo da análise (24/11/2026)
```

## Como reexecutar

Requer Python 3.10 ou superior.

```bash
git clone <URL deste repositório>
cd mceq-so-ia
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python baixar_dados.py           # ~141 MB
jupyter notebook analise.ipynb   # depois: Run All
```

O notebook regrava todos os arquivos de `dados/limpos/` e `figuras/`. A única etapa com sorteio (a amostra de 5.000 resíduos do Q-Q plot) usa semente fixa (2026), então os números saem iguais em qualquer execução.

## O que o notebook faz

1. Lê o CSV bruto e confere a integridade: IDs únicos, categorias esperadas, escala de 0 a 10.
2. Seleciona a amostra e registra quantos respondentes saem em cada filtro.
3. Gera a tabela descritiva por grupo (n, média, desvio padrão, IC 95%, mediana e quartis).
4. Gera os gráficos: média com IC 95% por grupo e distribuição das notas por grupo.
5. Verifica os pressupostos da ANOVA (Levene, assimetria e Q-Q plot dos resíduos).
6. Roda o teste confirmatório (ANOVA ou Kruskal-Wallis, conforme a regra do protocolo), com tamanho de efeito e comparações par a par.
7. Faz análises **exploratórias**, só descritivas: recorte Brasil, tempo de experiência e sentimento sobre IA.

## Licença

- **Dados:** ODbL 1.0, © Stack Overflow. A redistribuição de dados derivados (`dados/limpos/`) segue a mesma licença.
- **Código:** livre para uso acadêmico.

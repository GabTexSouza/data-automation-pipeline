# Dados

A pasta `data/raw` é usada para armazenar os arquivos mensais de entrada.

A pasta `data/processed` é usada para armazenar a base consolidada e tratada gerada pelo pipeline.

Os arquivos desta pasta são gerados localmente e não são versionados no GitHub.

Para reproduzir o projeto, execute primeiro:

```bash
C:\Users\gabri\anaconda3\python.exe scripts/01_generate_sample_files.py
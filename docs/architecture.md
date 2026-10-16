---
title: Architecture
description: Describe architecture choosen for the project
created_at: 2026-10-16
updated_at: 2026-10-16
---

# Arquitetura

## Objetivo

Este documento registra a organização arquitetural atual do **Idea Inbox** e as responsabilidades atribuídas aos seus módulos. A estrutura busca manter o projeto simples, com separação clara de responsabilidades e espaço para evoluir conforme novas necessidades surgirem.

A arquitetura atual está organizada em três módulos principais: `application`, `messages` e `files`.

## Estrutura atual

src/
├── application/
│ └── orchestrator.py
├── files/
│ └── organizer.py
├── messages/
│ └── message_receiver.py
└── main.py

### `application/`

Contém a lógica de aplicação responsável por coordenar o fluxo principal do programa.

O `Orchestrator`, definido em `orchestrator.py`, coordena a obtenção e o processamento das mensagens. Ele aciona o componente responsável por receber as mensagens e encaminha os resultados para o componente de organização.

A responsabilidade do orquestrador é coordenar as etapas do processo, sem concentrar nele os detalhes específicos de integração com o Telegram ou de manipulação dos arquivos.

### `messages/`

Contém os componentes relacionados à obtenção das mensagens de entrada.

O `MessageReceiver`, definido em `message_receiver.py`, é responsável por buscar ou receber as mensagens enviadas ao bot do Telegram e disponibilizá-las para o restante da aplicação.

Essa separação mantém os detalhes da integração com o Telegram fora da lógica de organização das notas.

### `files/`

Contém os componentes relacionados à organização das notas e aos arquivos gerenciados pelo projeto.

O `Organizer`, definido em `organizer.py`, é responsável por processar as mensagens recebidas e executar a organização correspondente. Na implementação atual, essa responsabilidade também inclui salvar as alterações nos arquivos.

Como o projeto poderá modificar arquivos existentes, está previsto que o processo faça um backup antes de aplicar alterações. Essa proteção deve garantir que as alterações só comecem depois que o backup necessário tiver sido concluído com sucesso.

Caso as operações com arquivos e o processo de backup ganhem complexidade, essas responsabilidades poderão ser extraídas para componentes próprios, sem exigir uma mudança completa na estrutura do projeto.

### `main.py`

É o ponto de entrada da aplicação. Sua função é iniciar e conectar os componentes necessários para executar o fluxo principal.

## Fluxo de processamento

O fluxo atual segue esta sequência:

1. A aplicação inicia pelo `main.py`.
2. O `Orchestrator` coordena o processamento.
3. O `Orchestrator` aciona o `MessageReceiver` para obter as mensagens do Telegram.
4. As mensagens retornadas são encaminhadas ao `Organizer`.
5. O `Organizer` processa as mensagens e organiza as notas, incluindo a gravação nos arquivos.
6. Antes de alterar arquivos existentes, o processo deverá criar o backup necessário e confirmar que ele foi concluído com sucesso.

## Decisões arquiteturais

### Separação por responsabilidade

Os módulos foram separados de acordo com seus papéis no fluxo da aplicação:

- `application`: coordenação do processo;
- `messages`: obtenção de mensagens externas;
- `files`: organização e manipulação dos arquivos.

Essa divisão evita concentrar todo o comportamento em um único módulo e facilita localizar onde uma responsabilidade deve ser implementada.

### Orquestração separada das operações

O `Orchestrator` coordena o fluxo, enquanto os componentes especializados executam as tarefas relacionadas às mensagens e aos arquivos. Dessa forma, os detalhes de cada operação não precisam ficar concentrados na lógica de coordenação.

### Evolução incremental

A arquitetura foi mantida intencionalmente simples. Novas camadas, interfaces ou componentes devem ser introduzidos quando houver uma necessidade concreta, como o aumento da complexidade do armazenamento, do backup ou das regras de organização.

O objetivo não é maximizar a quantidade de módulos, mas manter responsabilidades compreensíveis e reduzir o acoplamento entre partes que podem evoluir de forma independente.

## Considerações futuras

Conforme o projeto evoluir, vale reavaliar a divisão atual nos seguintes pontos:

- **Persistência:** separar a leitura e a gravação de arquivos da lógica que decide como organizar as notas, caso o `Organizer` acumule responsabilidades demais.
- **Backup e recuperação:** definir como os backups serão criados, identificados e usados para recuperar arquivos se uma operação falhar.
- **Organização do conteúdo:** caso as regras de classificação das mensagens se tornem independentes da manipulação dos arquivos, considerar colocá-las em um módulo próprio.
- **Testes:** manter a coordenação, a integração com o Telegram e as operações com arquivos testáveis de forma isolada sempre que isso trouxer benefício.

Esses pontos são possibilidades de evolução, não requisitos que precisam ser implementados imediatamente.

## Resumo

A arquitetura atual separa a coordenação da aplicação (`application`), a entrada de mensagens (`messages`) e a organização dos arquivos (`files`). Essa estrutura atende ao estágio inicial do projeto e permite evoluir gradualmente, preservando a clareza das responsabilidades e priorizando a segurança das alterações nos arquivos.

# 🦉 Strix IA - Drone Autônomo com IA para Dispersão Inteligente de Aves

StrixIA é um sistema inteligente embarcado em drones autônomos, desenvolvido com foco na identificação, monitoramento e dispersão estratégica de aves em áreas sensíveis. A aplicação principal é o controle de aves em lavouras (como arrozais), prevenindo perdas de safra, mas o sistema é totalmente escalável para uso em zonas de segurança aeroportuária, ajudando a evitar colisões com aeronaves (bird strike).

O nome vem de Strix, um gênero de corujas — predadoras naturais de pássaros — representando vigilância silenciosa, eficiência e ação noturna, combinada com IA (Inteligência Artificial) para prover um sistema ágil, adaptável e inteligente.

## 🧠 Visão Geral

O sistema é baseado em um conjunto de módulos especializados, controlados por agentes inteligentes que tomam decisões em tempo real com base em visão computacional, rotas de voo, resposta comportamental das aves e regras programadas.

Cada drone opera de forma autônoma, realizando patrulhas, identificando aves em tempo real e reagindo com estímulos visuais e sonoros para afugentá-las, com registro completo de todas as ações e métricas de desempenho.

## 📁 Estrutura de Pastas

StrixIA/
├─ main.py                     # Script principal de inicialização do sistema
└─ Services/
  ├─ BirdView/               # Módulo de Visão Computacional para detecção e rastreamento de aves
  ├─ FlyControl/             # Módulo de controle de voo (rotas, manobras evasivas, perseguição)
  ├─ LaserPoint/             # Módulo de controle do apontamento e ativação de lasers dissuasores
  ├─ SoundPlay/              # Módulo de reprodução de sons (predadores, ruídos de dispersão)
  ├─ Metrics/                # Coleta de métricas e histórico de ações para análise e melhoria contínua
  ├─ Database/               # Interface de persistência para salvar métricas e eventos capturados


## ⚙️ Tecnologias e Conceitos

- Drones Autônomos
- Visão Computacional com IA
- Agentes Inteligentes
- Controle em tempo real
- Atuação multicanal (som, luz, movimento)
- Rastreamento e Log de métricas
- Aplicações Agro e Aeroportuárias
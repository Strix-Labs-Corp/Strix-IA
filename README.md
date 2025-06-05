# 🦉 Strix IA - Drone Autônomo com IA para Dispersão Inteligente de Aves

StrixIA é um sistema inteligente embarcado em drones autônomos, desenvolvido com foco na identificação, monitoramento e dispersão estratégica de aves em áreas sensíveis. A aplicação principal é o controle de aves em lavouras (como arrozais), prevenindo perdas de safra, mas o sistema é totalmente escalável para uso em zonas de segurança aeroportuária, ajudando a evitar colisões com aeronaves (bird strike).

O nome vem de Strix, um gênero de corujas — predadoras naturais de pássaros — representando vigilância silenciosa, eficiência e ação noturna, combinada com IA (Inteligência Artificial) para prover um sistema ágil, adaptável e inteligente.

## 🧠 Visão Geral

O sistema é baseado em um conjunto de módulos especializados, controlados por agentes inteligentes que tomam decisões em tempo real com base em visão computacional, rotas de voo, resposta comportamental das aves e regras programadas.

Cada drone opera de forma autônoma, realizando patrulhas, identificando aves em tempo real e reagindo com estímulos visuais e sonoros para afugentá-las, com registro completo de todas as ações e métricas de desempenho.

---

## 🚀 Funcionalidades e Coleta de Dados

* **Detecção de Pássaros:** Reconhecimento visual de aves utilizando IA.
* **Ações de Dispersão:**
    * Manobras de voo.
    * Laser direcionado.
    * Emissão de sons para espantar os animais.
* **Coleta de Métricas:**
    * Dados de voo.
    * Período de detecção.
    * Métodos de dispersão utilizados.
    * Taxa de sucesso do espanto (medida pelo tempo entre um espanto e outro).

---

## 📋 Detalhes do Projeto

### ✈️ Cenários de Uso

* **Protótipo:** Uso recomendado em ambiente de testes controlados ou demonstrações via computador.
* **Protótipo Físico:** Recomendado o uso de drone modular.
* **Aplicação Real:** Integração com **drones agrícolas já existentes no mercado** (ex: Drones Spark) devido a:
    * Autonomia.
    * Modularidade nativa (câmera, laser, som, etc.).
    * Centro de processamento nativo.
    * Controle de voo avançado.
    * Capacidade de operação em diversos ambientes.
* **Outras Aplicações:** Potencial de viabilidade no **setor de aviação** para espantar pássaros de pistas.

---

## 📁 Estrutura de Pastas

```
StrixIA/
├─ main.py                     # Script principal de inicialização do sistema
└─ Services/
  ├─ BirdView/               # Módulo de Visão Computacional para detecção e rastreamento de aves
  ├─ FlyControl/             # Módulo de controle de voo (rotas, manobras evasivas, perseguição)
  ├─ LaserPoint/             # Módulo de controle do apontamento e ativação de lasers dissuasores
  ├─ SoundPlay/              # Módulo de reprodução de sons (predadores, ruídos de dispersão)
  ├─ Metrics/                # Coleta de métricas e histórico de ações para análise e melhoria contínua
  ├─ Database/               # Interface de persistência para salvar métricas e eventos capturados
```

---
---

## 🔧 Requisitos Técnicos

### 🖥️ Hardware Recomendado

* **Drone Modular:** Modelos como F450 + Pixhawk Kit (recomendado), S500 / S550.
    * A modularidade do drone permite a montagem tanto com a CPU para controlar ele todo e rodar a IA, quanto montar os periféricos no drone.
* **Microcontrolador de Voo:** Pixhawk Kit (para controle de motores e sensores de voo, principal função de abstrair os comandos de voo para comandos compatíveis com controlador autônomo).
* **Periféricos:**
    * **Speaker:** Buzzers, mini alto-falantes 3W ou 5W.
    * **Câmera:** Raspberry Pi Cam V2, Logitech C270.
    * **Laser:** Módulo Laser verde 532nm 5mW.
* **CPU:** Raspberry Pi 4 ou 5.
    * Módulo de CPU responsável por rodar a IA, controlar o módulo de voo e o uso de periféricos.
    * Compatível com todas as linguagens de programação, com **recomendação de Python** devido às bibliotecas disponíveis.

---

## ⚙️ Tecnologias e Conceitos

- Drones Autônomos
- Visão Computacional com IA
- Agentes Inteligentes
- Controle em tempo real
- Atuação multicanal (som, luz, movimento)
- Rastreamento e Log de métricas
- Aplicações Agro e Aeroportuárias

---

## 🏷️ Possíveis Nomes para o Projeto

* **Strix.IA**
* **STRIX Labs**
* **R.A.V.E.N.** (Repellent Autonomous Vigilance & Environmental Network)
* **A.E.R.O.M.I.N.D.** (Autonomous Environmental Repulsion & Observation Management by Intelligent Neural Drones)
* **NOCU** (No Crow Unleashed)
* **TALON** (Tactical Avian Limiter & Observation Node)
    * Pode ser usado para módulos do sistema, como “TALON Guard”, “TALON Scout”, etc.
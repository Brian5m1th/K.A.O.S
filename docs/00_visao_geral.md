Source: Notas no ClickUp
Tags: #ia-pessoal #arquitetura #stack
Related: [[index]] [[01_estrutura_pastas]] [[02_fluxo_dados]]

# Visão Geral do Assistente de IA Local

Esta é a documentação arquitetural do Assistente de IA Local, planejada para ser consumida diretamente no seu vault do Obsidian. O projeto visa estruturar um ecossistema de agentes inteligentes de alto desempenho rodando localmente.

## 🛠️ Stack Tecnológica

| Componente | Tecnologia | Papel no Ecossistema |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.12+ | Base do desenvolvimento com tipagem forte (Type Hints). |
| **Gerenciador** | `uv` | Gerenciamento ultrarrápido de dependências e ambiente virtual. |
| **Framework Web** | FastAPI | Exposição de APIs REST/WebSockets para a interface. |
| **Agentes** | LangGraph | Orquestrador de fluxos agentivos complexos com estado (Stateful). |
| **Vector DB** | Qdrant | Armazenamento de embeddings e busca RAG de alta performance. |
| **Metadata DB** | PostgreSQL | Persistência de histórico de chat, threads e metadados. |
| **LLM Local** | Ollama | Servidor local executando modelos (Qwen, Llama). |
| **Frontend** | Open WebUI | Interface de usuário amigável conectada ao FastAPI. |

---

## 🗺️ Mapa da Documentação (Obsidian Links)

Navegue pelos componentes detalhados da arquitetura utilizando as notas abaixo:

- [[01_estrutura_pastas|Estrutura de Pastas e Padrão de Camadas]]
- [[02_fluxo_dados|Fluxo de Dados e Ciclo de Vida do Agente]]
- [[03_infraestrutura_docker|Infraestrutura Docker e Ambiente]]
- [[04_integracoes|Integração Obsidian & N8N]]

---

## 🎯 Diretrizes de Projeto

1. **Design Orientado a Domínio (Clean/Layered)**: Arquitetura inspirada em Spring Boot para facilitar manutenção e testabilidade.
2. **Execução Local**: Toda a inteligência e banco de dados rodam em containers locais, sem dependências externas obrigatórias (respeitando a privacidade do Vault).
3. **Tipagem e Pydantic**: Uso extensivo de Pydantic v2 para validação e Type Hints obrigatórios em todas as assinaturas de funções.

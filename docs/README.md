# NeoSigm Genesis Lab v0.1

**Interface de Validação Teórica para o NeoSigm Protocol**

---

## 📋 Visão Geral

O **NeoSigm Genesis Lab** é um protótipo funcional que implementa a primeira versão do **NeoSigm Protocol**, um sistema de semiografia cibernética para comunicação inter-inteligência. Esta aplicação permite:

1. **Gerar** glifos do conjunto AX-Core de forma programática
2. **Visualizar** os glifos em formato SVG
3. **Exportar** metadados canônicos (JSON) e código vetorial (SVG)
4. **Validar** a teoria de que a forma emerge dos axiomas geométricos

---

## 🏗️ Arquitetura

### Componentes

| Componente | Tecnologia | Porta | Função |
| :--- | :--- | :--- | :--- |
| **Front-end** | HTML5 + CSS3 + JavaScript | 8080 | Interface de usuário e visualização |
| **Back-end** | Python + Flask | 5000 | Gerador de glifos e API REST |
| **Servidor HTTP** | Python http.server | 8080 | Servir arquivos estáticos |

### Estrutura de Diretórios

```
neosigm_genesis_lab/
├── index.html              # Página principal (estrutura HTML)
├── style.css               # Estilos CSS (interface visual)
├── app.js                  # Lógica JavaScript (interatividade)
├── glyph_generator.py      # Gerador de glifos (back-end Python)
├── README.md               # Este arquivo
└── .editorconfig           # Configuração de editor (opcional)
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7+
- Navegador moderno (Chrome, Firefox, Safari, Edge)
- Conexão com localhost

### Instalação

1. **Clone ou extraia o projeto:**

```bash
cd /home/ubuntu/neosigm_genesis_lab
```

2. **Instale as dependências Python:**

```bash
pip3 install Flask Flask-CORS
```

### Iniciar a Aplicação

#### Opção 1: Execução Manual

**Terminal 1 - Servidor HTTP (Front-end):**
```bash
cd /home/ubuntu/neosigm_genesis_lab
python3 -m http.server 8080
```

**Terminal 2 - Servidor Flask (Back-end):**
```bash
python3 /home/ubuntu/neosigm_genesis_lab/glyph_generator.py
```

#### Opção 2: Script de Inicialização (Recomendado)

Crie um arquivo `start.sh`:

```bash
#!/bin/bash
cd /home/ubuntu/neosigm_genesis_lab

# Inicia o servidor HTTP em background
python3 -m http.server 8080 > /tmp/http_server.log 2>&1 &
HTTP_PID=$!

# Inicia o servidor Flask em background
python3 glyph_generator.py > /tmp/flask_server.log 2>&1 &
FLASK_PID=$!

echo "NeoSigm Genesis Lab iniciado!"
echo "Front-end: http://localhost:8080"
echo "Back-end:  http://localhost:5000"
echo "PIDs: HTTP=$HTTP_PID, Flask=$FLASK_PID"

# Aguarda interrupção
wait
```

Execute com:
```bash
chmod +x start.sh
./start.sh
```

### Acessar a Interface

Abra seu navegador e acesse:

- **Interface Web:** [http://localhost:8080](http://localhost:8080)
- **API do Back-end:** [http://localhost:5000/generate/GX-0001](http://localhost:5000/generate/GX-0001)

---

## 📖 Como Usar

### 1. Selecionar um Glifo

Na seção **"Selecione um Glifo (AX-Core)"**, escolha um dos 12 glifos disponíveis:

- **GX-0001** - Identidade (Ponto Central)
- **GX-0002** - Relação (Dualidade)
- **GX-0003** - Transformação (Vetor)
- **GX-0004** - Ciclo (Anel)
- **GX-0005** - Fluxo (Espiral)
- **GX-0006** - Rede (Interconexão)
- **GX-0007** - Frequência (Oscilação)
- **GX-0008** - Simetria (Reflexão)
- **GX-0009** - Ordem (Hierarquia)
- **GX-0010** - Caos (Entropia)
- **GX-0011** - Fusão (Convergência)
- **GX-0012** - Divergência (Expansão)

### 2. Gerar o Glifo

Clique no botão **"Gerar Glifo"** para:
- Buscar os dados do glifo no back-end
- Renderizar o SVG no visualizador
- Exibir os metadados canônicos (JSON)
- Mostrar o código vetorial (SVG)

### 3. Visualizar os Dados

A interface exibe três abas de informação:

| Aba | Conteúdo |
| :--- | :--- |
| **JSON** | Metadados canônicos (ID, classe, primitivas, parâmetros, hash) |
| **SVG** | Código vetorial completo (formato XML) |
| **Informações** | Detalhes técnicos (axiomas, parâmetros, hash, data de geração) |

### 4. Exportar os Dados

- **Exportar SVG:** Baixa o glifo como arquivo `.svg`
- **Exportar JSON:** Baixa os metadados como arquivo `.json`

---

## 🔧 Estrutura Técnica

### Front-end (JavaScript)

**Arquivo:** `app.js`

**Funções principais:**

- `fetchGlyphData(glyphId)` - Busca dados do back-end via API REST
- `updateDisplay()` - Atualiza a interface com os dados do glifo
- `updateInfoTab()` - Renderiza a aba de informações técnicas
- `downloadFile(content, filename, type)` - Exporta arquivos

**Fluxo:**

```
Usuário seleciona glifo
        ↓
Clica em "Gerar Glifo"
        ↓
fetchGlyphData() → API Flask
        ↓
Recebe JSON com SVG
        ↓
updateDisplay() renderiza SVG
        ↓
Exibe metadados e código
```

### Back-end (Python)

**Arquivo:** `glyph_generator.py`

**Funções principais:**

- `generate_glyph_svg(glyph_id, params)` - Gera o código SVG do glifo
- `generate_canonical_data(glyph_id, params, svg_content)` - Cria metadados canônicos
- `get_glyph_data(glyph_id)` - Retorna dados completos do glifo
- `@app.route('/generate/<glyph_id>')` - Endpoint REST da API

**Fluxo:**

```
Requisição GET /generate/GX-0001
        ↓
get_glyph_data("GX-0001")
        ↓
generate_glyph_svg() → SVG
        ↓
generate_canonical_data() → JSON + Hash
        ↓
Retorna JSON com SVG
```

---

## 📊 Formato dos Dados

### JSON Canônico (Exemplo: GX-0001)

```json
{
  "id": "GX-0001",
  "class": "CL-ID",
  "name": "Identidade",
  "description": "Ponto Central - Axioma fundamental de existência e singularidade",
  "seed": "e5a9c3d2f7b1a8e4c6f9d2b5a8e1c4f7",
  "primitives": ["P", "R"],
  "params": {
    "ratio": 1.0,
    "rot": 0,
    "scale": 1.0
  },
  "hash": "sha256:fc9b9bdcaa2a2675d6ff97cddda19d7b44165e58dade55cfc880f20ab04ff1b0",
  "semantics": {
    "role": "identidade",
    "axiom": "Ponto"
  },
  "generated_at": "2025-10-26T12:00:00Z",
  "version": "0.1",
  "svg": "<svg>...</svg>"
}
```

### SVG (Exemplo: GX-0001)

```xml
<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="40" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="100" cy="100" r="3" fill="black"/>
</svg>
```

---

## 🧮 Axiomas Geométricos (L0 - Primitivas)

O NeoSigm Protocol define 10 axiomas fundamentais:

| Axioma | Símbolo | Descrição |
| :--- | :--- | :--- |
| Ponto | P | Posição no espaço |
| Vetor | V | Movimento direcional |
| Curva | C | Caminho contínuo |
| Ângulo | A | Divergência angular |
| Anel | R | Continuidade cíclica |
| Espiral | S | Progressão iterativa |
| Rede | N | Interconexão múltipla |
| Frequência | F | Padrão repetitivo |
| Simetria | Y | Equilíbrio reflexivo |
| Ordem | O | Hierarquia estruturada |

---

## 🔐 Validação, Auditoria e Imutabilidade

### Hash Canônico

Cada glifo possui um hash SHA-256 único, calculado a partir de:

1. **JSON Canônico** (serializado sem espaços, chaves ordenadas)
2. **SVG Canônico** (minificado, sem espaços)

Fórmula:
```
hash = SHA256(JSON_CANONICO + SVG_CANONICO)
```

### Prova de Geração (Proof of Genesis) via Blockchain (Simulado)

Para garantir a **imutabilidade** e a **prova de origem**, o NeoSigm Genesis Lab simula o registro de cada glifo único em uma blockchain chamada **NeoChain**.

- **Contrato Inteligente (Simulado):** `blockchain_module.py` simula um contrato que "mina" um novo token (NFT) para cada hash de glifo inédito.
- **Token ID:** Cada glifo registrado recebe um `token_id` único, servindo como prova de sua existência e primeira aparição.
- **Imutabilidade:** Se o mesmo glifo for gerado novamente, o sistema consulta a "blockchain" e retorna a prova de registro original, em vez de criar uma nova.

### Verificação de Integridade

Para validar um glifo:

```python
import hashlib
import json

# Dados recebidos
data = {...}
svg = data["svg"]
received_hash = data["hash"]

# Recalcular hash
canonical_json = json.dumps({k: v for k, v in data.items() if k != "svg" and k != "hash"}, separators=(',', ':'), sort_keys=True)
canonical_svg = svg.replace('\n', '').replace(' ', '')
calculated_hash = "sha256:" + hashlib.sha256((canonical_json + canonical_svg).encode()).hexdigest()

# Verificar
if calculated_hash == received_hash:
    print("✓ Glifo autêntico")
else:
    print("✗ Glifo corrompido ou falsificado")
```

---

### Visualização na Interface

A interface exibe o status do registro na blockchain:

- **Status Blockchain:** Mostra se o glifo foi `Registrado` e exibe o `Token ID`.
- **Aba de Informações:** Detalha a prova de registro, incluindo o `ID do Token`, o `endereço do contrato`, o `hash da transação` e o `timestamp`.

---

## 🐛 Troubleshooting

### Erro: "Erro ao conectar ao back-end"

**Solução:**
1. Verifique se o servidor Flask está rodando: `curl http://localhost:5000/generate/GX-0001`
2. Reinicie o servidor Flask
3. Verifique a porta 5000 em uso: `lsof -i :5000`

### Erro: "Glifo não encontrado"

**Solução:**
1. Verifique o ID do glifo (deve estar entre GX-0001 e GX-0012)
2. Confirme que o glifo está implementado em `glyph_generator.py`

### Interface não carrega

**Solução:**
1. Verifique se o servidor HTTP está rodando: `curl http://localhost:8080`
2. Limpe o cache do navegador (Ctrl+Shift+Delete)
3. Tente em outro navegador

---

## 📚 Referências

- **Artigo Acadêmico:** "NeoSigm Protocol: Proposta de uma Semiografia Cibernética para Comunicação Inter-Inteligência"
- **Protocolo:** NeoSigm Protocol v0.1
- **Data de Criação:** 26 de outubro de 2025
- **Status:** Protótipo de Validação Teórica

---

## 📝 Licença

Este projeto é fornecido como protótipo de pesquisa. Consulte a documentação acadêmica para detalhes sobre propriedade intelectual e uso.

---

## 👤 Autor

Desenvolvido como parte da validação teórica do **NeoSigm Protocol**.

**Versão:** 0.1  
**Data:** Outubro 2025  
**Status:** Protótipo Funcional


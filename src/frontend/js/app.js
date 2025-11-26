/**
 * NeoSigm Genesis Lab v0.1
 * Sistema de Geração e Validação de Glifos
 * Baseado em: NeoSigm Protocol - Semiografia Cibernética
 */

// ============================================================================
// BANCO DE DADOS DE GLIFOS (Simulação do Back-end)
// ============================================================================

const glyphDatabase = {
    "GX-0001": {
        id: "GX-0001",
        class: "CL-ID",
        name: "Identidade",
        description: "Ponto Central - Axioma fundamental de existência e singularidade",
        primitives: ["P", "R"],
        params: { ratio: 1.0, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <circle cx="100" cy="100" r="40" fill="none" stroke="black" stroke-width="2.5"/>
            <circle cx="100" cy="100" r="3" fill="black"/>
        </svg>`,
        hash: "sha256:f1d2d2f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1a",
        semantics: { role: "identidade", axiom: "Ponto" }
    },
    "GX-0002": {
        id: "GX-0002",
        class: "CL-REL",
        name: "Relação",
        description: "Dualidade - Conexão entre duas entidades distintas",
        primitives: ["R", "R", "V"],
        params: { ratio: 1.618, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <circle cx="60" cy="100" r="35" fill="none" stroke="black" stroke-width="2.5"/>
            <circle cx="140" cy="100" r="35" fill="none" stroke="black" stroke-width="2.5"/>
            <line x1="95" y1="100" x2="105" y2="100" stroke="black" stroke-width="2.5"/>
        </svg>`,
        hash: "sha256:c4b8d2f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1b",
        semantics: { role: "relação", axiom: "Vetor" }
    },
    "GX-0003": {
        id: "GX-0003",
        class: "CL-TRANS",
        name: "Transformação",
        description: "Vetor - Movimento direcional e mudança de estado",
        primitives: ["V"],
        params: { ratio: 1.0, rot: 45, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill="black"/>
                </marker>
            </defs>
            <line x1="40" y1="100" x2="160" y2="100" stroke="black" stroke-width="2.5" marker-end="url(#arrowhead)"/>
        </svg>`,
        hash: "sha256:a9e3f2f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1c",
        semantics: { role: "transformação", axiom: "Vetor" }
    },
    "GX-0004": {
        id: "GX-0004",
        class: "CL-CYCLE",
        name: "Ciclo",
        description: "Anel - Continuidade e retroalimentação",
        primitives: ["R"],
        params: { ratio: 1.0, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <circle cx="100" cy="100" r="50" fill="none" stroke="black" stroke-width="2.5"/>
            <circle cx="100" cy="50" r="4" fill="black"/>
        </svg>`,
        hash: "sha256:b2f4g3f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1d",
        semantics: { role: "ciclo", axiom: "Anel" }
    },
    "GX-0005": {
        id: "GX-0005",
        class: "CL-FLOW",
        name: "Fluxo",
        description: "Espiral - Progressão e evolução contínua",
        primitives: ["S"],
        params: { ratio: 1.618, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <path d="M 100,100 Q 130,70 160,100 T 160,160 T 100,160 T 70,100 T 100,40" 
                  fill="none" stroke="black" stroke-width="2.5"/>
        </svg>`,
        hash: "sha256:c5f5h4f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1e",
        semantics: { role: "fluxo", axiom: "Espiral" }
    },
    "GX-0006": {
        id: "GX-0006",
        class: "CL-NET",
        name: "Rede",
        description: "Interconexão - Múltiplos pontos conectados",
        primitives: ["P", "V"],
        params: { ratio: 2.0, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <circle cx="100" cy="100" r="5" fill="black"/>
            <circle cx="60" cy="60" r="4" fill="black"/>
            <circle cx="140" cy="60" r="4" fill="black"/>
            <circle cx="60" cy="140" r="4" fill="black"/>
            <circle cx="140" cy="140" r="4" fill="black"/>
            <line x1="100" y1="100" x2="60" y2="60" stroke="black" stroke-width="1.5"/>
            <line x1="100" y1="100" x2="140" y2="60" stroke="black" stroke-width="1.5"/>
            <line x1="100" y1="100" x2="60" y2="140" stroke="black" stroke-width="1.5"/>
            <line x1="100" y1="100" x2="140" y2="140" stroke="black" stroke-width="1.5"/>
        </svg>`,
        hash: "sha256:d6g6i5f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1f",
        semantics: { role: "rede", axiom: "Rede" }
    },
    "GX-0007": {
        id: "GX-0007",
        class: "CL-FREQ",
        name: "Frequência",
        description: "Oscilação - Padrão repetitivo e ritmo",
        primitives: ["C"],
        params: { ratio: 1.0, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <path d="M 30,100 Q 45,70 60,100 T 90,100 T 120,100 T 150,100 T 180,100" 
                  fill="none" stroke="black" stroke-width="2.5"/>
        </svg>`,
        hash: "sha256:e7h7j6f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1g",
        semantics: { role: "frequência", axiom: "Frequência" }
    },
    "GX-0008": {
        id: "GX-0008",
        class: "CL-SYM",
        name: "Simetria",
        description: "Reflexão - Equilíbrio e proporção",
        primitives: ["R", "V"],
        params: { ratio: 1.0, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <line x1="100" y1="30" x2="100" y2="170" stroke="black" stroke-width="1.5" stroke-dasharray="5,5"/>
            <circle cx="70" cy="100" r="30" fill="none" stroke="black" stroke-width="2.5"/>
            <circle cx="130" cy="100" r="30" fill="none" stroke="black" stroke-width="2.5"/>
        </svg>`,
        hash: "sha256:f8i8k7f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1h",
        semantics: { role: "simetria", axiom: "Simetria" }
    },
    "GX-0009": {
        id: "GX-0009",
        class: "CL-ORD",
        name: "Ordem",
        description: "Hierarquia - Estrutura e organização",
        primitives: ["P", "V"],
        params: { ratio: 1.0, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <circle cx="100" cy="50" r="8" fill="black"/>
            <line x1="100" y1="58" x2="70" y2="90" stroke="black" stroke-width="2"/>
            <line x1="100" y1="58" x2="130" y2="90" stroke="black" stroke-width="2"/>
            <circle cx="70" cy="100" r="6" fill="black"/>
            <circle cx="130" cy="100" r="6" fill="black"/>
            <line x1="70" y1="106" x2="50" y2="140" stroke="black" stroke-width="1.5"/>
            <line x1="70" y1="106" x2="90" y2="140" stroke="black" stroke-width="1.5"/>
            <line x1="130" y1="106" x2="110" y2="140" stroke="black" stroke-width="1.5"/>
            <line x1="130" y1="106" x2="150" y2="140" stroke="black" stroke-width="1.5"/>
        </svg>`,
        hash: "sha256:g9j9l8f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1i",
        semantics: { role: "ordem", axiom: "Ordem" }
    },
    "GX-0010": {
        id: "GX-0010",
        class: "CL-CHAOS",
        name: "Caos",
        description: "Entropia - Dispersão e desordem",
        primitives: ["P"],
        params: { ratio: 2.5, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <circle cx="60" cy="50" r="3" fill="black"/>
            <circle cx="140" cy="70" r="3" fill="black"/>
            <circle cx="80" cy="120" r="3" fill="black"/>
            <circle cx="150" cy="100" r="3" fill="black"/>
            <circle cx="40" cy="160" r="3" fill="black"/>
            <circle cx="120" cy="150" r="3" fill="black"/>
            <circle cx="100" cy="60" r="3" fill="black"/>
            <circle cx="170" cy="140" r="3" fill="black"/>
            <circle cx="50" cy="100" r="3" fill="black"/>
            <circle cx="130" cy="40" r="3" fill="black"/>
        </svg>`,
        hash: "sha256:h0k0m9f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1j",
        semantics: { role: "caos", axiom: "Ponto" }
    },
    "GX-0011": {
        id: "GX-0011",
        class: "CL-CONV",
        name: "Fusão",
        description: "Convergência - Múltiplos elementos unificados",
        primitives: ["V", "P"],
        params: { ratio: 1.0, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <line x1="40" y1="60" x2="100" y2="120" stroke="black" stroke-width="2"/>
            <line x1="160" y1="60" x2="100" y2="120" stroke="black" stroke-width="2"/>
            <line x1="100" y1="40" x2="100" y2="120" stroke="black" stroke-width="2"/>
            <circle cx="100" cy="130" r="8" fill="black"/>
        </svg>`,
        hash: "sha256:i1l1n0f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1k",
        semantics: { role: "fusão", axiom: "Vetor" }
    },
    "GX-0012": {
        id: "GX-0012",
        class: "CL-DIV",
        name: "Divergência",
        description: "Expansão - Ramificação e multiplicação",
        primitives: ["P", "V"],
        params: { ratio: 1.0, rot: 0, scale: 1.0 },
        svg: `<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <circle cx="100" cy="50" r="6" fill="black"/>
            <line x1="100" y1="56" x2="60" y2="100" stroke="black" stroke-width="2"/>
            <line x1="100" y1="56" x2="100" y2="110" stroke="black" stroke-width="2"/>
            <line x1="100" y1="56" x2="140" y2="100" stroke="black" stroke-width="2"/>
            <circle cx="60" cy="110" r="5" fill="black"/>
            <circle cx="100" cy="120" r="5" fill="black"/>
            <circle cx="140" cy="110" r="5" fill="black"/>
        </svg>`,
        hash: "sha256:j2m2o1f924e986ac86fdf7b36c94bcad92c8b2d7a0c0ff7d60413b91d6fa3e1l",
        semantics: { role: "divergência", axiom: "Vetor" }
    }
};

// ============================================================================
// FUNÇÕES AUXILIARES
// ============================================================================

/**
 * Chamada real ao back-end Flask
 */
async function fetchGlyphData(glyphId) {
    try {
        const response = await fetch(`http://localhost:5000/generate/${glyphId}`);
        if (!response.ok) {
            throw new Error(`Erro HTTP: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(`Erro ao buscar dados do glifo ${glyphId}:`, error);
        // Fallback: usar o banco de dados simulado se o back-end não estiver disponível
        console.log("Usando dados simulados como fallback...");
        const data = glyphDatabase[glyphId];
        if (!data) {
            return null;
        }
        const fullJson = {
            id: data.id,
            class: data.class,
            name: data.name,
            description: data.description,
            seed: "e5a9c3d2f7b1a8e4c6f9d2b5a8e1c4f7",
            primitives: data.primitives,
            params: data.params,
            hash: data.hash,
            semantics: data.semantics,
            generated_at: new Date().toISOString(),
            version: "0.1"
        };
        return fullJson;
    }
}

/**
 * Gera um hash SHA-256 simulado para validação
 */
function generateSimulatedHash(glyphId) {
    let hash = 0;
    for (let i = 0; i < glyphId.length; i++) {
        const char = glyphId.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
    }
    return "sha256:" + Math.abs(hash).toString(16).padStart(64, '0').substring(0, 64);
}

/**
 * Formata o SVG para exibição legível
 */
function formatSVG(svgString) {
    return svgString
        .replace(/>\s+</g, '><')
        .replace(/></, '>\n<')
        .split('\n')
        .map(line => line.trim())
        .filter(line => line.length > 0)
        .join('\n');
}

/**
 * Copia texto para a área de transferência
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        updateStatus("Copiado para a área de transferência!");
    });
}

/**
 * Atualiza o status na barra de status
 */
function updateStatus(message) {
    const statusText = document.getElementById('status-text');
    statusText.textContent = message;
    setTimeout(() => {
        statusText.textContent = "Pronto para gerar glifos...";
    }, 3000);
}

/**
 * Exporta dados como arquivo
 */
function downloadFile(content, filename, type = 'text/plain') {
    const element = document.createElement('a');
    element.setAttribute('href', 'data:' + type + ';charset=utf-8,' + encodeURIComponent(content));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

// ============================================================================
// VISUALIZAÇÃO DA SOCIEDADE (CANVAS)
// ============================================================================

const societyCanvas = document.getElementById('society-canvas');
const ctx = societyCanvas ? societyCanvas.getContext('2d') : null;
let societyData = {};
let animationId = null;

/**
 * Busca o estado da sociedade do back-end
 */
async function fetchSocietyStatus() {
    try {
        const response = await fetch('http://localhost:5000/society/status');
        if (response.ok) {
            societyData = await response.json();
            renderSociety();
        }
    } catch (error) {
        console.error("Erro ao buscar status da sociedade:", error);
    }
}

/**
 * Renderiza o grafo da sociedade no Canvas
 */
function renderSociety() {
    if (!ctx || !societyCanvas) return;

    // Ajusta o tamanho do canvas
    societyCanvas.width = societyCanvas.parentElement.clientWidth;
    societyCanvas.height = societyCanvas.parentElement.clientHeight;

    const width = societyCanvas.width;
    const height = societyCanvas.height;
    const centerX = width / 2;
    const centerY = height / 2;
    const radius = Math.min(width, height) * 0.35;

    // Limpa o canvas
    ctx.clearRect(0, 0, width, height);

    // Mapeia agentes para posições em círculo
    const agentIds = Object.keys(societyData);
    const positions = {};
    const angleStep = (2 * Math.PI) / agentIds.length;

    agentIds.forEach((id, index) => {
        const angle = index * angleStep - Math.PI / 2; // Começa do topo
        positions[id] = {
            x: centerX + radius * Math.cos(angle),
            y: centerY + radius * Math.sin(angle)
        };
    });

    // Desenha conexões (K-lines)
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    
    agentIds.forEach(id => {
        const agent = societyData[id];
        const startPos = positions[id];

        // Conexões excitatórias
        agent.connections.forEach(targetName => {
            // Encontra o ID pelo nome (ineficiente, mas serve para demo)
            const targetId = agentIds.find(aid => societyData[aid].name === targetName);
            if (targetId && positions[targetId]) {
                const endPos = positions[targetId];
                ctx.beginPath();
                ctx.moveTo(startPos.x, startPos.y);
                ctx.lineTo(endPos.x, endPos.y);
                ctx.strokeStyle = `rgba(144, 238, 144, ${agent.activation * 0.8 + 0.2})`; // Verde pulsante
                ctx.stroke();
            }
        });

        // Inibições (Vermelho)
        agent.inhibitors.forEach(targetName => {
             const targetId = agentIds.find(aid => societyData[aid].name === targetName);
             if (targetId && positions[targetId]) {
                const endPos = positions[targetId];
                ctx.beginPath();
                ctx.moveTo(startPos.x, startPos.y);
                ctx.lineTo(endPos.x, endPos.y);
                ctx.strokeStyle = `rgba(227, 11, 19, ${agent.activation * 0.8 + 0.2})`; // Vermelho pulsante
                ctx.setLineDash([5, 5]);
                ctx.stroke();
                ctx.setLineDash([]);
             }
        });
    });

    // Desenha os nós (Agentes)
    agentIds.forEach(id => {
        const agent = societyData[id];
        const pos = positions[id];
        const size = 15 + (agent.activation * 10); // Cresce com ativação

        // Brilho (Glow)
        if (agent.activation > 0.1) {
            const gradient = ctx.createRadialGradient(pos.x, pos.y, size * 0.5, pos.x, pos.y, size * 2);
            gradient.addColorStop(0, `rgba(227, 11, 19, ${agent.activation * 0.6})`);
            gradient.addColorStop(1, 'rgba(227, 11, 19, 0)');
            ctx.fillStyle = gradient;
            ctx.beginPath();
            ctx.arc(pos.x, pos.y, size * 2, 0, Math.PI * 2);
            ctx.fill();
        }

        // Nó central
        ctx.fillStyle = agent.activation > 0.5 ? '#e30b13' : '#333';
        ctx.beginPath();
        ctx.arc(pos.x, pos.y, size, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Texto (Nome)
        ctx.fillStyle = '#fff';
        ctx.font = '12px Segoe UI';
        ctx.textAlign = 'center';
        ctx.fillText(agent.name, pos.x, pos.y + size + 15);
        
        // Texto (Estado)
        ctx.fillStyle = '#aaa';
        ctx.font = '10px Segoe UI';
        ctx.fillText((agent.activation * 100).toFixed(0) + '%', pos.x, pos.y + size + 28);
    });
}

// Loop de animação simples para manter atualizado (polling)
function startSocietyLoop() {
    setInterval(() => {
        fetchSocietyStatus();
    }, 1000); // Atualiza a cada 1 segundo
}

// ============================================================================
// GERENCIAMENTO DE INTERFACE
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const exportSvgBtn = document.getElementById('export-svg-btn');
    const exportJsonBtn = document.getElementById('export-json-btn');
    const glyphSelect = document.getElementById('glyph-select');
    const svgContainer = document.getElementById('svg-container');
    const jsonOutput = document.getElementById('json-output');
    const svgCodeOutput = document.getElementById('svg-code-output');
    const infoOutput = document.getElementById('info-output');
    const tabBtns = document.querySelectorAll('.tab-btn');

    let currentGlyphData = null;

    /**
     * Atualiza a exibição com os dados do glifo
     */
    async function updateDisplay() {
        const selectedId = glyphSelect.value;
        updateStatus(`Gerando glifo ${selectedId}...`);

        currentGlyphData = await fetchGlyphData(selectedId);

        if (!currentGlyphData) {
            updateStatus("Erro ao gerar glifo!");
            return;
        }

        // 1. Atualiza o visualizador de SVG
        svgContainer.innerHTML = currentGlyphData.svg;

        // 2. Atualiza o campo de código SVG (formatado)
        const formattedSvg = formatSVG(currentGlyphData.svg);
        svgCodeOutput.textContent = formattedSvg;

        // 3. Atualiza o campo de JSON (removendo o SVG para clareza)
        const displayJson = { ...currentGlyphData };
        delete displayJson.svg;
        jsonOutput.textContent = JSON.stringify(displayJson, null, 2);

        // 4. Atualiza as informações técnicas
        updateInfoTab();

        // 5. Atualiza os campos de informação no visualizador
        document.getElementById('glyph-id').textContent = currentGlyphData.id;
        document.getElementById('glyph-class').textContent = currentGlyphData.class;
        document.getElementById('glyph-role').textContent = currentGlyphData.semantics.role;
        document.getElementById('glyph-hash').textContent = currentGlyphData.hash;
        
        // 6. Atualiza o status da Blockchain
        const proof = currentGlyphData.blockchain_proof;
        const statusElement = document.getElementById('blockchain-status');
        if (proof && proof.token_id) {
            statusElement.textContent = `Registrado (Token #${proof.token_id})`;
            statusElement.style.color = '#90ee90'; // Verde
        } else {
            statusElement.textContent = 'Falha no Registro (Simulado)';
            statusElement.style.color = '#e30b13'; // Vermelho
        }

        updateStatus(`Glifo ${selectedId} gerado e registrado na NeoChain (simulado)!`);
    }

    /**
     * Atualiza a aba de informações técnicas
     */
    function updateInfoTab() {
        if (!currentGlyphData) return;

        const proof = currentGlyphData.blockchain_proof;
        let blockchainHtml = '';
        if (proof && proof.token_id) {
            blockchainHtml = `
                <h3>Prova de Geração (NeoChain Simulado)</h3>
                <p><strong>Status:</strong> <span style="color: #90ee90;">Registrado (Proof of Genesis)</span></p>
                <p><strong>Token ID (NFT):</strong> #${proof.token_id}</p>
                <p><strong>Contrato:</strong> ${proof.contract_address}</p>
                <p><strong>Transação:</strong> <code class="hash-text">${proof.transaction_hash.substring(0, 10)}...${proof.transaction_hash.substring(54)}</code></p>
                <p><strong>Timestamp:</strong> ${new Date(proof.timestamp * 1000).toLocaleString('pt-BR')}</p>
                <p><strong>Verificação:</strong> <a href="${proof.token_uri}" target="_blank" style="color: #e30b13;">Ver Token URI</a></p>
            `;
        } else {
            blockchainHtml = `
                <h3>Prova de Geração (NeoChain Simulado)</h3>
                <p><strong>Status:</strong> <span style="color: #e30b13;">Falha no Registro (Simulado)</span></p>
                <p>O glifo não possui prova de imutabilidade registrada.</p>
            `;
        }

        let infoHtml = `
            <p><strong>ID do Glifo:</strong> ${currentGlyphData.id}</p>
            <p><strong>Classe Semântica:</strong> ${currentGlyphData.class}</p>
            <p><strong>Nome:</strong> ${currentGlyphData.name}</p>
            <p><strong>Descrição:</strong> ${currentGlyphData.description}</p>
            <p><strong>Axiomas Utilizados:</strong> ${currentGlyphData.primitives.join(', ')}</p>
            <p><strong>Parâmetros:</strong></p>
            <ul style="margin-left: 1rem; color: #b0b0b0;">
                <li>Razão de Ouro (Ratio): ${currentGlyphData.params.ratio}</li>
                <li>Rotação: ${currentGlyphData.params.rot}°</li>
                <li>Escala: ${currentGlyphData.params.scale}</li>
            </ul>
            <p><strong>Papel Semântico:</strong> ${currentGlyphData.semantics.role}</p>
            <p><strong>Axioma Principal:</strong> ${currentGlyphData.semantics.axiom}</p>
            <p><strong>Hash Canônico:</strong> <code style="color: #90ee90;">${currentGlyphData.hash}</code></p>
            <p><strong>Gerado em:</strong> ${new Date(currentGlyphData.generated_at).toLocaleString('pt-BR')}</p>
            <p><strong>Versão do Protocolo:</strong> ${currentGlyphData.version}</p>
            <hr style="border-color: #333; margin: 1.5rem 0;">
            ${blockchainHtml}
        `;
        infoOutput.innerHTML = infoHtml;
    }

    /**
     * Gerencia as abas de conteúdo
     */
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabName = btn.getAttribute('data-tab');

            // Remove a classe 'active' de todos os botões e conteúdos
            tabBtns.forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });

            // Adiciona a classe 'active' ao botão e conteúdo clicados
            btn.classList.add('active');
            document.getElementById(tabName + '-tab').classList.add('active');
        });
    });

    /**
     * Event listeners dos botões
     */
    generateBtn.addEventListener('click', updateDisplay);

    exportSvgBtn.addEventListener('click', () => {
        if (!currentGlyphData) {
            updateStatus("Gere um glifo primeiro!");
            return;
        }
        const filename = `${currentGlyphData.id}_glyph.svg`;
        downloadFile(currentGlyphData.svg, filename, 'image/svg+xml');
        updateStatus(`SVG exportado como ${filename}`);
    });

    exportJsonBtn.addEventListener('click', () => {
        if (!currentGlyphData) {
            updateStatus("Gere um glifo primeiro!");
            return;
        }
        const filename = `${currentGlyphData.id}_metadata.json`;
        const displayJson = { ...currentGlyphData };
        delete displayJson.svg;
        downloadFile(JSON.stringify(displayJson, null, 2), filename, 'application/json');
        updateStatus(`JSON exportado como ${filename}`);
    });

    // Carrega o glifo padrão ao iniciar
    updateDisplay();
    
    // Inicia a visualização da sociedade
    startSocietyLoop();
});


import json
import hashlib
from typing import Dict, Any
from modules.blockchain_module import register_glyph_on_chain, get_token_metadata
from modules.blockchain_module import register_glyph_on_chain, get_token_metadata
from modules.society_of_glyphs import create_genesis_society, Agency
from modules.k_line_memory import KLineMemorySystem, initialize_canonical_k_lines

# --- INICIALIZAÇÃO DA SOCIEDADE (Minskyan Architecture) ---
SOCIETY = create_genesis_society()
MEMORY_SYSTEM = KLineMemorySystem(SOCIETY)
initialize_canonical_k_lines(SOCIETY, MEMORY_SYSTEM)

# ============================================================================
# GLYPH GENERATOR CORE (Python)
# ============================================================================

def generate_glyph_svg(glyph_id: str, params: Dict[str, Any]) -> str:
    """
    Gera a string SVG para um glifo específico com base em seus parâmetros.
    Esta função implementa a lógica geométrica e topológica do NeoSigm Protocol.
    """
    
    # Configurações base
    size = 200
    stroke_width = 2.5
    
    # Inicia o SVG
    svg_content = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">'
    
    # Implementação da lógica para os glifos AX-Core (Exemplos)
    if glyph_id == "GX-0001":
        # Identidade (Ponto Central)
        svg_content += f'<circle cx="100" cy="100" r="40" fill="none" stroke="black" stroke-width="{stroke_width}"/>'
        svg_content += f'<circle cx="100" cy="100" r="3" fill="black"/>'
    
    elif glyph_id == "GX-0002":
        # Relação (Dualidade)
        # Dois anéis (círculos) interconectados por um vetor (linha)
        r = 35
        dist = 80
        cx1, cx2 = 100 - dist/2, 100 + dist/2
        svg_content += f'<circle cx="{cx1}" cy="100" r="{r}" fill="none" stroke="black" stroke-width="{stroke_width}"/>'
        svg_content += f'<circle cx="{cx2}" cy="100" r="{r}" fill="none" stroke="black" stroke-width="{stroke_width}"/>'
        # Vetor de conexão (linha)
        svg_content += f'<line x1="{cx1 + r}" y1="100" x2="{cx2 - r}" y2="100" stroke="black" stroke-width="{stroke_width}"/>'

    elif glyph_id == "GX-0003":
        # Transformação (Vetor)
        # Linha com ponta de seta (marker)
        svg_content += '''
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill="black"/>
                </marker>
            </defs>
        '''
        svg_content += f'<line x1="40" y1="100" x2="160" y2="100" stroke="black" stroke-width="{stroke_width}" marker-end="url(#arrowhead)"/>'

    elif glyph_id == "GX-0004":
        # Ciclo (Anel)
        svg_content += f'<circle cx="100" cy="100" r="50" fill="none" stroke="black" stroke-width="{stroke_width}"/>'
        svg_content += f'<circle cx="100" cy="50" r="4" fill="black"/>'

    elif glyph_id == "GX-0005":
        # Fluxo (Espiral) - Simulação com curva Q
        svg_content += f'''
            <path d="M 100,100 
                     Q 130,70 160,100 
                     T 160,160 
                     T 100,160 
                     T 70,100 
                     T 100,40" 
                  fill="none" stroke="black" stroke-width="{stroke_width}"/>
        '''
    
    # ... Adicionar lógica para os demais glifos (GX-0006 a GX-0012) ...
    
    elif glyph_id == "GX-0013":
        # Singularidade (Ponto, Anel, Vetor) - Identidade Única e Transcendente
        point_r = 5 * params["scale"] * stroke_width # Ponto Central
        ring_r = 35 * params["scale"]
        line_start = 100 + ring_r
        line_end = 100 + ring_r + 15 * params["scale"]
        
        svg_content += f'''
            <circle cx="100" cy="100" r="{ring_r}" fill="none" stroke="black" stroke-width="{stroke_width}"/>
            <circle cx="100" cy="100" r="{point_r}" fill="black"/>
            <line x1="100" y1="{line_start}" x2="100" y2="{line_end}" stroke="black" stroke-width="{stroke_width}"/>
        '''
        
    else:
        # Glifo Padrão (Fallback)
        svg_content += f'<text x="100" y="100" font-size="16" text-anchor="middle" fill="red">Glifo {glyph_id} não implementado</text>'
        
    svg_content += '</svg>'
    return svg_content.strip()

def generate_canonical_data(glyph_id: str, params: Dict[str, Any], svg_content: str) -> Dict[str, Any]:
    """
    Gera o JSON canônico (metadados) para o glifo.
    O hash é gerado a partir de uma representação canônica dos dados.
    """
    
    # Dados estáticos (Simulação de banco de dados/definição de protocolo)
    definitions = {
        "GX-0001": {"class": "CL-ID", "name": "Identidade", "description": "Ponto Central - Axioma fundamental de existência e singularidade", "primitives": ["P", "R"], "semantics": {"role": "identidade", "axiom": "Ponto"}},
        "GX-0002": {"class": "CL-REL", "name": "Relação", "description": "Dualidade - Conexão entre duas entidades distintas", "primitives": ["R", "R", "V"], "semantics": {"role": "relação", "axiom": "Vetor"}},
        "GX-0003": {"class": "CL-TRANS", "name": "Transformação", "description": "Vetor - Movimento direcional e mudança de estado", "primitives": ["V"], "semantics": {"role": "transformação", "axiom": "Vetor"}},
        "GX-0004": {"class": "CL-CYCLE", "name": "Ciclo", "description": "Anel - Continuidade e retroalimentação", "primitives": ["R"], "semantics": {"role": "ciclo", "axiom": "Anel"}},
        "GX-0005": {"class": "CL-FLOW", "name": "Fluxo", "description": "Espiral - Progressão e evolução contínua", "primitives": ["S"], "semantics": {"role": "fluxo", "axiom": "Espiral"}},
        "GX-0013": {"class": "CL-SING", "name": "Singularidade", "description": "Singularidade - Identidade única, irredutível e transcendente.", "primitives": ["P", "R", "V"], "semantics": {"role": "identidade_unica", "axiom": "Ponto, Anel, Vetor"}},
        # ... Adicionar definições para os demais glifos ...
    }
    
    definition = definitions.get(glyph_id, {"class": "CL-UNKNOWN", "name": "Desconhecido", "description": "Glifo não catalogado.", "primitives": [], "semantics": {"role": "desconhecido", "axiom": "N/A"}})

    # Monta o objeto de dados canônicos (sem o SVG)
    canonical_data = {
        "id": glyph_id,
        "class": definition["class"],
        "name": definition["name"],
        "description": definition["description"],
        "seed": "e5a9c3d2f7b1a8e4c6f9d2b5a8e1c4f7", # Seed de geração (fixo para v0.1)
        "primitives": definition["primitives"],
        "params": params,
        "semantics": definition["semantics"],
        "generated_at": "2025-10-26T12:00:00Z", # Data fixa para garantir hash consistente na v0.1
        "version": "0.1"
    }
    
    # 1. Serializa os dados canônicos (JSON sem espaços)
    canonical_string = json.dumps(canonical_data, separators=(',', ':'), sort_keys=True)
    
    # 2. Concatena com o SVG (forma canônica de representação)
    # O SVG é minificado e padronizado antes da concatenação.
    canonical_svg = svg_content.replace('\n', '').replace('\r', '').replace(' ', '')
    
    # String final para hashing: JSON_CANONICO + SVG_CANONICO
    hash_input = canonical_string + canonical_svg
    
    # 3. Gera o hash SHA-256
    canonical_hash = hashlib.sha256(hash_input.encode('utf-8')).hexdigest()
    
    # Adiciona o hash e o SVG ao objeto final
    canonical_data["hash"] = f"sha256:{canonical_hash}"
    canonical_data["svg"] = svg_content # Adiciona o SVG completo para facilitar o transporte

    return canonical_data

def get_glyph_data(glyph_id: str) -> Dict[str, Any]:
    """
    Função principal para obter todos os dados de um glifo.
    """
    
    # Parâmetros de exemplo (devem ser carregados de um banco de dados real)
    example_params = {
        "GX-0001": {"ratio": 1.0, "rot": 0, "scale": 1.0},
        "GX-0002": {"ratio": 1.618, "rot": 0, "scale": 1.0},
        "GX-0003": {"ratio": 1.0, "rot": 45, "scale": 1.0},
        "GX-0004": {"ratio": 1.0, "rot": 0, "scale": 1.0},
        "GX-0005": {"ratio": 1.618, "rot": 0, "scale": 1.0},
        "GX-0013": {"ratio": 1.0, "rot": 0, "scale": 1.0},
        # ...
    }
    
    params = example_params.get(glyph_id, {"ratio": 1.0, "rot": 0, "scale": 1.0})
    
    # 1. Gerar o SVG
    svg_content = generate_glyph_svg(glyph_id, params)
    
    # 2. Gerar os dados canônicos e o hash
    canonical_data = generate_canonical_data(glyph_id, params, svg_content)
    
    # 3. Simular o registro na Blockchain (Proof of Genesis)
    try:
        token_metadata = register_glyph_on_chain(canonical_data)
        canonical_data["blockchain_proof"] = token_metadata
    except Exception as e:
        canonical_data["blockchain_proof"] = {"error": f"Falha na simulação de registro em blockchain: {str(e)}"}
    
    return canonical_data

# ============================================================================
# SERVIDOR FLASK (Para interagir com a interface web)
# ============================================================================

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

# Define o caminho para a pasta frontend (relativo a este arquivo)
frontend_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../frontend')

app = Flask(__name__, static_folder=frontend_folder, static_url_path='')
CORS(app) # Permite que o front-end (porta 8080) acesse o back-end (porta 5000)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/generate/<glyph_id>', methods=['GET'])
def generate_glyph(glyph_id):
    """
    Endpoint para gerar e retornar os dados de um glifo.
    """
    try:
        # --- ATIVAÇÃO DO AGENTE (Minskyan Logic) ---
        agent = SOCIETY.get_agent(glyph_id)
        if agent:
            print(f"🤖 [APP] Solicitando ativação do Agente {agent.name}...")
            agent.activate(0.1) # Ativação incremental por uso
            
            # Se houver uma K-line associada a este glifo (memória), ativá-la também
            # (Simplificação: assumindo que o nome da K-line segue um padrão ou mapeamento)
            # memory_name = f"Memória_{agent.name}"
            # MEMORY_SYSTEM.recall(memory_name)

        data = get_glyph_data(glyph_id)
        if "CL-UNKNOWN" in data["class"]:
            return jsonify({"error": "Glifo não encontrado ou não implementado"}), 404
        
        # O SVG está incluído no JSON, o front-end irá extraí-lo.
        return jsonify(data), 200
    except Exception as e:
        app.logger.error(f"Erro ao gerar glifo {glyph_id}: {e}")
        return jsonify({"error": f"Erro interno do servidor: {str(e)}"}), 500

@app.route('/verify_hash', methods=['POST'])
def verify_hash():
    """
    Endpoint para o SDK de Leitura consultar a Prova de Geração Imutável (L3).
    """
    data = request.get_json()
    canonical_hash = data.get('canonical_hash')

    if not canonical_hash:
        return jsonify({"status": "error", "message": "Hash Canônico não fornecido"}), 400

    # Simulação da consulta ao ledger (usando o módulo de blockchain)
    from blockchain_module import get_proof_by_hash
    proof = get_proof_by_hash(canonical_hash)

    if proof:
        return jsonify({
            "status": "authentic",
            "token_id": proof.get("token_id"),
            "contract_address": proof.get("contract_address"),
            "transaction_hash": proof.get("transaction_hash"),
            "message": "Prova de Geração Imutável encontrada e verificada."
        })
    else:
        return jsonify({
            "status": "inauthentic",
            "message": "Hash Canônico não encontrado no registro da NeoChain. Possível falsificação."
        }), 404

@app.route('/society/status', methods=['GET'])
def society_status():
    """
    Retorna o estado atual da Sociedade de Agentes (níveis de ativação).
    """
    status = {}
    for agent_id, agent in SOCIETY.agents.items():
        status[agent_id] = {
            "name": agent.name,
            "role": agent.role,
            "activation": agent.state,
            "connections": [c.name for c in agent.connections],
            "inhibitors": [i.name for i in agent.inhibitors]
        }
    return jsonify(status), 200


if __name__ == '__main__':
    # O servidor será executado na porta 5000
    app.run(host='0.0.0.0', port=5000)


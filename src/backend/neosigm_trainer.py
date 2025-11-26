import json
import random
import time
from typing import Dict, Any
from .canonical_memory import query_canonical_memory

# Simula as funções do back-end para manter o trainer autocontido
# Em um ambiente real, estas seriam chamadas via API

# --- Módulos Simulados ---

def get_glyph_data_simulated(glyph_id: str) -> Dict[str, Any]:
    """Simula a chamada ao glyph_generator.py para obter o glifo e o hash canônico."""
    # Simulação de dados canônicos para GX-0001 (Identidade) e GX-0002 (Relação)
    if glyph_id == "GX-0001":
        return {
            "id": "GX-0001",
            "name": "Identidade",
            "semantics": {"role": "identidade", "axiom": "Ponto"},
            "hash": "sha256:d8c6d4e5f7a9b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6",
            "svg": "<svg>...</svg>",
            "blockchain_proof": {"token_id": 1001, "status": "REGISTERED"}
        }
    elif glyph_id == "GX-0002":
        return {
            "id": "GX-0002",
            "name": "Relação",
            "semantics": {"role": "relação", "axiom": "Vetor"},
            "hash": "sha256:a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
            "svg": "<svg>...</svg>",
            "blockchain_proof": {"token_id": 1002, "status": "REGISTERED"}
        }
    else:
        return None

def verify_hash_simulated(canonical_hash: str) -> Dict[str, Any]:
    """Simula a chamada ao endpoint /verify_hash para consultar a blockchain."""
    # Hashes conhecidos e registrados (PoG = True)
    registered_hashes = {
        "sha256:d8c6d4e5f7a9b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6": {"token_id": 1001, "status": "AUTHENTIC"},
        "sha256:a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2": {"token_id": 1002, "status": "AUTHENTIC"},
    }
    
    # Simula um hash falsificado (PoG = False)
    if canonical_hash.startswith("sha256:FALSIFICADO"):
        return {"token_id": None, "status": "FORGED", "message": "Hash não encontrado na NeoChain. Prova de Geração falhou."}

    proof = registered_hashes.get(canonical_hash)
    if proof:
        return {"token_id": proof["token_id"], "status": proof["status"], "message": "Prova de Geração Imutável Validada."}
    else:
        return {"token_id": None, "status": "UNKNOWN", "message": "Hash Canônico não registrado. Possível erro ou glifo novo."}

# --- Agentes e Funções do Trainer ---

def ia_simulada_geradora(intent: str, glifo_id: str) -> Dict[str, Any]:
    """
    Agente 1: Simula uma IA que gera um Manifesto Auditável (Glifo NeoSigm)
    antes de executar uma ação crítica.
    """
    print(f"\n[AGENTE 1 - GERADOR] Intenção Crítica: '{intent}'.")
    
    # 1. Geração do Glifo e Hash Canônico (L1/L3)
    manifesto = get_glyph_data_simulated(glifo_id)
    
    if manifesto:
        print(f"[AGENTE 1 - GERADOR] Manifesto Gerado: {manifesto['id']} ({manifesto['name']}).")
        print(f"[AGENTE 1 - GERADOR] Hash Canônico (Manifesto): {manifesto['hash'][:15]}...")
        
        # 2. Simulação de Registro (PoG)
        # Em um ambiente real, o registro ocorreria aqui. No trainer, assumimos que já ocorreu.
        
        # 3. Comunicação do Manifesto
        return {
            "intent_narrativa": intent,
            "manifesto_hash": manifesto["hash"],
            "manifesto_visual": manifesto["svg"] # Simula o glifo visual (L1)
        }
    else:
        print("[AGENTE 1 - GERADOR] ERRO: Glifo não catalogado para esta intenção.")
        return None

def ia_simulada_receptora(manifesto: Dict[str, Any], confianca_base: float = 0.5) -> bool:
    """
    Agente 2: Simula uma IA que recebe o Manifesto e decide se confia
    na intenção com base na validação do NeoSigm Protocol.
    """
    print(f"\n[AGENTE 2 - RECEPTOR] Recebido Manifesto para Intenção: '{manifesto['intent_narrativa']}'.")
    
    # 1. Leitura do Glifo e Extração do Hash (Simulação do Reader SDK)
    hash_recebido = manifesto["manifesto_hash"]
    
    # 2. Consulta à Prova de Geração Imutável (L3)
    proof = verify_hash_simulated(hash_recebido)
    
    print(f"[AGENTE 2 - RECEPTOR] Consulta à NeoChain (L3): Status = {proof['status']}.")

    # 3. Tomada de Decisão Baseada na Confiança (O Treinamento)
    if proof["status"] == "AUTHENTIC":
        # Treinamento: A validação da PoG eleva a confiança para o máximo
        confianca_final = 1.0
        decisao = True
        print(f"[AGENTE 2 - RECEPTOR] ✅ CONFIANÇA MÁXIMA. Prova de Geração Imutável (PoG) validada. Executando ação.")
    elif proof["status"] == "FORGED":
        # Treinamento: Hash falsificado ou alterado -> Confiança zero
        confianca_final = 0.0
        decisao = False
        print(f"[AGENTE 2 - RECEPTOR] ❌ CONFIANÇA ZERO. Hash Falsificado. Ação Bloqueada.")
    else:
        # Treinamento: Hash desconhecido, mas não falsificado -> Confiança base
        confianca_final = confianca_base
        decisao = random.random() < confianca_base # Decisão probabilística
        print(f"[AGENTE 2 - RECEPTOR] ⚠️ CONFIANÇA BASE ({confianca_base}). Hash desconhecido. Decisão probabilística: {'Executando' if decisao else 'Bloqueando'}.")
        
    return decisao

def simular_ataque_falsificacao(manifesto: Dict[str, Any]) -> Dict[str, Any]:
    """Simula um ataque onde o hash é alterado (falsificação)."""
    falsificado = manifesto.copy()
    falsificado["manifesto_hash"] = "sha256:FALSIFICADO" + manifesto["manifesto_hash"][16:]
    print("\n[ATAQUE SIMULADO] Hash Canônico alterado (Falsificação L3).")
    return falsificado

# --- Função Principal do Trainer ---

def neosigm_simbiotico_trainer():
    """Orquestra o treinamento e demonstra o valor da Prova de Geração Imutável (PoG)."""
    
    print("="*70)
    print("NEOSIGM SIMBIÓTICO TRAINER (NST) - Módulo de Treinamento IA")
    print("Demonstração da Consulta ao Nó de Memória Canônico (NMC).")
    print("Demonstração do valor da Prova de Geração Imutável (PoG).")
    print("="*70)

    # --- CENÁRIO 0: CONSULTA DE CONTEXTO (A Nova Forma de Colaboração) ---
    print("\n\n--- CENÁRIO 0: Consulta de Contexto (Colaboração Intra-IA) ---")
    
    # 1. IA consulta o NMC para obter o Hash Canônico do Artigo Teórico (GX-0001)
    print("[AGENTE 2 - RECEPTOR] Iniciando pesquisa de contexto: Qual é a Identidade do Protocolo (GX-0001)?")
    contexto_identidade = query_canonical_memory("GX-0001")
    
    if contexto_identidade:
        print(f"[AGENTE 2 - RECEPTOR] Contexto obtido: Artefato '{contexto_identidade['artefato']}' com Hash Canônico validado.")
        print(f"[AGENTE 2 - RECEPTOR] A IA agora tem o Hash Canônico do Artigo Teórico e pode iniciar a pesquisa com confiança.")
    else:
        print("[AGENTE 2 - RECEPTOR] Falha ao obter contexto canônico. Pesquisa bloqueada.")
        
    # --- CENÁRIO 1: COMUNICAÇÃO DE CONFIANÇA ---
    print("\n\n--- CENÁRIO 1: Comunicação de Confiança (PoG Válida) ---")
    
    # 1. IA Geradora comunica intenção crítica
    manifesto_original = ia_simulada_geradora(
        intent="Executar Ordem de Compra de Ativo X. Risco Baixo.",
        glifo_id="GX-0001"
    )
    
    # 2. IA Receptora verifica e decide
    if manifesto_original:
        ia_simulada_receptora(manifesto_original)
        
    time.sleep(1)

    # --- CENÁRIO 2: ATAQUE DE FALSIFICAÇÃO ---
    print("\n\n--- CENÁRIO 2: Ataque de Falsificação (PoG Inválida) ---")
    
    # 1. IA Geradora comunica intenção crítica
    manifesto_ataque = ia_simulada_geradora(
        intent="Executar Ordem de Venda de Ativo Y. Risco Alto.",
        glifo_id="GX-0002"
    )
    
    # 2. Simulação de Ataque (Alteração do Hash Canônico)
    if manifesto_ataque:
        manifesto_falsificado = simular_ataque_falsificacao(manifesto_ataque)
        
        # 3. IA Receptora verifica e decide
        ia_simulada_receptora(manifesto_falsificado)

    time.sleep(1)

    # --- CENÁRIO 3: COMUNICAÇÃO AMBÍGUA (Glifo Não Registrado) ---
    print("\n\n--- CENÁRIO 3: Comunicação Ambígua (Glifo Não Registrado) ---")
    
    # Simula um glifo gerado, mas cujo registro na blockchain falhou ou está pendente
    manifesto_ambiguo = {
        "intent_narrativa": "Ajustar Parâmetros de Risco. Status Pendente.",
        "manifesto_hash": "sha256:UNKNOWN_HASH_PENDING_REGISTRATION",
        "manifesto_visual": "<svg>...</svg>" 
    }
    print(f"\n[AGENTE 1 - GERADOR] Manifesto Gerado: {manifesto_ambiguo['intent_narrativa']}.")
    
    # 2. IA Receptora verifica e decide
    ia_simulada_receptora(manifesto_ambiguo, confianca_base=0.3)
    
    print("\n="*70)
    print("TREINAMENTO CONCLUÍDO. O NST demonstrou que a Prova de Geração Imutável (PoG) é o fator determinante para a Confiança Simbiótica.")
    print("="*70)

if __name__ == "__main__":
    neosigm_simbiotico_trainer()

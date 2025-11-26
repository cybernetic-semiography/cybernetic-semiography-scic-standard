import time
from typing import Dict, Any

# ============================================================================
# SIMULAÇÃO DE BLOCKCHAIN (NeoChain)
# ============================================================================

# Variáveis globais para simular o estado do contrato e do token
CONTRACT_ADDRESS = "0xNeoSigmProtocolContractAddress001"
TOKEN_COUNTER = 1000  # Começa em 1000 para simular tokens já emitidos
REGISTERED_GLYPHS = {}  # Hash -> Token Data

def generate_token_id(glyph_hash: str) -> int:
    """
    Gera um ID de token determinístico baseado no hash do glifo.
    Em um sistema real, isso seria o resultado da transação de minting.
    Aqui, usamos um hash simples para simular.
    """
    global TOKEN_COUNTER
    # Simula a emissão de um novo token
    TOKEN_COUNTER += 1
    return TOKEN_COUNTER

def register_glyph_on_chain(canonical_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Registra um glifo na blockchain simulada (NeoChain).
    Retorna os metadados de registro (token ID, contrato, hash da transação, timestamp).
    """
    glyph_hash = canonical_data.get("hash", "unknown")
    
    # Verifica se o glifo já foi registrado
    if glyph_hash in REGISTERED_GLYPHS:
        return REGISTERED_GLYPHS[glyph_hash]
    
    # Gera um novo token ID
    token_id = generate_token_id(glyph_hash)
    
    # Simula uma transação de blockchain
    tx_hash = f"0x{glyph_hash[:64]}"  # Simula um hash de transação
    timestamp = int(time.time())
    
    # Armazena os metadados do registro
    registration_data = {
        "status": "Registrado",
        "token_id": token_id,
        "contract_address": CONTRACT_ADDRESS,
        "tx_hash": tx_hash,
        "timestamp": timestamp,
        "glyph_hash": glyph_hash
    }
    
    REGISTERED_GLYPHS[glyph_hash] = registration_data
    return registration_data

def get_token_metadata(glyph_hash: str) -> Dict[str, Any]:
    """
    Recupera os metadados de um token registrado na blockchain.
    Retorna None se o glifo não foi registrado.
    """
    return REGISTERED_GLYPHS.get(glyph_hash, None)

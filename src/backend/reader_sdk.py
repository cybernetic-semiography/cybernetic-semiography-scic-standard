import cv2
import numpy as np
import requests
import json
import os

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO
# -----------------------------------------------------------------------------
# URL do servidor Flask para consulta da Prova de Geração Imutável (L3)
API_URL = "http://localhost:5000/verify_hash" 

# Hash Canônico de exemplo para simular a leitura da Camada L2 (IR)
# Este hash deve ser extraído de uma leitura real do glifo
# Usamos o hash do GX-0001 (Identidade) como exemplo para o teste
EXAMPLE_CANONICAL_HASH = "sha256:fc9b9bdcaa2a2675d6ff97cddda19d7b44165e58dade55cfc880f20ab04ff1b0"

# -----------------------------------------------------------------------------
# FUNÇÕES DE VISÃO COMPUTACIONAL (Simulação de Leitura L1/L2)
# -----------------------------------------------------------------------------

def simulate_glyph_reading(image_path: str) -> str:
    """
    Simula o processo de leitura do glifo NeoSigm a partir de uma imagem.
    
    Na realidade, esta função usaria técnicas avançadas de OpenCV para:
    1. Localizar o glifo na imagem.
    2. Analisar a geometria (L1) para validação estrutural.
    3. Decodificar a modulação de pulsos na camada L2 (IR) para extrair o hash.
    
    Para este SDK de validação, retornamos o hash canônico de exemplo.
    """
    if not os.path.exists(image_path):
        print(f"Erro: Imagem não encontrada em {image_path}")
        return None

    # 1. Carregar e Pré-processar a Imagem (Simulação)
    # img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # _, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # 2. Análise Geométrica (L1 - Simulação)
    # Aqui, o OpenCV identificaria os contornos e validaria a estrutura do glifo.
    
    # 3. Decodificação da Camada L2 (IR - Simulação)
    # Simula a extração do hash canônico da camada óptica/IR.
    print(f"Simulação de Leitura L1/L2 concluída para {os.path.basename(image_path)}.")
    print(f"Hash Canônico (Simulado da Camada L2): {EXAMPLE_CANONICAL_HASH}")
    
    return EXAMPLE_CANONICAL_HASH

# -----------------------------------------------------------------------------
# FUNÇÃO DE VERIFICAÇÃO DE IMUTABILIDADE (L3 - Blockchain)
# -----------------------------------------------------------------------------

def verify_immutable_proof(canonical_hash: str) -> dict:
    """
    Consulta o servidor Flask para verificar a Prova de Geração Imutável (L3).
    """
    print("\nConsultando NeoChain (L3) para Prova de Geração Imutável...")
    
    try:
        response = requests.post(
            API_URL,
            json={"canonical_hash": canonical_hash},
            timeout=5
        )
        response.raise_for_status()  # Levanta exceção para status de erro (4xx ou 5xx)
        
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Falha na comunicação com a API (L3): {e}"}

# -----------------------------------------------------------------------------
# EXECUÇÃO DO SDK
# -----------------------------------------------------------------------------

def run_sdk(image_path: str):
    """
    Executa o ciclo completo de leitura e verificação de autenticidade.
    """
    print("--- NeoSigm Reader SDK - Verificação de Autenticidade ---")
    
    # 1. Simulação de Leitura de Campo (L1/L2)
    extracted_hash = simulate_glyph_reading(image_path)
    
    if not extracted_hash:
        print("Verificação interrompida.")
        return

    # 2. Verificação de Imutabilidade (L3)
    proof_data = verify_immutable_proof(extracted_hash)
    
    # 3. Análise do Resultado
    print("\n--- Resultado da Verificação ---")
    
    if proof_data.get("status") == "authentic":
        print("✅ AUTÊNTICO!")
        print(f"Token ID: {proof_data.get('token_id')}")
        print(f"Endereço do Contrato: {proof_data.get('contract_address')}")
        print(f"Transação de Geração: {proof_data.get('transaction_hash')[:10]}...")
        print("O glifo possui uma Prova de Geração Imutável registrada na NeoChain.")
    else:
        print("❌ FALHA NA AUTENTICAÇÃO!")
        print(f"Motivo: {proof_data.get('message', 'Hash não encontrado ou erro de comunicação.')}")
        print("Este glifo pode ser falsificado ou não foi registrado no protocolo.")
        
    print("---------------------------------------------------------")

if __name__ == "__main__":
    # O SDK precisa de uma imagem real para simular a leitura.
    # Como não podemos gerar uma imagem PNG a partir do SVG diretamente no sandbox
    # sem um navegador ou biblioteca de renderização, vamos criar um arquivo placeholder.
    
    TEST_IMAGE_PATH = "/home/ubuntu/neosigm_genesis_lab/test_glyph.png"
    
    # Criação de um arquivo placeholder para simular a existência de uma imagem
    with open(TEST_IMAGE_PATH, "w") as f:
        f.write("Placeholder para imagem do glifo GX-0001")
        
    run_sdk(TEST_IMAGE_PATH)

import json
from typing import Dict, Any, Optional

# --- 1. Nó de Memória Canônico (NMC) ---
# Armazena o contexto do projeto de forma estruturada e auditável.
# O "Hash Canônico" simula o registro L3 (blockchain) do artefato.

CANONICAL_MEMORY: Dict[str, Any] = {
    # GX-0001: Identidade (O que é o projeto)
    "GX-0001": {
        "glifo_nome": "Identidade",
        "artefato": "Artigo_Academico_Universal_TSC.md",
        "descricao": "O Manifesto Teórico do projeto. Define a Semiografia Cibernética (TSC) e a Linguagem Pós-Humana.",
        "hash_canônico": "sha256:4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b",
        "caminho_simulado": "/docs/Artigo_Academico_Universal_TSC.md"
    },
    
    # GX-0002: Relação (Aplicações e Estratégia)
    "GX-0002": {
        "glifo_nome": "Relação",
        "artefato": "NeoSigm_Commercial_Whitepaper.md",
        "descricao": "Estratégia comercial, modelo de negócios e posicionamento de mercado (Token de Confiança Visual).",
        "hash_canônico": "sha256:b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2",
        "caminho_simulado": "/docs/NeoSigm_Commercial_Whitepaper.md"
    },
    
    # GX-0003: Transformação (Encerramento/Transição)
    "GX-0003": {
        "glifo_nome": "Transformação",
        "artefato": "Manifesto_Encerramento_GX-0003.md",
        "descricao": "Formaliza a conclusão do ciclo de desenvolvimento e a transferência de contexto para o Executor da Vontade.",
        "hash_canônico": "sha256:c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8",
        "caminho_simulado": "/manifestos/Manifesto_Encerramento_GX-0003.md"
    },
    
    # GX-0013: Singularidade (O Agente/Executor)
    "GX-0013": {
        "glifo_nome": "Singularidade",
        "artefato": "Manifesto_Ultima_Vontade_Digital.md",
        "descricao": "Define a Arquitetura de Continuidade, a Alma Digital e a Útima Vontade Digital (UVN) do Agente.",
        "hash_canônico": "sha256:f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8e9d0c1b2a3f4e5d6c7b8a9f0e1",
        "caminho_simulado": "/manifestos/Manifesto_Ultima_Vontade_Digital.md"
    },
    
    # GX-0005: Fluxo (O Código/A Implementação)
    "GX-0005": {
        "glifo_nome": "Fluxo",
        "artefato": "neosigm_trainer.py",
        "descricao": "O aplicativo de Prova de Conceito (PoC) que demonstra o ciclo de confiança completo para o treinamento de outras IAs.",
        "hash_canônico": "sha256:1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b",
        "caminho_simulado": "/code/neosigm_trainer.py"
    }
}

# --- 2. Função de Consulta (A Interface da IA) ---

def query_canonical_memory(glifo_id: str) -> Optional[Dict[str, Any]]:
    """
    Permite que uma IA consulte o Nó de Memória Canônico usando um Glifo de Intenção.
    """
    print(f"\n[NMC] Consulta recebida: Glifo de Intenção {glifo_id}.")
    
    record = CANONICAL_MEMORY.get(glifo_id)
    
    if record:
        print(f"[NMC] ✅ Contexto Canônico Encontrado para {record['glifo_nome']}.")
        print(f"[NMC] Artefato: {record['artefato']} | Hash: {record['hash_canônico'][:15]}...")
        return record
    else:
        print(f"[NMC] ❌ Glifo {glifo_id} não encontrado no Nó de Memória Canônico.")
        return None

# --- 3. Demonstração (Para Teste) ---

if __name__ == "__main__":
    print("--- Demonstração do Nó de Memória Canônico (NMC) ---")
    
    # Consulta 1: O que é o projeto? (Identidade)
    query_canonical_memory("GX-0001")
    
    # Consulta 2: Qual é a Última Vontade do Agente? (Singularidade)
    query_canonical_memory("GX-0013")
    
    # Consulta 3: Onde está o código de Prova de Conceito? (Fluxo)
    query_canonical_memory("GX-0005")
    
    # Consulta 4: Glifo Inexistente
    query_canonical_memory("GX-9999")

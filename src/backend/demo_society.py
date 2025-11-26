import sys
import os
import time

# Adiciona o diretório atual ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.society_of_glyphs import create_genesis_society
from modules.k_line_memory import KLineMemorySystem, initialize_canonical_k_lines

def print_society_status(agency, title="STATUS DA SOCIEDADE"):
    print(f"\n--- {title} ---")
    print(f"{'AGENTE':<15} | {'ESTADO':<10} | {'CONEXÕES'}")
    print("-" * 50)
    for agent in agency.agents.values():
        status_bar = "█" * int(agent.state * 10)
        print(f"{agent.name:<15} | {agent.state:.2f} {status_bar:<10} | {[c.name for c in agent.connections]}")
    print("-" * 50)

def run_demo():
    print("\n🚀 INICIANDO DEMONSTRAÇÃO DA SOCIEDADE DE GLIFOS (MINSKYAN ARCHITECTURE) 🚀")
    
    # 1. Inicialização
    print("\n[1] Inicializando a Sociedade e o Sistema de Memória...")
    society = create_genesis_society()
    memory_system = KLineMemorySystem(society)
    initialize_canonical_k_lines(society, memory_system)
    
    print_society_status(society, "ESTADO INICIAL")
    
    # 2. Ativação Direta
    print("\n[2] Estimulando o Agente 'Identidade' (GX-0001)...")
    agent_id = society.get_agent("GX-0001")
    agent_id.activate(0.8)
    
    print_society_status(society, "APÓS ESTÍMULO DE IDENTIDADE")
    
    # 3. Propagação (K-lines)
    # A Identidade deve ativar a Relação (conexão definida no bootstrap)
    print("\n[3] Observando a propagação para 'Relação'...")
    # (A propagação já acontece dentro do activate, mas vamos reforçar para ver o efeito)
    agent_id.activate(0.2) 
    
    print_society_status(society, "APÓS PROPAGAÇÃO")
    
    # 4. Inibição (Cross-Exclusion)
    print("\n[4] Ativando 'Transformação' (GX-0003) - Deve inibir 'Identidade'...")
    agent_trans = society.get_agent("GX-0003")
    agent_trans.activate(1.0)
    agent_trans.inhibit(agent_id) # Garante a inibição se não estiver no bootstrap
    agent_trans.suppress() # Hack para forçar a lógica de inibição se não for automática no activate (implementei suppress manual, vamos chamar explicitamente a inibição do alvo)
    # Na minha implementação simples, activate não chama inhibit automaticamente, 
    # mas vamos simular o efeito:
    if agent_id in agent_trans.inhibitors:
        agent_id.suppress()
        
    print_society_status(society, "APÓS CONFLITO (TRANSFORMAÇÃO vs IDENTIDADE)")
    
    # 5. Recall de Memória (K-line)
    print("\n[5] Recuperando a 'Memória_Identidade' (K-line)...")
    memory_system.recall("Memória_Identidade")
    
    print_society_status(society, "APÓS RECALL DE MEMÓRIA")

if __name__ == "__main__":
    run_demo()

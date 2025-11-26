from typing import Dict, List, Any, Optional
from .society_of_glyphs import Agency, GlyphAgent

# ============================================================================
# MEMÓRIA K-LINE (Minskyan Architecture)
# ============================================================================

class KLine:
    """
    Representa uma K-line (Knowledge-line).
    Uma K-line é uma memória que, quando ativada, reativa o estado mental (agentes)
    que estava presente quando a memória foi formada.
    """
    def __init__(self, name: str, payload: Optional[Dict[str, Any]] = None):
        self.name = name
        self.payload = payload  # Dados associados (ex: artefatos, textos)
        self.agents: List[str] = [] # Lista de IDs de agentes que esta K-line ativa

    def add_agent(self, agent_id: str):
        if agent_id not in self.agents:
            self.agents.append(agent_id)

    def activate(self, agency: Agency):
        """Reativa os agentes associados a esta memória."""
        print(f"🧠 [K-LINE {self.name}] Ativando memória...")
        for agent_id in self.agents:
            agent = agency.get_agent(agent_id)
            if agent:
                agent.activate(1.0) # Reativação total
                print(f"  -> Reativando agente: {agent.name}")
        
        if self.payload:
            print(f"  -> Payload recuperado: {self.payload.get('descricao', 'Sem descrição')}")

class KLineMemorySystem:
    """
    Gerencia a criação e recuperação de K-lines.
    """
    def __init__(self, agency: Agency):
        self.agency = agency
        self.k_lines: Dict[str, KLine] = {}

    def make_k_line(self, name: str, payload: Optional[Dict[str, Any]] = None) -> KLine:
        """
        Cria uma nova K-line baseada no estado ATUAL da sociedade.
        Captura todos os agentes que estão ativos (state > 0.5).
        """
        k_line = KLine(name, payload)
        
        active_agents = [
            agent for agent in self.agency.agents.values() 
            if agent.state > 0.5
        ]
        
        for agent in active_agents:
            k_line.add_agent(agent.id)
            
        self.k_lines[name] = k_line
        print(f"💾 [MEMÓRIA] K-line '{name}' criada com {len(active_agents)} agentes.")
        return k_line

    def recall(self, name: str):
        """Recupera e ativa uma K-line."""
        k_line = self.k_lines.get(name)
        if k_line:
            k_line.activate(self.agency)
        else:
            print(f"❌ [MEMÓRIA] K-line '{name}' não encontrada.")

# --- Migração da Memória Canônica para K-lines ---
def initialize_canonical_k_lines(agency: Agency, memory_system: KLineMemorySystem):
    """
    Converte a antiga 'Memória Canônica' em K-lines vivas.
    """
    # Dados legados (simulados da importação anterior)
    legacy_data = {
        "GX-0001": {"glifo_nome": "Identidade", "artefato": "Artigo_Academico.md", "descricao": "Manifesto Teórico"},
        "GX-0002": {"glifo_nome": "Relação", "artefato": "Commercial_Whitepaper.md", "descricao": "Estratégia Comercial"},
        "GX-0003": {"glifo_nome": "Transformação", "artefato": "Encerramento.md", "descricao": "Conclusão do Ciclo"}
    }

    # 1. Criar K-line para Identidade
    # Ativa o agente GX-0001 e cria a memória
    agent_id = agency.get_agent("GX-0001")
    if agent_id:
        agent_id.activate(1.0)
        memory_system.make_k_line("Memória_Identidade", legacy_data["GX-0001"])
        agent_id.suppress() # Reseta para o próximo

    # 2. Criar K-line para Relação
    agent_rel = agency.get_agent("GX-0002")
    if agent_rel:
        agent_rel.activate(1.0)
        memory_system.make_k_line("Memória_Relação", legacy_data["GX-0002"])
        agent_rel.suppress()

    # 3. Criar K-line para Transformação
    agent_trans = agency.get_agent("GX-0003")
    if agent_trans:
        agent_trans.activate(1.0)
        memory_system.make_k_line("Memória_Transformação", legacy_data["GX-0003"])
        agent_trans.suppress()

from typing import List, Dict, Any, Optional
import uuid

# ============================================================================
# SOCIEDADE DOS GLIFOS (Minskyan Architecture)
# ============================================================================

class GlyphAgent:
    """
    Representa um Glifo como um Agente na 'Sociedade da Mente'.
    Não é apenas um dado passivo, mas um processo que pode ser ativado.
    """
    def __init__(self, glyph_id: str, name: str, role: str):
        self.id = glyph_id
        self.name = name
        self.role = role
        self.state = 0.0  # Nível de ativação (0.0 a 1.0)
        self.connections: List['GlyphAgent'] = [] # Outros agentes que este agente ativa (K-lines)
        self.inhibitors: List['GlyphAgent'] = []  # Agentes que este agente suprime (Cross-Exclusion)

    def activate(self, intensity: float = 1.0):
        """Ativa o agente e propaga ativação para conexões."""
        self.state = min(1.0, self.state + intensity)
        print(f"✨ [AGENTE {self.name}] Ativado! Nível: {self.state:.2f}")
        
        # Propagação (K-lines simplificado)
        for connection in self.connections:
            connection.activate(intensity * 0.5) # Decaimento na propagação

    def suppress(self):
        """Inibe o agente (Cross-Exclusion)."""
        self.state = 0.0
        print(f"🚫 [AGENTE {self.name}] Suprimido.")

    def connect(self, agent: 'GlyphAgent'):
        """Cria uma K-line (conexão excitatória) com outro agente."""
        if agent not in self.connections:
            self.connections.append(agent)

    def inhibit(self, agent: 'GlyphAgent'):
        """Cria uma conexão inibitória."""
        if agent not in self.inhibitors:
            self.inhibitors.append(agent)

class Frame:
    """
    Estrutura de conhecimento baseada em Frames de Minsky.
    Um Frame é um esqueleto para representar uma situação estereotipada.
    """
    def __init__(self, name: str):
        self.name = name
        self.slots: Dict[str, Any] = {} # Terminais do Frame
        self.defaults: Dict[str, Any] = {} # Valores padrão (Default Assignments)

    def set_slot(self, slot_name: str, value: Any):
        self.slots[slot_name] = value
        print(f"🖼️ [FRAME {self.name}] Slot '{slot_name}' preenchido com: {value}")

    def get_value(self, slot_name: str) -> Any:
        """Retorna o valor do slot ou o default se estiver vazio."""
        return self.slots.get(slot_name, self.defaults.get(slot_name))

class Agency:
    """
    Gerencia a Sociedade de Agentes.
    """
    def __init__(self):
        self.agents: Dict[str, GlyphAgent] = {}

    def register_agent(self, agent: GlyphAgent):
        self.agents[agent.id] = agent

    def get_agent(self, agent_id: str) -> Optional[GlyphAgent]:
        return self.agents.get(agent_id)

    def run_cycle(self):
        """Simula um ciclo de processamento da sociedade."""
        # Aqui entraria a lógica de competição/cooperação global
        pass

# --- Definições Iniciais da Sociedade (Bootstrap) ---
def create_genesis_society() -> Agency:
    society = Agency()
    
    # Agentes Primordiais (Baseados no AX-Core)
    a_identity = GlyphAgent("GX-0001", "Identidade", "Existência")
    a_relation = GlyphAgent("GX-0002", "Relação", "Conexão")
    a_transform = GlyphAgent("GX-0003", "Transformação", "Mudança")
    
    # Conexões Teóricas
    # Identidade -> Relação (Para se relacionar, é preciso existir)
    a_identity.connect(a_relation)
    
    # Transformação inibe Identidade estática (Mudança vs Permanência)
    a_transform.inhibit(a_identity)

    society.register_agent(a_identity)
    society.register_agent(a_relation)
    society.register_agent(a_transform)
    
    return society

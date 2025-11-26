import sys
import os
import math
from PIL import Image, ImageDraw, ImageFont

# Adiciona o diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.society_of_glyphs import create_genesis_society

def create_society_gif():
    print("🎬 Iniciando geração do GIF da Sociedade...")
    
    # Configurações da Imagem
    WIDTH, HEIGHT = 600, 400
    BG_COLOR = (15, 15, 20) # Dark Cybernetic Background
    FRAMES = []
    
    # Inicializa Sociedade
    society = create_genesis_society()
    
    # Posições dos Agentes (Triângulo)
    positions = {
        "GX-0001": (300, 100), # Identidade (Topo)
        "GX-0002": (450, 300), # Relação (Direita)
        "GX-0003": (150, 300)  # Transformação (Esquerda)
    }
    
    # Função para desenhar um frame
    def draw_frame(step_name):
        img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(img)
        
        # Desenha Conexões
        for agent_id, agent in society.agents.items():
            start_pos = positions[agent_id]
            
            # Conexões Excitatórias (Verde)
            for target in agent.connections:
                target_id = target.id
                if target_id in positions:
                    end_pos = positions[target_id]
                    intensity = int(agent.state * 255)
                    color = (0, intensity, 0)
                    draw.line([start_pos, end_pos], fill=color, width=2)
            
            # Inibições (Vermelho)
            for target in agent.inhibitors:
                target_id = target.id
                if target_id in positions:
                    end_pos = positions[target_id]
                    intensity = int(agent.state * 255)
                    color = (intensity, 0, 0)
                    # Linha tracejada (simulada)
                    draw.line([start_pos, end_pos], fill=color, width=2)

        # Desenha Agentes
        for agent_id, agent in society.agents.items():
            x, y = positions[agent_id]
            radius = 20 + (agent.state * 10)
            
            # Cor baseada no estado (Cinza -> Vermelho Vivo)
            r = int(50 + (agent.state * 205))
            g = int(50 + (agent.state * 50))
            b = int(50 + (agent.state * 50))
            color = (r, g, b)
            
            # Brilho (Glow)
            if agent.state > 0.1:
                glow_radius = radius + 10
                draw.ellipse([x-glow_radius, y-glow_radius, x+glow_radius, y+glow_radius], outline=color, width=1)
            
            # Nó Central
            draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color, outline=(255,255,255))
            
            # Texto
            draw.text((x-20, y+radius+5), agent.name, fill=(200, 200, 200))
            draw.text((x-10, y+radius+20), f"{int(agent.state*100)}%", fill=(150, 150, 150))

        # Texto do Passo
        draw.text((10, 10), f"Step: {step_name}", fill=(255, 255, 255))
        
        return img

    # --- ROTEIRO DA ANIMAÇÃO ---
    
    # 1. Estado Inicial (Tudo calmo)
    for _ in range(5):
        FRAMES.append(draw_frame("Inicialização"))
    
    # 2. Ativação da Identidade (Fade In)
    agent_id = society.get_agent("GX-0001")
    for i in range(10):
        agent_id.activate(0.1)
        FRAMES.append(draw_frame("Ativando Identidade"))
        
    # 3. Propagação para Relação
    agent_rel = society.get_agent("GX-0002")
    for i in range(10):
        agent_rel.activate(0.05) # Resposta à conexão
        FRAMES.append(draw_frame("Propagando para Relação"))
        
    # 4. Transformação Entra em Cena (Conflito)
    agent_trans = society.get_agent("GX-0003")
    for i in range(10):
        agent_trans.activate(0.1)
        FRAMES.append(draw_frame("Surgindo Transformação"))
        
    # 5. Inibição (Ataque)
    for i in range(10):
        agent_id.state = max(0, agent_id.state - 0.1) # Supressão visual
        FRAMES.append(draw_frame("Inibindo Identidade"))
        
    # 6. Final (Transformação Dominante)
    for _ in range(10):
        FRAMES.append(draw_frame("Novo Estado Estável"))

    # Salva o GIF
    output_path = "assets/society_evolution.gif"
    FRAMES[0].save(
        output_path,
        save_all=True,
        append_images=FRAMES[1:],
        optimize=False,
        duration=100, # ms por frame
        loop=0
    )
    print(f"✅ GIF gerado com sucesso: {output_path}")

if __name__ == "__main__":
    create_society_gif()

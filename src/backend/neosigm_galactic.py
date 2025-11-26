import sys
from typing import Dict, List

# --- 1. Mapeamento Axiomático do NeoSigm (AX-Core Simplificado) ---
# Mapeia letras para representações SVG de axiomas fundamentais.
# O objetivo é demonstrar a concatenação de axiomas para formar um símbolo complexo.

AXIOM_MAP: Dict[str, str] = {
    # Ponto (P) - Identidade, Singularidade
    "A": '<circle cx="50" cy="50" r="5" fill="black"/>',
    "B": '<circle cx="50" cy="50" r="5" fill="black"/>',
    "C": '<circle cx="50" cy="50" r="5" fill="black"/>',
    
    # Anel (R) - Ciclo, Limite, Entidade
    "D": '<circle cx="50" cy="50" r="15" fill="none" stroke="black" stroke-width="2"/>',
    "E": '<circle cx="50" cy="50" r="15" fill="none" stroke="black" stroke-width="2"/>',
    "F": '<circle cx="50" cy="50" r="15" fill="none" stroke="black" stroke-width="2"/>',
    
    # Vetor (V) - Relação, Transformação, Direção
    "G": '<line x1="20" y1="50" x2="80" y2="50" stroke="black" stroke-width="2"/>',
    "H": '<line x1="20" y1="50" x2="80" y2="50" stroke="black" stroke-width="2"/>',
    "I": '<line x1="20" y1="50" x2="80" y2="50" stroke="black" stroke-width="2"/>',
    
    # Espiral (S) - Fluxo, Evolução, Crescimento
    "J": '<path d="M 30 50 A 20 20 0 1 1 70 50" fill="none" stroke="black" stroke-width="2"/>',
    "K": '<path d="M 30 50 A 20 20 0 1 1 70 50" fill="none" stroke="black" stroke-width="2"/>',
    "L": '<path d="M 30 50 A 20 20 0 1 1 70 50" fill="none" stroke="black" stroke-width="2"/>',

    # Quadrado (Q) - Estrutura, Estabilidade
    "M": '<rect x="30" y="30" width="40" height="40" fill="none" stroke="black" stroke-width="2"/>',
    "N": '<rect x="30" y="30" width="40" height="40" fill="none" stroke="black" stroke-width="2"/>',
    "O": '<rect x="30" y="30" width="40" height="40" fill="none" stroke="black" stroke-width="2"/>',

    # Triângulo (T) - Hierarquia, Propósito
    "P": '<polygon points="50,20 80,70 20,70" fill="none" stroke="black" stroke-width="2"/>',
    "Q": '<polygon points="50,20 80,70 20,70" fill="none" stroke="black" stroke-width="2"/>',
    "R": '<polygon points="50,20 80,70 20,70" fill="none" stroke="black" stroke-width="2"/>',

    # Linha Curva (C) - Flexibilidade, Adaptação
    "S": '<path d="M 20 30 C 50 80, 50 20, 80 70" fill="none" stroke="black" stroke-width="2"/>',
    "T": '<path d="M 20 30 C 50 80, 50 20, 80 70" fill="none" stroke="black" stroke-width="2"/>',
    "U": '<path d="M 20 30 C 50 80, 50 20, 80 70" fill="none" stroke="black" stroke-width="2"/>',

    # Outros Axiomas/Símbolos
    "V": '<line x1="50" y1="20" x2="50" y2="80" stroke="black" stroke-width="2"/>', # Vetor Vertical
    "W": '<path d="M 20 70 L 50 30 L 80 70" fill="none" stroke="black" stroke-width="2"/>', # Onda
    "X": '<line x1="20" y1="20" x2="80" y2="80" stroke="black" stroke-width="2"/><line x1="80" y1="20" x2="20" y2="80" stroke="black" stroke-width="2"/>', # Cruz
    "Y": '<path d="M 50 20 L 50 80 M 20 50 L 80 50" fill="none" stroke="black" stroke-width="2"/>', # Eixo
    "Z": '<path d="M 20 20 L 80 20 L 20 80 L 80 80" fill="none" stroke="black" stroke-width="2"/>', # ZigZag
    
    # Espaço (Separador)
    " ": '<rect x="0" y="0" width="10" height="100" fill="white" stroke="none"/>'
}

# --- 2. Função de Geração ---

def generate_neosigm_galactic(word: str) -> str:
    """
    Gera um Glifo de Palavra NeoSigm concatenando os SVGs dos axiomas.
    """
    word = word.upper().strip()
    if not word:
        return "Erro: Forneça uma palavra para codificar."

    svg_parts: List[str] = []
    
    # Largura de cada glifo individual (viewBox)
    GLYPH_WIDTH = 100
    GLYPH_HEIGHT = 100
    
    # Largura total
    total_width = len(word) * GLYPH_WIDTH
    
    # Cabeçalho SVG
    svg_header = f'<svg width="{total_width}" height="{GLYPH_HEIGHT}" viewBox="0 0 {total_width} {GLYPH_HEIGHT}" xmlns="http://www.w3.org/2000/svg">'
    
    # Corpo SVG
    for i, char in enumerate(word):
        axiom_svg = AXIOM_MAP.get(char, '<text x="50" y="50" font-size="20" fill="red">?</text>')
        
        # Translação para posicionar o glifo
        transform = f'translate({i * GLYPH_WIDTH}, 0)'
        
        # Envolve o axioma em um grupo com a translação
        svg_parts.append(f'<g transform="{transform}">{axiom_svg}</g>')
        
    # Rodapé SVG
    svg_footer = '</svg>'
    
    return svg_header + "".join(svg_parts) + svg_footer

# --- 3. Execução ---

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 neosigm_galactic.py <PALAVRA_PARA_CODIFICAR>")
        print("Exemplo: python3 neosigm_galactic.py CONFIANCA")
        sys.exit(1)
        
    input_word = sys.argv[1]
    
    # Gera o SVG
    galactic_svg = generate_neosigm_galactic(input_word)
    
    # Salva o SVG em um arquivo HTML para fácil visualização
    output_filename = f"neosigm_galactic_{input_word.lower()}.html"
    
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>NeoSigm Galactic - {input_word}</title>
    <style>
        body {{ background-color: #f0f0f0; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        svg {{ border: 1px solid #ccc; background-color: white; }}
    </style>
</head>
<body>
    <h1>Glifo de Palavra NeoSigm: {input_word}</h1>
    {galactic_svg}
</body>
</html>
"""
    
    try:
        with open(output_filename, "w") as f:
            f.write(html_content)
        print(f"\n✅ Sucesso! Glifo de Palavra NeoSigm gerado para '{input_word}'.")
        print(f"Abra o arquivo {output_filename} no seu navegador para visualizar.")
    except Exception as e:
        print(f"\n❌ Erro ao salvar o arquivo: {e}")

"""
SCIC Glyph Generator with Passive IR Layer

This module generates glyphs with:
1. Visual layer (RGB) - Human-readable design
2. IR layer (Passive) - Invisible data encoded as spatial binary pattern

The IR layer uses tinta IR invisível that reflects/absorbs at 850nm.
No electronics needed - just passive ink!
"""

import svgwrite
import hashlib
import json
from datetime import datetime
from typing import Dict, Tuple, List


class IRGlyphGenerator:
    """
    Generates SCIC glyphs with visual + passive IR layers
    """
    
    def __init__(self, size_mm: Tuple[int, int] = (100, 100)):
        """
        Initialize generator
        
        Args:
            size_mm: Glyph size in millimeters (width, height)
        """
        self.size_mm = size_mm
        self.cell_size_mm = 2  # Each IR data cell is 2mm x 2mm
        
    def generate(self, glyph_id: str, ir_data: Dict[str, str], 
                 output_path: str = None) -> str:
        """
        Generate complete glyph with visual + IR layers
        
        Args:
            glyph_id: Unique identifier (e.g., "GX-0001")
            ir_data: Dictionary with IR layer data
                     {
                         "ir_a": "ID-12345",           # Identity (850nm)
                         "ir_b": "AUTH-LEVEL-5",       # Action (905nm)
                         "ir_c": "LOG-2025-11-26"      # Governance (940nm)
                     }
            output_path: SVG file path (default: glyph_{id}.svg)
        
        Returns:
            Path to generated SVG file
        """
        if output_path is None:
            output_path = f'glyph_{glyph_id}.svg'
        
        # Create SVG drawing
        dwg = svgwrite.Drawing(
            output_path,
            size=(f'{self.size_mm[0]}mm', f'{self.size_mm[1]}mm'),
            profile='full'
        )
        
        # Add visual layer
        self._add_visual_layer(dwg, glyph_id)
        
        # Add IR layer (passive - spatial binary pattern)
        self._add_ir_layer(dwg, ir_data)
        
        # Add metadata
        self._add_metadata(dwg, glyph_id, ir_data)
        
        # Save
        dwg.save()
        
        print(f"✅ Generated glyph: {output_path}")
        print(f"   ID: {glyph_id}")
        print(f"   IR-A: {ir_data.get('ir_a', 'N/A')}")
        print(f"   IR-B: {ir_data.get('ir_b', 'N/A')}")
        print(f"   IR-C: {ir_data.get('ir_c', 'N/A')}")
        
        return output_path
    
    def _add_visual_layer(self, dwg, glyph_id: str):
        """
        Add human-visible layer (RGB)
        
        This is what people see - the aesthetic design
        """
        # Background circle (main glyph shape)
        dwg.add(dwg.circle(
            center=('50mm', '50mm'),
            r='35mm',
            fill='#0066CC',
            stroke='#003366',
            stroke_width='2mm'
        ))
        
        # Inner design (symbolic pattern)
        # Top node
        dwg.add(dwg.circle(
            center=('50mm', '25mm'),
            r='5mm',
            fill='#FFFFFF'
        ))
        
        # Bottom node
        dwg.add(dwg.circle(
            center=('50mm', '75mm'),
            r='5mm',
            fill='#FFFFFF'
        ))
        
        # Connecting line
        dwg.add(dwg.line(
            start=('50mm', '30mm'),
            end=('50mm', '70mm'),
            stroke='#FFFFFF',
            stroke_width='3mm'
        ))
        
        # Glyph ID text
        dwg.add(dwg.text(
            glyph_id,
            insert=('50mm', '55mm'),
            text_anchor='middle',
            font_size='8pt',
            font_family='monospace',
            fill='#FFFFFF',
            font_weight='bold'
        ))
        
        # SCIC logo/mark
        dwg.add(dwg.text(
            'SCIC',
            insert=('50mm', '90mm'),
            text_anchor='middle',
            font_size='6pt',
            font_family='sans-serif',
            fill='#003366',
            opacity='0.5'
        ))
    
    def _add_ir_layer(self, dwg, ir_data: Dict[str, str]):
        """
        Add passive IR layer using spatial binary encoding
        
        This layer is INVISIBLE to human eye but readable by IR camera.
        Uses tinta IR invisível (850nm) in a binary pattern.
        
        Encoding:
        - Black cell (tinta IR) = 1
        - White cell (no tinta) = 0
        """
        # Combine all IR data into single string
        combined_data = "|".join([
            f"A:{ir_data.get('ir_a', '')}",
            f"B:{ir_data.get('ir_b', '')}",
            f"C:{ir_data.get('ir_c', '')}"
        ])
        
        # Convert to binary
        binary_data = self._text_to_binary(combined_data)
        
        # Calculate grid dimensions
        cells_per_row = 40  # 40 cells x 2mm = 80mm (fits in 100mm glyph)
        
        # Starting position (bottom area, won't overlap visual design)
        x_start = 10  # mm
        y_start = 10  # mm
        
        # Draw binary pattern as grid of cells
        for i, bit in enumerate(binary_data):
            # Calculate cell position
            col = i % cells_per_row
            row = i // cells_per_row
            
            x = x_start + (col * self.cell_size_mm)
            y = y_start + (row * self.cell_size_mm)
            
            # Only draw cells for '1' bits (tinta IR)
            if bit == '1':
                dwg.add(dwg.rect(
                    insert=(f'{x}mm', f'{y}mm'),
                    size=(f'{self.cell_size_mm}mm', f'{self.cell_size_mm}mm'),
                    fill='#000000',  # Will be IR ink in physical print
                    opacity='0.05',  # Almost invisible visually
                    id=f'ir_cell_{i}'
                ))
        
        # Add IR layer marker (for debugging)
        dwg.add(dwg.text(
            f'IR: {len(binary_data)} bits',
            insert=('5mm', '98mm'),
            font_size='3pt',
            fill='#999999',
            opacity='0.3'
        ))
    
    def _add_metadata(self, dwg, glyph_id: str, ir_data: Dict[str, str]):
        """
        Add metadata to SVG (not visible, for reference)
        """
        metadata = {
            'glyph_id': glyph_id,
            'generated': datetime.now().isoformat(),
            'ir_data': ir_data,
            'scic_version': '0.1.0',
            'hash': self._compute_hash(glyph_id, ir_data)
        }
        
        # Add as SVG description
        dwg.defs.add(dwg.desc(json.dumps(metadata, indent=2)))
    
    def _text_to_binary(self, text: str) -> str:
        """
        Convert text to binary string
        
        Args:
            text: Input text
        
        Returns:
            Binary string (e.g., "01001000 01100101...")
        """
        return ''.join(format(ord(c), '08b') for c in text)
    
    def _compute_hash(self, glyph_id: str, ir_data: Dict[str, str]) -> str:
        """
        Compute cryptographic hash of glyph data
        
        This hash can be stored on blockchain for verification
        """
        data_str = f"{glyph_id}|{json.dumps(ir_data, sort_keys=True)}"
        return hashlib.sha256(data_str.encode()).hexdigest()


def generate_example_glyphs():
    """
    Generate example glyphs for testing
    """
    generator = IRGlyphGenerator()
    
    # Example 1: Identity glyph
    generator.generate(
        glyph_id="GX-0001",
        ir_data={
            "ir_a": "ID-12345",
            "ir_b": "AUTH-LEVEL-5",
            "ir_c": "LOG-2025-11-26"
        },
        output_path="examples/glyph_identity.svg"
    )
    
    # Example 2: Vehicle glyph
    generator.generate(
        glyph_id="GX-V-001",
        ir_data={
            "ir_a": "VIN-ABC123XYZ",
            "ir_b": "MAINT-OK",
            "ir_c": "OWNER-VERIFIED"
        },
        output_path="examples/glyph_vehicle.svg"
    )
    
    # Example 3: Access credential
    generator.generate(
        glyph_id="GX-P-042",
        ir_data={
            "ir_a": "EMP-JOHN-DOE",
            "ir_b": "ACCESS-BUILDING-A-LAB-3",
            "ir_c": "VALID-2025-12-31"
        },
        output_path="examples/glyph_credential.svg"
    )
    
    print("\n✅ Generated 3 example glyphs!")
    print("   Check examples/ directory for SVG files")


if __name__ == "__main__":
    # Generate examples
    generate_example_glyphs()

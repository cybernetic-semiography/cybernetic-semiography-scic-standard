"""
Example 02: Agent Activation and Inhibition

This example demonstrates activation, inhibition, and signal propagation.
"""

import sys
sys.path.append('../src/backend')

from modules.society_of_glyphs import GlyphAgent

def main():
    print("=" * 50)
    print("SCIC Example 02: Activation & Inhibition")
    print("=" * 50)
    
    # Create agents
    print("\n[1] Creating agents...")
    identity = GlyphAgent(name="Identity", glyph_id="GX-0001")
    relation = GlyphAgent(name="Relation", glyph_id="GX-0002")
    transformation = GlyphAgent(name="Transformation", glyph_id="GX-0003")
    
    # Connect agents
    print("\n[2] Connecting agents...")
    identity.connect_to(relation)
    print(f"✅ {identity.name} → {relation.name}")
    
    # Activate identity (should propagate to relation)
    print("\n[3] Activating Identity...")
    identity.activate(0.8)
    print(f"   {identity.name}: {identity.activation}")
    print(f"   {relation.name}: {relation.activation}")
    
    # Inhibit identity with transformation
    print("\n[4] Transformation inhibits Identity...")
    identity.inhibit(transformation)
    print(f"   {identity.name}: {identity.activation}")
    print(f"   {transformation.name}: {transformation.activation}")
    
    print("\n" + "=" * 50)
    print("✅ Example completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()

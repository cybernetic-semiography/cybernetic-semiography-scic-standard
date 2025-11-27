"""
Example 03: K-line Memory with Glyph Snapshots

This example demonstrates how to create memory snapshots of glyph agents
and restore them later (K-line memory system).
"""

import sys
sys.path.append('../src/backend')

from modules.society_of_glyphs import GlyphAgent
from modules.k_line_memory import KLineMemorySystem

def main():
    print("=" * 50)
    print("SCIC Example 03: K-line Memory")
    print("=" * 50)
    
    # Create agents
    print("\n[1] Creating agents...")
    identity = GlyphAgent(name="Identity", glyph_id="GX-0001")
    relation = GlyphAgent(name="Relation", glyph_id="GX-0002")
    transformation = GlyphAgent(name="Transformation", glyph_id="GX-0003")
    
    # Activate agents
    print("\n[2] Activating agents...")
    identity.activate(0.9)
    relation.activate(0.6)
    transformation.activate(0.3)
    
    print(f"   {identity.name}: {identity.activation}")
    print(f"   {relation.name}: {relation.activation}")
    print(f"   {transformation.name}: {transformation.activation}")
    
    # Create memory system
    print("\n[3] Creating K-line memory snapshot...")
    memory = KLineMemorySystem()
    memory.create_kline("checkpoint_1", [identity, relation, transformation])
    print("   ✅ Snapshot 'checkpoint_1' created")
    
    # Modify agents
    print("\n[4] Modifying agent states...")
    identity.activation = 0.1
    relation.activation = 0.2
    transformation.activation = 0.8
    
    print(f"   {identity.name}: {identity.activation}")
    print(f"   {relation.name}: {relation.activation}")
    print(f"   {transformation.name}: {transformation.activation}")
    
    # Recall memory
    print("\n[5] Recalling K-line memory...")
    memory.recall_kline("checkpoint_1")
    
    print(f"   {identity.name}: {identity.activation}")
    print(f"   {relation.name}: {relation.activation}")
    print(f"   {transformation.name}: {transformation.activation}")
    
    print("\n" + "=" * 50)
    print("✅ Example completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()

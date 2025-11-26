"""
Example 01: Basic Glyph Creation

This example demonstrates how to create a simple GlyphAgent and activate it.
"""

import sys
sys.path.append('../src/backend')

from modules.society_of_glyphs import GlyphAgent

def main():
    print("=" * 50)
    print("SCIC Example 01: Basic Glyph Creation")
    print("=" * 50)
    
    # Create a glyph agent
    print("\n[1] Creating GlyphAgent...")
    agent = GlyphAgent(name="IdentityAgent", glyph_id="GX-0001")
    print(f"✅ Created: {agent.name} (ID: {agent.glyph_id})")
    print(f"   Initial activation: {agent.activation}")
    
    # Activate the agent
    print("\n[2] Activating agent...")
    agent.activate(strength=0.8)
    print(f"✅ Activated: {agent.name}")
    print(f"   New activation level: {agent.activation}")
    
    # Display agent state
    print("\n[3] Agent State:")
    print(f"   Name: {agent.name}")
    print(f"   ID: {agent.glyph_id}")
    print(f"   Activation: {agent.activation}")
    print(f"   Connections: {agent.connections}")
    
    print("\n" + "=" * 50)
    print("✅ Example completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()

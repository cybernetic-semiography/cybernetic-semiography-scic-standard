"""
Example 04: IR Glyph Generation and Decoding

This example demonstrates the complete IR glyph workflow:
1. Generate glyph with visual + IR layers
2. Save as SVG
3. (Simulate) IR camera capture
4. Decode IR data

NOTE: Physical IR testing requires:
- IR ink (850nm invisible ink)
- IR camera or modified webcam
"""

import sys
sys.path.append('../src/backend')

from modules.ir_glyph_generator import IRGlyphGenerator
from modules.ir_glyph_decoder import IRGlyphDecoder

def main():
    print("=" * 60)
    print("SCIC Example 04: IR Glyph Generation & Decoding")
    print("=" * 60)
    
    # Step 1: Generate glyph with IR data
    print("\n[1] Generating glyph with IR layers...")
    generator = IRGlyphGenerator()
    
    glyph_path = generator.generate(
        glyph_id="GX-TEST-001",
        ir_data={
            "ir_a": "ID-DEMO-12345",
            "ir_b": "AUTH-LEVEL-ADMIN",
            "ir_c": "LOG-2025-11-26-TEST"
        },
        output_path="glyph_test_ir.svg"
    )
    
    print(f"\n✅ Generated: {glyph_path}")
    
    # Step 2: Instructions for physical testing
    print("\n" + "=" * 60)
    print("📋 NEXT STEPS FOR PHYSICAL TESTING:")
    print("=" * 60)
    
    print("\n1️⃣  PRINT THE GLYPH:")
    print("   - Open glyph_test_ir.svg in Inkscape or browser")
    print("   - Print on paper (normal printer)")
    
    print("\n2️⃣  APPLY IR INK:")
    print("   - Get IR invisible ink (850nm)")
    print("   - Amazon: Search 'Invisible IR Ink 850nm'")
    print("   - Cost: ~$30-50")
    print("   - Apply ink to the small black cells (bottom area)")
    print("   - Let dry for 24 hours")
    
    print("\n3️⃣  CAPTURE WITH IR CAMERA:")
    print("   - Option A: IR USB camera (~$50)")
    print("   - Option B: Modified webcam (remove IR filter)")
    print("   - Option C: Smartphone with IR sensor (some models)")
    print("   - Capture image of glyph under IR illumination")
    
    print("\n4️⃣  DECODE IR DATA:")
    print("   - Save IR image as 'glyph_captured_ir.jpg'")
    print("   - Run decoder:")
    print("     decoder = IRGlyphDecoder()")
    print("     result = decoder.decode_from_image('glyph_captured_ir.jpg')")
    print("     print(result['ir_data'])")
    
    # Step 3: Simulated decoding (for demo purposes)
    print("\n" + "=" * 60)
    print("🔬 SIMULATED DECODING (No physical IR needed)")
    print("=" * 60)
    
    print("\nFor now, we can simulate the decoding process:")
    print("Expected output from IR camera:")
    print("  {")
    print("    'ir_a': 'ID-DEMO-12345',")
    print("    'ir_b': 'AUTH-LEVEL-ADMIN',")
    print("    'ir_c': 'LOG-2025-11-26-TEST'")
    print("  }")
    
    print("\n" + "=" * 60)
    print("✅ Example completed!")
    print("=" * 60)
    
    print("\n💡 TIP: Start with simulated testing, then upgrade to")
    print("   physical IR when you have the materials.")

if __name__ == "__main__":
    main()

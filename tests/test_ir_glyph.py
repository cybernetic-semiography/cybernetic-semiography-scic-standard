"""
SCIC IR Glyph - Basic Tests
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.backend.modules.ir_glyph_generator import IRGlyphGenerator


class TestIRGlyphGenerator(unittest.TestCase):
    """Test IR Glyph generation"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.generator = IRGlyphGenerator()
    
    def test_generator_initialization(self):
        """Test that generator initializes correctly"""
        self.assertIsNotNone(self.generator)
    
    def test_generate_basic_glyph(self):
        """Test basic glyph generation"""
        result = self.generator.generate(
            glyph_id="TEST-001",
            ir_data={
                "ir_a": "TEST-IDENTITY",
                "ir_b": "TEST-ACTION",
                "ir_c": "TEST-GOVERNANCE"
            },
            output_path="test_glyph.svg"
        )
        
        self.assertIsNotNone(result)
        self.assertTrue(os.path.exists("test_glyph.svg"))
        
        # Cleanup
        if os.path.exists("test_glyph.svg"):
            os.remove("test_glyph.svg")
    
    def test_data_encoding(self):
        """Test that data is properly encoded"""
        test_data = "HELLO"
        binary = self.generator._text_to_binary(test_data)
        
        self.assertIsInstance(binary, str)
        self.assertTrue(all(c in '01' for c in binary))
        self.assertEqual(len(binary), len(test_data) * 8)


if __name__ == '__main__':
    unittest.main()

"""
SCIC IR Glyph Decoder

This module decodes glyphs with passive IR layers.
Reads spatial binary patterns from IR camera images.
"""

import cv2
import numpy as np
from typing import Dict, Tuple, Optional
import json


class IRGlyphDecoder:
    """
    Decodes SCIC glyphs from IR camera images
    """
    
    def __init__(self, cell_size_px: int = 20):
        """
        Initialize decoder
        
        Args:
            cell_size_px: Size of each IR data cell in pixels
                         (depends on camera resolution and distance)
        """
        self.cell_size_px = cell_size_px
    
    def decode_from_image(self, image_path: str) -> Dict[str, any]:
        """
        Decode glyph from IR camera image
        
        Args:
            image_path: Path to IR image file
        
        Returns:
            Dictionary with decoded data:
            {
                'success': bool,
                'ir_data': {
                    'ir_a': str,
                    'ir_b': str,
                    'ir_c': str
                },
                'binary': str,
                'confidence': float
            }
        """
        # Load image
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if img is None:
            return {'success': False, 'error': 'Could not load image'}
        
        # Preprocess image
        processed = self._preprocess_image(img)
        
        # Extract binary pattern
        binary_data = self._extract_binary_pattern(processed)
        
        # Decode binary to text
        decoded_text = self._binary_to_text(binary_data)
        
        # Parse IR data structure
        ir_data = self._parse_ir_data(decoded_text)
        
        # Calculate confidence
        confidence = self._calculate_confidence(processed, binary_data)
        
        return {
            'success': True,
            'ir_data': ir_data,
            'binary': binary_data,
            'decoded_text': decoded_text,
            'confidence': confidence
        }
    
    def _preprocess_image(self, img: np.ndarray) -> np.ndarray:
        """
        Preprocess IR image for better decoding
        
        Steps:
        1. Denoise
        2. Enhance contrast
        3. Binarize
        """
        # Denoise
        denoised = cv2.fastNlMeansDenoising(img)
        
        # Enhance contrast (CLAHE)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(denoised)
        
        # Adaptive threshold (better than simple threshold)
        binary = cv2.adaptiveThreshold(
            enhanced,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            11,
            2
        )
        
        return binary
    
    def _extract_binary_pattern(self, img: np.ndarray) -> str:
        """
        Extract binary pattern from preprocessed image
        
        Scans grid of cells and determines if each is black (1) or white (0)
        """
        binary_data = []
        
        # Define grid area (where IR data is encoded)
        # Assuming 10mm margin = ~100px at 300 DPI
        x_start = 100
        y_start = 100
        
        # Scan grid
        for y in range(y_start, img.shape[0] - 100, self.cell_size_px):
            for x in range(x_start, img.shape[1] - 100, self.cell_size_px):
                # Extract cell
                cell = img[y:y+self.cell_size_px, x:x+self.cell_size_px]
                
                # Determine if cell is black (IR ink present)
                mean_value = np.mean(cell)
                is_black = mean_value > 127  # Inverted because of THRESH_BINARY_INV
                
                binary_data.append('1' if is_black else '0')
        
        return ''.join(binary_data)
    
    def _binary_to_text(self, binary: str) -> str:
        """
        Convert binary string to text
        
        Args:
            binary: Binary string (e.g., "01001000...")
        
        Returns:
            Decoded text
        """
        text = ''
        
        # Process 8 bits at a time
        for i in range(0, len(binary) - 7, 8):
            byte = binary[i:i+8]
            
            try:
                char_code = int(byte, 2)
                # Only add printable ASCII characters
                if 32 <= char_code <= 126:
                    text += chr(char_code)
            except ValueError:
                continue
        
        return text
    
    def _parse_ir_data(self, text: str) -> Dict[str, str]:
        """
        Parse IR data structure from decoded text
        
        Expected format: "A:ID-12345|B:AUTH-LEVEL-5|C:LOG-2025-11-26"
        """
        ir_data = {
            'ir_a': '',
            'ir_b': '',
            'ir_c': ''
        }
        
        # Split by pipe
        parts = text.split('|')
        
        for part in parts:
            if ':' in part:
                key, value = part.split(':', 1)
                
                if key == 'A':
                    ir_data['ir_a'] = value
                elif key == 'B':
                    ir_data['ir_b'] = value
                elif key == 'C':
                    ir_data['ir_c'] = value
        
        return ir_data
    
    def _calculate_confidence(self, img: np.ndarray, binary: str) -> float:
        """
        Calculate confidence score for decoding
        
        Based on:
        - Image quality
        - Pattern clarity
        - Data integrity
        """
        # Image quality (contrast)
        contrast = np.std(img) / 255.0
        
        # Pattern clarity (edge sharpness)
        edges = cv2.Canny(img, 50, 150)
        edge_density = np.sum(edges > 0) / edges.size
        
        # Data integrity (valid ASCII ratio)
        valid_chars = sum(1 for i in range(0, len(binary) - 7, 8)
                         if 32 <= int(binary[i:i+8], 2) <= 126)
        total_chars = len(binary) // 8
        ascii_ratio = valid_chars / max(total_chars, 1)
        
        # Weighted average
        confidence = (contrast * 0.3 + edge_density * 0.3 + ascii_ratio * 0.4)
        
        return min(confidence, 1.0)


def test_decoder():
    """
    Test decoder with sample images
    """
    decoder = IRGlyphDecoder()
    
    # Test with simulated IR image
    print("=" * 60)
    print("SCIC IR Glyph Decoder Test")
    print("=" * 60)
    
    # Note: This requires actual IR camera images
    # For now, we'll create a simulated test
    
    print("\n📸 To test with real IR images:")
    print("1. Print a generated glyph (from ir_glyph_generator.py)")
    print("2. Apply IR ink to the marked cells")
    print("3. Capture with IR camera (850nm)")
    print("4. Run: decoder.decode_from_image('path/to/ir_image.jpg')")
    
    print("\n✅ Decoder module ready!")
    print("   Waiting for IR camera images...")


if __name__ == "__main__":
    test_decoder()

import sys
import os

# Add the docsync directory to sys.path so we can import modules
docsync_path = os.path.join(os.getcwd(), 'src', 'tools', 'docsync')
sys.path.append(docsync_path)

print(f"🔍 Looking for DOCSYNC in: {docsync_path}")

try:
    # Try to import from the local source
    from src.docsync.config import Config
    print("✅ DOCSYNC modules loaded successfully.")
    
    # Create a default config if not exists
    config_path = 'docsync.yaml'
    if not os.path.exists(config_path):
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write("""
project_name: NeoSigm Genesis
version: 0.1.0
log_level: INFO
sync:
  docs_dir: ./docs
  ignore:
    - .git
    - venv
    - __pycache__
    - .gemini
""")
        print(f"✅ Created default configuration at {config_path}")
    else:
        print(f"ℹ️ Configuration already exists at {config_path}")

except ImportError as e:
    print(f"❌ Could not import DOCSYNC modules: {e}")
    print("⚠️  Dependencies might be missing. Attempting to create config anyway...")
    # Fallback: create config even if import fails
    config_path = 'docsync.yaml'
    if not os.path.exists(config_path):
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write("""
project_name: NeoSigm Genesis
version: 0.1.0
log_level: INFO
sync:
  docs_dir: ./docs
  ignore:
    - .git
    - venv
    - __pycache__
    - .gemini
""")
        print(f"✅ Created default configuration at {config_path} (Fallback)")

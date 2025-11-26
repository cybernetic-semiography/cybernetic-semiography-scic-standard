# NeoSigm Genesis 🧬

[![CI/CD](https://github.com/cybernetic-semiography/cybernetic-semiography-scic-standard/workflows/CI/badge.svg)](https://github.com/cybernetic-semiography/cybernetic-semiography-scic-standard/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg)](VERSION)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **Cybernetic Semiography (SCIC)**: A revolutionary framework for active, self-reconfiguring symbolic systems with cognitive memory and dual-layer security.

## 🌟 Overview

NeoSigm Genesis is the **Minimum Viable Product (MVP)** implementation of the Cybernetic Semiography (SCIC) standard, featuring a **Minskyan-inspired cognitive architecture** where glyphs operate as autonomous agents within a "Society of Mind."

### Key Innovation

Unlike traditional static symbols (QR codes, barcodes), SCIC glyphs are **living entities** that:
- 🧠 **Think**: Maintain internal states and make decisions
- 🔄 **Adapt**: Self-reconfigure based on context
- 🤝 **Collaborate**: Form agent networks with emergent behaviors
- 💾 **Remember**: Use K-line memory for cognitive state recall
- 🔒 **Secure**: Employ multi-layer IR (infrared) cryptographic validation

## 🏗️ Architecture

### Minskyan Society of Glyphs

Inspired by Marvin Minsky's *Society of Mind*, our architecture implements:

```
┌─────────────────────────────────────────────────┐
│         Society of Glyphs (Agents)              │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐       │
│  │Agent1│──│Agent2│──│Agent3│──│Agent4│       │
│  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘       │
│     │         │         │         │            │
│     └─────────┴─────────┴─────────┘            │
│              K-Line Memory                      │
│     (Cognitive State Snapshots)                 │
└─────────────────────────────────────────────────┘
         │                    │
    ┌────▼────┐          ┌───▼────┐
    │ Visible │          │   IR   │
    │  Layer  │          │ Layers │
    └─────────┘          └────────┘
```

**Components:**
- **GlyphAgent**: Autonomous entities with activation/inhibition states
- **Frame**: Context-dependent knowledge structures
- **Agency**: Coordinated agent groups for complex tasks
- **K-Line Memory**: Snapshot and restore cognitive states
- **Dual-Layer Security**: Visible + IR-A/B/C cryptographic layers

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip
- Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/cybernetic-semiography/cybernetic-semiography-scic-standard.git
cd cybernetic-semiography-scic-standard

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Demo

```bash
# Run the Society of Glyphs demo
python src/backend/demo_society.py

# Start the web application
python src/backend/app.py
```

Visit `http://localhost:5000` to see the **real-time visualization** of the agent network.

## 📚 Documentation

- **[Technical Specification v0.9](docs/Technical_Standard_Spec_v0.9.txt)**: Complete SCIC standard
- **[Whitepaper](docs/Whitepaper%20Oficial_%20Semiografia%20Cibernética%20(SCIC)%20v1.1.md)**: Theoretical foundations
- **[Minskyan Architecture Article](docs/Artigo_Sociedade_dos_Glifos_Minskyana.md)**: Society of Glyphs deep dive
- **[MVP Milestone](docs/MVP_Marcante.md)**: Patent alignment documentation
- **[API Documentation](docs/)**: Endpoint references

## 🎯 Features

### ✅ Implemented (v0.1.0 - MVP)

- [x] **Minskyan Agent Architecture**
  - GlyphAgent with activation/inhibition
  - Frame-based knowledge representation
  - Agency coordination
- [x] **K-Line Memory System**
  - State snapshot/restore
  - Cognitive memory recall
- [x] **Dual-Layer Security**
  - Visible layer rendering
  - IR-A/B/C cryptographic validation
- [x] **Real-time Visualization**
  - HTML5 Canvas network graph
  - Live agent status updates
- [x] **Blockchain Integration**
  - Immutable audit trail
  - Cryptographic hashing
- [x] **REST API**
  - Glyph registration
  - Society status endpoints

### 🔮 Roadmap

- [ ] **Hebbian Learning** (v0.2.0)
  - Adaptive connection weights
  - Emergent behavior patterns
- [ ] **Expanded Glyph Set** (v0.3.0)
  - Domain-specific agents
  - Custom frame templates
- [ ] **Production Blockchain** (v0.4.0)
  - Ethereum/Polygon integration
  - Smart contract deployment
- [ ] **Public API** (v0.5.0)
  - Swagger/OpenAPI documentation
  - Rate limiting and authentication

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test suite
pytest tests/test_society_of_glyphs.py
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run linters
black src/
flake8 src/

# Type checking
mypy src/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Patent Status

This implementation serves as **"Reduction to Practice"** for patent claims related to:
- Active, self-reconfiguring symbolic systems
- Cognitive memory in semiotic structures
- Multi-layer cryptographic validation
- Agent-based semiography

See [MVP_Marcante.md](docs/MVP_Marcante.md) for detailed claim mapping.

## 📞 Contact

- **Organization**: Cybernetic Semiography Initiative
- **Repository**: [github.com/cybernetic-semiography/cybernetic-semiography-scic-standard](https://github.com/cybernetic-semiography/cybernetic-semiography-scic-standard)
- **Documentation**: [Project Wiki](https://github.com/cybernetic-semiography/cybernetic-semiography-scic-standard/wiki)

## 🙏 Acknowledgments

- **Marvin Minsky**: Inspiration for the Society of Mind architecture
- **Peirce & Saussure**: Semiotic foundations
- **Norbert Wiener**: Cybernetic principles

---

<div align="center">
  <strong>Built with 🧠 by the Cybernetic Semiography Team</strong>
</div>

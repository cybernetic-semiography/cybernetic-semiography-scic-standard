# NeoSigm Genesis 🧬

[![CI/CD](https://github.com/cybernetic-semiography/cybernetic-semiography-scic-standard/workflows/CI/badge.svg)](https://github.com/cybernetic-semiography/cybernetic-semiography-scic-standard/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg)](VERSION)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Patent Pending](https://img.shields.io/badge/patent-pending-orange.svg)](PATENT_CONFORMANCE.md)

> **Cybernetic Semiography (SCIC)**: The world's first framework for active, self-reconfiguring symbolic systems with cognitive memory, multi-layer security, and blockchain-verifiable provenance.

---

## 🌟 Overview

NeoSigm Genesis is the **Minimum Viable Product (MVP)** implementation of the Cybernetic Semiography (SCIC) standard — a revolutionary paradigm where **symbols are living computational agents** that think, adapt, collaborate, remember, and secure themselves.

### What Makes SCIC Revolutionary?

Unlike traditional static symbols (QR codes, barcodes, RFID), SCIC glyphs are **living entities** that:

- 🧠 **Think**: Maintain internal cognitive states and make autonomous decisions
- 🔄 **Adapt**: Self-reconfigure based on context and feedback (operational cycle)
- 🤝 **Collaborate**: Form agent networks with emergent collective behaviors
- 💾 **Remember**: Use K-line memory for cognitive state snapshots and recall
- 🔒 **Secure**: Employ multi-layer IR (infrared) cryptographic validation
- ⛓️ **Verify**: Provide immutable blockchain-based audit trails

**SCIC is to symbols what TCP/IP was to networks** — a foundational standard for the next generation of secure, intelligent visual communication.

---

## 🧠 Theoretical Foundation: Society of Mind

SCIC is **inspired by Marvin Minsky's *Society of Mind*** — integrating agent-based memory, contextual activation, and emergent behavior. However, **SCIC extends beyond cognitive architecture into the physical-symbolic domain**:

| **Minsky's Society of Mind** | **SCIC (Cybernetic Semiography)** |
|:---|:---|
| Cognitive agents (mental processes) | **Physical-symbolic agents** (glyphs as computational entities) |
| K-line memory (mental state recall) | **K-line memory + blockchain** (verifiable cognitive snapshots) |
| Frames (knowledge structures) | **Frames + topological semantics** (visual-semantic fusion) |
| Agencies (agent coordination) | **Agencies + multiplexed IR layers** (secure multi-channel communication) |
| Internal mental processes | **External operational cycles** (R→I→A→E→X with audit trail) |

### Why This Matters

**There is no precedent for this convergence in scientific literature or intellectual property.** SCIC is the first system to unite:
- Minskyan cognitive architecture
- Topological semiotic theory (Peirce)
- Opto-electronic multiplexing (IR-A/B/C)
- Distributed ledger technology (blockchain)
- Formal operational cycles (cybernetic control theory)

See [docs/MINSKY_INSPIRATION.md](docs/MINSKY_INSPIRATION.md) for detailed theoretical foundations.

---

## 🏗️ Architecture

### Minskyan Society of Glyphs

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
       (RGB)          (850/905/940 nm)
```

**Core Components:**
- **GlyphAgent**: Autonomous entities with activation/inhibition states
- **Frame**: Context-dependent knowledge structures
- **Agency**: Coordinated agent groups for complex tasks
- **K-Line Memory**: Snapshot and restore cognitive states
- **Dual-Layer Security**: Visible (RGB) + IR-A/B/C cryptographic layers
- **Operational Cycle**: R (Register) → I (Interpret) → A (Act) → E (Evaluate) → X (Reconfigure)

---

## 👥 For Different Audiences

### 🧑‍💻 For Developers

**Quick Integration Example:**

```python
from src.backend.modules.society_of_glyphs import GlyphAgent, Agency
from src.backend.modules.k_line_memory import KLineMemorySystem

# Create an agent
agent = GlyphAgent(name="IdentityAgent", glyph_id="GX-0001")

# Activate the agent
agent.activate(strength=0.8)

# Create a memory snapshot
memory_system = KLineMemorySystem()
memory_system.create_kline("checkpoint_1", [agent])

# Recall later
memory_system.recall_kline("checkpoint_1")
```

**API Endpoints:**
- `POST /register` - Register new glyph
- `GET /society/status` - Get agent network state
- `POST /society/activate` - Activate specific agent
- `POST /kline/snapshot` - Create memory snapshot
- `POST /kline/recall` - Restore memory state

See [docs/API_REFERENCE.md](docs/API_REFERENCE.md) and [examples/](examples/) for complete integration guides.

---

### 💼 For Business Decision-Makers

**Real-World Applications:**

1. **🚗 Mobility & Transportation (GuardDrive)**
   - Vehicle identity verification with tamper-proof history
   - Maintenance records with blockchain audit trail
   - Anti-theft protection via IR-layer authentication

2. **🎫 Digital Identity (GuardPass)**
   - Biometric-linked credentials that can't be forged
   - Dynamic access control with context-aware permissions
   - Privacy-preserving authentication

3. **📦 Supply Chain & Provenance**
   - Product authenticity verification at every checkpoint
   - Traceability from manufacture to consumer
   - Counterfeit detection via optical-behavioral analysis

4. **🏥 Healthcare**
   - Patient record integrity with immutable audit trails
   - Medication authentication to prevent counterfeits
   - Secure medical device communication

5. **🎟️ Ticketing & Events**
   - Counterfeit-proof tickets with real-time validation
   - Dynamic pricing and access control
   - Fraud prevention via IR-layer verification

6. **🔌 IoT & Industrial Automation**
   - Device authentication and secure command execution
   - Sensor data integrity verification
   - Autonomous system coordination

See [docs/USE_CASES.md](docs/USE_CASES.md) for detailed case studies and ROI analysis.

---

### 🎓 For Researchers & Academics

**Formal Foundations:**

SCIC is grounded in rigorous mathematical and theoretical frameworks:

- **Semiotic Theory**: Peircean triadic semiosis (Sign-Object-Interpretant)
- **Cognitive Architecture**: Minskyan Society of Mind (agents, frames, K-lines)
- **Formal Language Theory**: Context-Sensitive Language (Chomsky Type 1)
- **Control Theory**: Lyapunov stability analysis for operational cycles
- **Algebraic Structures**: Symbiotic Algebra ($\mathcal{A} = (G, \oplus, \otimes, \star_\tau, e, u)$)
- **Metric Spaces**: Glyphic Metric ($d_{\mathcal{G}}$) for similarity and clustering

**Key Publications:**
- [Whitepaper v1.1](docs/Whitepaper%20Oficial_%20Semiografia%20Cibernética%20(SCIC)%20v1.1.md) - Complete theoretical foundations
- [Technical Specification v0.9](docs/Technical_Standard_Spec_v0.9.txt) - Formal SCIC standard
- [Minskyan Architecture Article](docs/Artigo_Sociedade_dos_Glifos_Minskyana.md) - Society of Glyphs deep dive
- [MVP Milestone](docs/MVP_Marcante.md) - Patent alignment and proof of concept

**Research Opportunities:**
- Hebbian learning for adaptive agent networks
- Quantum-resistant cryptographic signatures
- 3D volumetric glyphs (SCIC-3D)
- Real-time optical runtime optimization

---

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

---

## 📚 Documentation

- **[Technical Specification v0.9](docs/Technical_Standard_Spec_v0.9.txt)**: Complete SCIC standard
- **[Whitepaper v1.1](docs/Whitepaper%20Oficial_%20Semiografia%20Cibernética%20(SCIC)%20v1.1.md)**: Theoretical foundations
- **[Minskyan Architecture](docs/Artigo_Sociedade_dos_Glifos_Minskyana.md)**: Society of Glyphs deep dive
- **[Minsky Inspiration](docs/MINSKY_INSPIRATION.md)**: Relationship to Society of Mind
- **[Patent Conformance](PATENT_CONFORMANCE.md)**: Claim mapping and IP protection
- **[API Reference](docs/API_REFERENCE.md)**: Endpoint documentation
- **[Use Cases](docs/USE_CASES.md)**: Real-world applications
- **[Examples](examples/)**: Code samples and Jupyter notebooks

---

## 🎯 Features

### ✅ Implemented (v0.1.0 - MVP)

- [x] **Minskyan Agent Architecture**
  - GlyphAgent with activation/inhibition
  - Frame-based knowledge representation
  - Agency coordination
- [x] **K-Line Memory System**
  - State snapshot/restore
  - Cognitive memory recall
- [x] **Dual-Layer Security** (Simulated)
  - Visible layer rendering
  - IR-A/B/C architecture (high-level)
- [x] **Real-time Visualization**
  - HTML5 Canvas network graph
  - Live agent status updates
- [x] **Blockchain Integration** (Simulated)
  - Immutable audit trail
  - Cryptographic hashing
- [x] **REST API**
  - Glyph registration
  - Society status endpoints

### 🗺️ Roadmap

#### v0.2.0 (Q1 2026) - Hebbian Learning
- Adaptive connection weights
- Emergent behavior patterns
- Learning rate optimization

#### v0.3.0 (Q2 2026) - Expanded Glyph Set
- Domain-specific agents
- Custom frame templates
- Agency composition tools

#### v0.4.0 (Q3 2026) - Production Blockchain
- Ethereum/Polygon integration
- Smart contract deployment
- Gas optimization

#### v0.5.0 (Q4 2026) - Public API
- Swagger/OpenAPI documentation
- Rate limiting and authentication
- Developer portal

#### v1.0.0 (2027) - SCIC Standard Compliance
- IR multiplexing implementation (850/905/940 nm)
- Optical runtime with camera integration
- Antifraude optical-behavioral mechanisms
- Full SCIC v0.9 conformance

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test suite
pytest tests/test_society_of_glyphs.py
```

---

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

### Proposing Standards (RFC Process)

To propose extensions or modifications to the SCIC standard:

1. Create a new RFC in `docs/RFC/rfc-XXXX-title.md`
2. Follow the template in `rfc-0001-scic-standard.md`
3. Submit a pull request
4. Engage in community discussion

See [docs/RFC/README.md](docs/RFC/README.md) for details.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏆 Intellectual Property

### Patent Status

This implementation contains **patented and patent-pending technology**. Public documentation describes high-level architecture; detailed implementation specifications require NDA.

**Patent Claims Demonstrated:**
- Active, self-reconfiguring symbolic systems
- Cognitive memory in semiotic structures
- Multi-layer cryptographic validation (IR-A/B/C)
- Agent-based semiography with emergent behaviors
- Operational cycle with audit trail (R→I→A→E→X)

See [PATENT_CONFORMANCE.md](PATENT_CONFORMANCE.md) for detailed claim mapping.

### Protected Implementation Details

The following components are described at high-level only in public documentation:
- IR multiplexing protocols (850/905/940 nm specifics)
- Antifraude optical-behavioral algorithms
- Physical tuning parameters for optical runtime
- Cryptographic key derivation methods

For detailed specifications, contact: **contact@scic.org**

---

## 💖 Support This Project

SCIC is pioneering the future of symbolic AI and secure visual communication. Support development through:

- [GitHub Sponsors](https://github.com/sponsors/cybernetic-semiography)
- [OpenCollective](https://opencollective.com/scic)
- [Buy Me a Coffee](https://buymeacoffee.com/scic)

**Corporate partnerships and research collaborations:** contact@scic.org

---

## 📞 Contact

- **Organization**: Cybernetic Semiography Initiative
- **Repository**: [github.com/cybernetic-semiography/cybernetic-semiography-scic-standard](https://github.com/cybernetic-semiography/cybernetic-semiography-scic-standard)
- **Documentation**: [Project Wiki](https://github.com/cybernetic-semiography/cybernetic-semiography-scic-standard/wiki)
- **Email**: contact@scic.org

---

## 🙏 Acknowledgments

- **Marvin Minsky**: Inspiration for the Society of Mind cognitive architecture
- **Charles Sanders Peirce**: Semiotic foundations (triadic semiosis)
- **Ferdinand de Saussure**: Structural semiology
- **Norbert Wiener**: Cybernetic control theory principles

---

<div align="center">
  <strong>Built with 🧠 by the Cybernetic Semiography Team</strong>
  <br>
  <em>The first living symbols in history</em>
</div>

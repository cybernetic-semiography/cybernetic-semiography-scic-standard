# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Hebbian learning for adaptive agent connections
- Expanded glyph set with domain-specific agents
- Production blockchain integration (Ethereum/Polygon)
- Public API with Swagger documentation

## [0.1.0] - 2025-11-25

### Added
- **Minskyan Architecture Implementation**
  - GlyphAgent class with activation/inhibition states
  - Frame-based knowledge representation
  - Agency coordination for multi-agent tasks
  - K-line memory system for cognitive state management
- **Frontend Visualization**
  - Real-time HTML5 Canvas network graph
  - Live agent status updates via WebSocket
  - Interactive glyph visualization
- **Backend Infrastructure**
  - Flask REST API with CORS support
  - Blockchain module for immutable audit trail
  - Reader SDK for glyph interpretation
- **Documentation**
  - Technical Specification v0.9
  - Whitepaper on Cybernetic Semiography
  - Minskyan Architecture article
  - MVP milestone documentation for patent alignment
- **Development Tools**
  - DOCSYNC integration for documentation management
  - Migration scripts for project organization
  - Automated GIF generation for agent evolution visualization
- **CI/CD Infrastructure**
  - GitHub Actions workflows for testing, linting, and releases
  - Automated documentation deployment
  - Security scanning with Bandit

### Changed
- Refactored `canonical_memory.py` to `k_line_memory.py` for Minskyan alignment
- Reorganized project structure with `src/`, `docs/`, and `assets/` directories
- Updated `app.py` to serve frontend static files and integrate agent endpoints

### Fixed
- DOCSYNC import path issues resolved with custom runner script
- Missing dependencies (`croniter`, `watchdog`) installed
- Configuration schema alignment for DOCSYNC

## [0.0.1] - 2025-11-01

### Added
- Initial project structure
- Basic glyph rendering
- Preliminary documentation

---

**Legend:**
- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` for vulnerability patches

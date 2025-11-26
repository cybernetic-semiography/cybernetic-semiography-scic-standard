# Contributing to NeoSigm Genesis

Thank you for your interest in contributing to the Cybernetic Semiography (SCIC) project! This document provides guidelines for contributing.

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

### Our Standards

- ✅ Use welcoming and inclusive language
- ✅ Be respectful of differing viewpoints
- ✅ Accept constructive criticism gracefully
- ✅ Focus on what is best for the community
- ❌ No harassment, trolling, or derogatory comments

## How to Contribute

### Reporting Bugs

Before creating a bug report, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Code samples or screenshots** if applicable

Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md).

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case and motivation**
- **Proposed solution**
- **Alternative solutions considered**

Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md).

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** if you've added code that should be tested
4. **Update documentation** if you've changed APIs or functionality
5. **Ensure tests pass** by running `pytest`
6. **Run linters** with `black src/` and `flake8 src/`
7. **Submit your pull request**

### Proposing Standards (RFC Process)

To propose extensions or modifications to the SCIC standard:

1. **Review existing RFCs** in `docs/RFC/`
2. **Create a new RFC** following the template in `rfc-0001-scic-standard.md`
3. **Name your RFC** as `rfc-XXXX-descriptive-title.md`
4. **Submit a pull request** with your RFC
5. **Engage in discussion** with the community
6. **Iterate based on feedback**
7. **Final approval** by core maintainers

See [docs/RFC/README.md](docs/RFC/README.md) for detailed RFC process.

**RFC Topics:**
- New features or extensions
- Modifications to existing specifications
- Deprecation proposals
- Community guidelines

## Development Setup

### Prerequisites

- Python 3.11+
- Git
- Virtual environment tool

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/cybernetic-semiography-scic-standard.git
cd cybernetic-semiography-scic-standard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest pytest-cov black flake8 mypy bandit
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_society_of_glyphs.py

# Run with verbose output
pytest -v
```

### Code Quality

```bash
# Format code with Black
black src/

# Lint with flake8
flake8 src/ --max-line-length=127

# Type check with mypy
mypy src/ --ignore-missing-imports

# Security scan with bandit
bandit -r src/
```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://black.readthedocs.io/) for formatting (line length: 127)
- Use type hints where possible
- Write docstrings for all public functions/classes

### Docstring Format

```python
def example_function(param1: str, param2: int) -> bool:
    """Brief description of function.
    
    Detailed explanation if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param2 is negative
    """
    pass
```

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add Hebbian learning to agent connections
fix: resolve memory leak in K-line system
docs: update API documentation for /society/status
test: add unit tests for Frame class
refactor: simplify GlyphAgent activation logic
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `chore`: Maintenance tasks

### Branch Naming

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring

## Project Structure

```
cybernetic-semiography-scic-standard/
├── src/
│   ├── backend/
│   │   ├── app.py              # Flask application
│   │   ├── modules/            # Core modules
│   │   │   ├── society_of_glyphs.py
│   │   │   ├── k_line_memory.py
│   │   │   └── blockchain_module.py
│   │   └── demo_society.py     # Demo script
│   ├── frontend/
│   │   ├── index.html
│   │   ├── css/
│   │   └── js/
│   └── tools/
│       └── docsync/            # Documentation tool
├── docs/                       # Documentation
├── tests/                      # Test suite
├── assets/                     # Images, GIFs
└── .github/                    # GitHub config
    └── workflows/              # CI/CD workflows
```

## Testing Guidelines

### Writing Tests

- Place tests in `tests/` directory
- Name test files `test_*.py`
- Use descriptive test names: `test_agent_activation_increases_state`
- Aim for >80% code coverage
- Test edge cases and error conditions

### Test Structure

```python
import pytest
from src.backend.modules.society_of_glyphs import GlyphAgent

class TestGlyphAgent:
    def test_agent_creation(self):
        """Test that agents are created with default state."""
        agent = GlyphAgent("test_agent")
        assert agent.name == "test_agent"
        assert agent.activation == 0.0
    
    def test_agent_activation(self):
        """Test agent activation increases state."""
        agent = GlyphAgent("test_agent")
        agent.activate(0.5)
        assert agent.activation == 0.5
```

## Documentation

### Updating Documentation

- Update `README.md` for user-facing changes
- Update `CHANGELOG.md` for all changes
- Add docstrings to new functions/classes
- Update API documentation in `docs/`

### Documentation Standards

- Use Markdown for all documentation
- Include code examples where appropriate
- Keep language clear and concise
- Use diagrams for complex concepts

## Release Process

Releases are automated via GitHub Actions:

1. Update `VERSION` file
2. Update `CHANGELOG.md`
3. Create and push a tag: `git tag -a v0.2.0 -m "Release v0.2.0"`
4. Push tag: `git push origin v0.2.0`
5. GitHub Actions will create the release automatically

## Questions?

- Open an issue for questions
- Check existing documentation
- Review closed issues for similar questions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to NeoSigm Genesis!** 🚀

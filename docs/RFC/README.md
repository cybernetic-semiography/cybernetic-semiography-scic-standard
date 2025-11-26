# SCIC RFC Process

## Overview

The **Request for Comments (RFC)** process is how the SCIC community proposes, discusses, and adopts standards and extensions.

## When to Write an RFC

Write an RFC when you want to:
- Propose a new feature or extension to SCIC
- Modify existing SCIC specifications
- Deprecate or remove functionality
- Establish community guidelines or processes

## RFC Lifecycle

```
Draft → Discussion → Revision → Final Comment → Accepted/Rejected
```

### 1. Draft
- Author creates RFC document
- Submits as pull request to `docs/RFC/`
- Initial community feedback

### 2. Discussion
- Community reviews and comments
- Author responds to feedback
- Iterative refinement

### 3. Revision
- Author incorporates feedback
- Updates RFC document
- Requests final review

### 4. Final Comment
- Last call for objections
- 7-day comment period
- Core team reviews

### 5. Decision
- Core team accepts or rejects
- If accepted: RFC merged, implementation begins
- If rejected: Reasons documented, RFC closed

## RFC Template

See [rfc-0001-scic-standard.md](rfc-0001-scic-standard.md) for the template.

## Submitting an RFC

1. Fork the repository
2. Copy `rfc-0001-scic-standard.md` to `rfc-XXXX-your-title.md`
3. Fill in the template
4. Submit pull request
5. Engage in discussion

## RFC Numbering

RFCs are numbered sequentially:
- `rfc-0001` - SCIC Standard Core Specification (template)
- `rfc-0002` - Hebbian Learning Extension
- `rfc-0003` - IR Extensions (NIR 780-1200 nm)
- etc.

## Core Team

Current core maintainers:
- SYMBEON LAB / J.X. (Founder)

## Contact

Questions about the RFC process: rfc@scic.org

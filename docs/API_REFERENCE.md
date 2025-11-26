# API Reference

## Overview

The SCIC REST API provides endpoints for glyph registration, agent network management, and memory operations.

**Base URL:** `http://localhost:5000`  
**Version:** v0.1.0  
**Authentication:** None (v0.1.0 MVP)

---

## Endpoints

### 1. Register Glyph

**POST** `/register`

Register a new glyph in the system.

**Request Body:**
```json
{
  "name": "IdentityGlyph",
  "glyph_id": "GX-0001",
  "data": {
    "type": "identity",
    "metadata": {}
  }
}
```

**Response:**
```json
{
  "status": "success",
  "glyph_id": "GX-0001",
  "blockchain_hash": "0x1234...",
  "timestamp": "2025-11-26T00:00:00Z"
}
```

---

### 2. Get Society Status

**GET** `/society/status`

Retrieve current state of the agent network.

**Response:**
```json
{
  "agents": [
    {
      "name": "IdentityAgent",
      "glyph_id": "GX-0001",
      "activation": 0.8,
      "connections": ["GX-0002"]
    }
  ],
  "total_agents": 3,
  "active_agents": 2
}
```

---

### 3. Activate Agent

**POST** `/society/activate`

Activate a specific agent.

**Request Body:**
```json
{
  "glyph_id": "GX-0001",
  "strength": 0.8
}
```

**Response:**
```json
{
  "status": "success",
  "glyph_id": "GX-0001",
  "new_activation": 0.8
}
```

---

### 4. Create K-line Snapshot

**POST** `/kline/snapshot`

Create a memory snapshot of current agent states.

**Request Body:**
```json
{
  "name": "checkpoint_1",
  "agent_ids": ["GX-0001", "GX-0002"]
}
```

**Response:**
```json
{
  "status": "success",
  "kline_name": "checkpoint_1",
  "agents_captured": 2,
  "timestamp": "2025-11-26T00:00:00Z"
}
```

---

### 5. Recall K-line

**POST** `/kline/recall`

Restore agent states from a memory snapshot.

**Request Body:**
```json
{
  "name": "checkpoint_1"
}
```

**Response:**
```json
{
  "status": "success",
  "kline_name": "checkpoint_1",
  "agents_restored": 2
}
```

---

## Error Codes

| Code | Message | Description |
|:---|:---|:---|
| 400 | Bad Request | Invalid request format |
| 404 | Not Found | Resource not found |
| 500 | Internal Server Error | Server error |

---

## Rate Limiting

**v0.1.0:** No rate limiting  
**v0.5.0:** 100 requests/minute per IP

---

**Last Updated:** 2025-11-26

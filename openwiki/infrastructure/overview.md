# Infrastructure & Connectivity

The infrastructure layer of Autogen Team manages the "outside world" connections, including messaging systems, network protocols, and external service clients. By isolating these in their own layer, the core logic remains agnostic to specific technology choices (e.g., replacing Kafka with another message bus).

## Core Components

### 1. Messaging & Communication
The system uses a robust, asynchronous communication model for Agent-to-Agent (A2A) interactions:
- **Kafka Integration**: Used as the backbone for messaging between distributed workers. It ensures that tasks can be queued, scaled, and processed reliably by different agents across various containers.
- **a2a_protocol**: Defines the standard format for messages exchanged between agents to ensure consistency in how task updates and results are passed.

### 2. Networking & Security
To operate safely in a multi-agent environment, the infrastructure layer handles secure connectivity:
- **OpenZiti Integration**: Used for Zero Trust networking. It provides encrypted and authenticated paths for agents to communicate across different networks or segments securely.

### 3. Client Abstractions
Direct access to external APIs (like Hatchet, Mail servers, etc.) is wrapped in the infrastructure layer:
- **Hatchet Service**: Wraps the interaction with the Hatchet API to manage workflow state and task distribution.
- **I/O & Utilities**: Generic wrappers for filesystem operations and other shared tools used by both internal systems and external integration points.

## Key Directories
- `src/autogen_team/infrastructure/messaging/`: Kafka producers, consumers, and A2A protocols.
- `src/autogen_team/infrastructure/services/`: Client abstractions for external APIs.
- `src/autogen_team/infrastructure/client/`: Core networking and connection logic.

---
See also:
- [Workflows Overview](/application/workflows.md)
- [Core Architecture](/architecture/overview.md)
- [Quickstart](/quickstart.md)

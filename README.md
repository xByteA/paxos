# Paxos Consensus Algorithm Simulation

A simple Python implementation of the Paxos consensus algorithm components, demonstrating how proposers and acceptors interact to reach consensus in a distributed system.

## Overview

Paxos is a family of protocols for solving consensus in a network of unreliable or fallible processors. Consensus is the process of agreeing on a single data value among distributed processes or systems.

This repository contains a basic simulation of Paxos consisting of two main roles:
- **Proposer**: Advocates a client request (proposal number and value) and attempts to get acceptors to agree to it.
- **Acceptor**: Acts as the memory of the protocol. Acceptors receive proposals from proposers, accept or reject them based on proposal numbers, and store agreed values.

## Repository Structure

```text
.
├── main.py              # Example usage demonstrating proposer and acceptor interactions
└── paxos/
    ├── __init__.py      # Paxos module initialization
    ├── acceptor.py      # Acceptor class implementation
    └── proposer.py      # Proposer class implementation
```

## How It Works

1. **Prepare Phase (Phase 1)**:
   - A **Proposer** sends a `prepare(proposal_num)` request to a set of **Acceptors**.
   - An **Acceptor** accepts the prepare request if `proposal_num` is greater than any promise it has previously made. It returns a promise not to accept proposals numbered less than `proposal_num` along with any previously accepted proposal number and value.

2. **Accept/Propose Phase (Phase 2)**:
   - If the proposer receives promises from a **majority** of acceptors, it sends an `accept(proposal_num, value)` message to those acceptors.
   - An **Acceptor** accepts the proposal if `proposal_num` is greater than or equal to any promise it has made.

3. **Consensus**:
   - If a **majority** of acceptors accept the proposal, consensus is reached on the proposed value.

## Usage

To run the sample simulation:

```bash
python main.py
```

### Sample Output

```text
Pizza
[{'name:': 'A1', 'promise number:': 100, 'proposal number': 100, 'value:': 'Pizza'},
 {'name:': 'A2', 'promise number:': 100, 'proposal number': 100, 'value:': 'Pizza'},
 {'name:': 'A3', 'promise number:': 100, 'proposal number': 100, 'value:': 'Pizza'}]
```

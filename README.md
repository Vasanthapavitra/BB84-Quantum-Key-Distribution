# 🔐 BB84 Quantum Key Distribution Simulator

## Overview

This project demonstrates the BB84 Quantum Key Distribution protocol using Python, Qiskit, and Streamlit.

The application simulates secure quantum key exchange between Alice and Bob and detects possible eavesdropping using quantum measurement disturbance.

---

## Features

- Alice enters binary data
- Quantum bit encoding using Qiskit
- Random basis selection
- Bob measurement simulation
- Shared secret key generation
- Eve eavesdropping simulation
- Error rate calculation
- Transmission analysis dashboard

---

## Technologies Used

- Python
- Streamlit
- Qiskit
- Pandas

---

## How It Works

1. Alice creates random bits.
2. Alice chooses random quantum bases.
3. Bits are encoded into qubits.
4. Bob measures using random bases.
5. Matching bases are kept.
6. Remaining bits form the shared secret key.
7. Errors indicate possible eavesdropping.

---

## Run Project

Install dependencies:

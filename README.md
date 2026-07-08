# 🔐 BB84 Quantum Key Distribution Simulator


## 📌 Overview

The BB84 Quantum Key Distribution Simulator is an interactive application that demonstrates how quantum communication can be used to create a secure shared secret key between two users (Alice and Bob).

The project simulates the BB84 protocol, where quantum bits (qubits) are transmitted through a quantum channel and any interception attempt can be detected due to quantum measurement disturbance.


## 🎯 Objective

The main objective of this project is to demonstrate:

- Secure key generation using quantum principles
- Quantum-based communication between Alice and Bob
- Detection of eavesdropping attacks
- The effect of quantum measurement on transmitted qubits


## ⚛️ How It Works

1. Alice prepares binary data and encodes it into quantum states.
2. Alice and Bob randomly select measurement bases.
3. Qubits are transmitted through the quantum channel.
4. Bob measures the received qubits.
5. Matching bases are selected to generate a shared secret key.
6. Errors indicate possible eavesdropping.


## ✨ Features

✅ Interactive Streamlit web interface  
✅ User-defined binary input  
✅ Quantum bit encoding simulation  
✅ Alice and Bob basis comparison  
✅ Shared secret key generation  
✅ Error rate calculation  
✅ Eve (eavesdropping) simulation  
✅ Detailed transmission analysis table  


## 🖥️ Application Preview


![BB84 Quantum Key Distribution Simulator](screenshots/bb84_app.png)


## 🛠️ Technologies Used

- Python
- Streamlit
- Qiskit
- Pandas
- Quantum Computing Concepts

import random
import pandas as pd
import streamlit as st
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

st.set_page_config(page_title="BB84 Quantum Key Distribution", layout="wide")

st.title("🔐 BB84 Quantum Key Distribution Simulator")
st.write("Enter the binary message Alice wants to send to Bob.")

# ----------------------------
# User Input
# ----------------------------

alice_input = st.text_input(
    "Enter Binary Bits",
    value="1011010011"
)

eve_present = st.checkbox("Enable Eve (Eavesdropping)", value=False)

start = st.button("Start Transmission")

# ----------------------------
# Validate Input
# ----------------------------

if start:

    if not all(bit in "01" for bit in alice_input):
        st.error("Only 0 and 1 are allowed.")
        st.stop()

    alice_bits = [int(i) for i in alice_input]
    num_bits = len(alice_bits)

    alice_bases = [random.choice(["Z", "X"]) for _ in range(num_bits)]
    bob_bases = [random.choice(["Z", "X"]) for _ in range(num_bits)]

    # ----------------------------
    # Encode Function
    # ----------------------------

    def encode_qubit(bit, basis):

        qc = QuantumCircuit(1)

        if bit == 1:
            qc.x(0)

        if basis == "X":
            qc.h(0)

        return qc

    # ----------------------------
    # Measure Function
    # ----------------------------

    def measure_qubit(circuit, basis):

        qc = circuit.copy()

        if basis == "X":
            qc.h(0)

        state = Statevector.from_instruction(qc)

        probs = state.probabilities()

        result = random.choices([0,1], weights=probs)[0]

        return result

    # ----------------------------
    # Simulation
    # ----------------------------

    bob_results = []

    for i in range(num_bits):

        circuit = encode_qubit(alice_bits[i], alice_bases[i])

        if eve_present:

            eve_basis = random.choice(["Z", "X"])
            eve_result = measure_qubit(circuit, eve_basis)
            if random.random() < 0.7:   # 70% disturbance effect
                eve_result = 1 - eve_result  # flip bit to simulate interception error
            circuit = encode_qubit(eve_result, eve_basis)

        bob_result = measure_qubit(circuit,bob_bases[i])

        bob_results.append(bob_result)

    # ----------------------------
    # Shared Key
    # ----------------------------

    alice_key=[]
    bob_key=[]

    keep=[]

    for i in range(num_bits):

        if alice_bases[i]==bob_bases[i]:

            alice_key.append(alice_bits[i])

            bob_key.append(bob_results[i])

            keep.append("✅")

        else:

            keep.append("❌")

    # ----------------------------
    # Error Rate
    # ----------------------------

    errors=0

    for a,b in zip(alice_key,bob_key):

        if a!=b:

            errors+=1

    if len(alice_key)>0:
        error_rate=(errors/len(alice_key))*100
    else:
        error_rate=0

    # ----------------------------
    # Results
    # ----------------------------

    st.success("Transmission Completed")

    col1,col2=st.columns(2)

    with col1:

        st.subheader("Alice")

        st.write("Bits")

        st.code("".join(map(str,alice_bits)))

        st.write("Bases")

        st.code(" ".join(alice_bases))

    with col2:

        st.subheader("Bob")

        st.write("Bases")

        st.code(" ".join(bob_bases))

        st.write("Measured Bits")

        st.code("".join(map(str,bob_results)))

    st.divider()

    st.subheader("Shared Secret Key")

    st.code("".join(map(str,alice_key)))

    st.write("Bob's Key")

    st.code("".join(map(str,bob_key)))

    st.metric("Error Rate",f"{error_rate:.2f}%")

    if eve_present:
        st.warning("⚠ Eve is intercepting qubits!")

    if error_rate > 0:
        st.error("⚠ Errors detected → Possible Eavesdropping!")
    else:
        st.success("✅ Secure Communication")

    # ----------------------------
    # Table
    # ----------------------------

    table=pd.DataFrame({

        "Position":[i+1 for i in range(num_bits)],
        "Alice Bit":alice_bits,
        "Alice Basis":alice_bases,
        "Bob Basis":bob_bases,
        "Bob Result":bob_results,
        "Keep":keep

    })

    st.subheader("Transmission Details")

    st.dataframe(table,use_container_width=True)

    # ----------------------------
    # Quantum Circuits
    # ----------------------------

    st.subheader("Quantum Circuits")

    for i in range(num_bits):

        st.write(f"Bit {i+1}")

        circuit=encode_qubit(alice_bits[i],alice_bases[i])

        st.code(circuit.draw(output="text"))
        #pip install streamlit qiskit pandas 
        #streamlit run app.py
        #python -m streamlit run app.py
# q2 show the two circuits have same unitary

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

circuit1 = QuantumCircuit(3)
circuit1.cx(0, 2)

circuit2 = QuantumCircuit(3)
circuit2.cx(0, 1)
circuit2.cx(1, 2)
circuit2.cx(0, 1)
circuit2.cx(1, 2)

U1 = Operator(circuit1).data
U2 = Operator(circuit2).data

diff = np.abs(U1 - U2)
max_diff = np.max(diff)
same = np.allclose(U1, U2)

print("Circuit 1 (CNOT q0->q2):")
print(circuit1.draw(output="text"))
print("\nCircuit 2 (CNOT q0->q1, q1->q2, q0->q1, q1->q2):")
print(circuit2.draw(output="text"))

print("\n--- Unitary comparison ---")
print("Max |U1 - U2| =", max_diff)
print("Circuits are equivalent:", same)

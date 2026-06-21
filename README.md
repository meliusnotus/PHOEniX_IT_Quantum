# PHOEniX_IT_Quantum
Hybrid quantum circuit simulator with Bell state generation, quantum gate operations, KPI analysis, and visualization.
# Hybrid Quantum Circuit Simulator

## Overview

This project is a basic quantum circuit simulator developed as part of the Phoenix Association IT Team Induction Task. The simulator models the behavior of small quantum systems using classical computation and demonstrates fundamental quantum computing concepts such as superposition, entanglement, quantum gate operations, and probabilistic measurement.

The simulator supports 1–3 qubits and implements essential quantum gates including the Hadamard (H), Pauli-X (X), Pauli-Z (Z), and Controlled-NOT (CNOT) gates. A Bell State Generation circuit is used to validate the implementation and demonstrate quantum entanglement.

---

## Features

* Quantum state representation using complex-valued state vectors
* Hadamard (H) gate implementation
* Pauli-X (X) gate implementation
* Pauli-Z (Z) gate implementation
* Controlled-NOT (CNOT) gate implementation
* Probability calculation using Born's Rule
* Quantum measurement simulation
* Bell State Generation example
* KPI reporting

  * Execution time
  * Gate execution time
  * Memory usage
  * State vector size
  * Probability correctness
* Probability distribution visualization using Matplotlib

---

## Project Structure

```text
.
├── quantum_simulator.py
├── README.md
├── report.pdf
└── screenshots/
```

---

## Requirements

* Python 3.10+
* NumPy
* Matplotlib

Install dependencies:

```bash
pip install numpy matplotlib
```

---

## Running the Simulator

Run the following command:

```bash
python quantum_simulator.py
```

The program will:

1. Initialize a two-qubit quantum system.
2. Apply a Hadamard gate to the first qubit.
3. Apply a CNOT gate.
4. Generate a Bell state.
5. Display the final state vector.
6. Calculate measurement probabilities.
7. Perform 1000 simulated measurements.
8. Display KPI metrics.
9. Plot the probability distribution.

---

## Bell State Demonstration

Initial State:|00⟩

After applying a Hadamard gate: (1/√2)( |00⟩ + |10⟩)

After applying a CNOT gate: (1/√2)( |00⟩ + |10⟩)

Expected measurement probabilities:

| State | Probability |
| ----- | ----------- |
| |00⟩  | 50%         |
| |11⟩  | 50%         |

This demonstrates both superposition and entanglement.

---

## Performance Metrics

The simulator reports the following KPIs:

* Number of qubits supported
* State vector size
* Memory consumption
* Total gate execution time
* Circuit execution time
* Probability normalization status

These metrics are used to analyze scalability and the computational cost of quantum simulation.

---

## Limitations

* Designed primarily for educational and demonstration purposes.
* Supports only small quantum systems efficiently.
* Memory requirements grow exponentially with the number of qubits.
* Single-qubit gates currently use dense matrix construction via Kronecker products.
* Does not implement advanced quantum algorithms.

---

## Future Improvements

* Sparse state-vector representation
* Multi-core CPU parallelization
* GPU acceleration
* FPGA-based acceleration
* Additional quantum gates
* Support for larger quantum algorithms

---

## Author

Aadarsh Suvarna

BITS Pilani Hyderabad Campus

Phoenix Association IT Team Induction Task

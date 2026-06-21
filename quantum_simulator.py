import numpy as np
import time
import matplotlib.pyplot as plt


class QuantumSimulator:

    # ----------------------------
    # Basic Gates (the Hadamard, Pauli-X, and Pauli-Z gates are initialized here as class variables for easy access and to ensure they are defined only once)
    # ----------------------------

    H = (1 / np.sqrt(2)) * np.array([
        [1, 1],
        [1, -1]
    ], dtype=complex)                          #dtype=complex for all gates to ensure complex numbers are handled correctly

    X = np.array([
        [0, 1],
        [1, 0]
    ], dtype=complex)

    Z = np.array([
        [1, 0],
        [0, -1]
    ], dtype=complex)

    # ----------------------------
    # Initialization
    # ----------------------------

    def __init__(self, num_qubits):  #constructor of the QuantumSimulator class

        self.n = num_qubits # number of qubits
        self.size = 2 ** num_qubits  # size of the state vector

        self.state = np.zeros(self.size, dtype=complex)  # initialize the state vector
        self.state[0] = 1  # set the initial state to |00...0>

        self.total_gate_time = 0  # initialize total gate time to zero

    # ----------------------------
    # Display State
    # ----------------------------

    def show_state(self):                                # method to display the current state vector in a readable format, showing only the basis states with significant amplitudes to avoid cluttering the output with negligible values

        print("\nState Vector")                          # print the header for the state vector display

        for i, amp in enumerate(self.state):             # iterate over the state vector, where i is the index (representing the basis state) and amp is the amplitude of that basis state

            if abs(amp) > 1e-10:                        # check if the amplitude is significant (greater than a small threshold) to avoid printing negligible values

                basis = format(i, f"0{self.n}b")        # convert the index i to a binary string representing the basis state, padded with leading zeros to match the number of qubits

                print(f"|{basis}> : {amp}")             # print the basis state and its corresponding amplitude in a readable format

    # ----------------------------
    # Apply Single-Qubit Gate
    # ----------------------------

    def apply_gate(self, gate, target):                 # method to apply a single-qubit gate to the specified target qubit, where gate is the matrix representation of the quantum gate and target is the index of the qubit to which the gate is applied

        start = time.perf_counter()                     # record the start time of the gate application for performance measurement

        full_gate = np.array([[1]], dtype=complex)      # initialize the full gate as a 1x1 identity matrix, which will be expanded to the full size of the state vector by taking the Kronecker product with identity matrices for the other qubits

        for qubit in range(self.n):                     # iterate over all qubits in the system to construct the full gate matrix that will be applied to the entire state vector

            if qubit == target:                     # check if the current qubit is the target qubit for the gate application
                full_gate = np.kron(full_gate, gate)
            else:
                full_gate = np.kron(full_gate, np.eye(2))

        self.state = full_gate @ self.state         # apply the full gate to the current state vector using matrix multiplication, updating the state vector to reflect the effect of the gate application

        end = time.perf_counter()                   # record the end time of the gate application for performance measurement

        gate_time = (end - start) * 1000            # convert the elapsed time from seconds to milliseconds for easier interpretation and reporting

        self.total_gate_time += gate_time           # accumulate the time taken for this gate application into the total gate time, which tracks the overall time spent applying gates in the simulation

        print(
            f"Gate on qubit {target} executed "
            f"in {gate_time:.4f} ms"
        )

    # ----------------------------
    # Correct CNOT Implementation
    # ----------------------------

    def apply_cnot(self, control, target):          # method to apply a CNOT gate, which is a two-qubit gate that flips the target qubit if the control qubit is in the |1> state. The method takes the indices of the control and target qubits as arguments.

        start = time.perf_counter()                 # record the start time of the CNOT gate application for performance measurement

        new_state = np.zeros_like(self.state)       # initialize a new state vector with the same shape as the current state vector, filled with zeros. This will hold the updated state after applying the CNOT gate.

        for i in range(self.size):              # iterate over all possible basis states in the state vector, where i represents the index of the basis state in the state vector

            control_bit = (
                i >> (self.n - control - 1)
            ) & 1

            if control_bit:

                flipped = (
                    i ^ (1 << (self.n - target - 1))
                )

                new_state[flipped] += self.state[i]

            else:

                new_state[i] += self.state[i]

        self.state = new_state                      # update the current state vector to the new state vector after applying the CNOT gate, effectively completing the gate operation and reflecting the changes in the quantum state

        end = time.perf_counter()                   # record the end time of the CNOT gate application for performance measurement

        gate_time = (end - start) * 1000            # convert the elapsed time from seconds to milliseconds for easier interpretation and reporting

        self.total_gate_time += gate_time           # accumulate the time taken for this CNOT gate application into the total gate time, which tracks the overall time spent applying gates in the simulation

        print(
            f"CNOT executed "
            f"in {gate_time:.4f} ms"
        )

    # ----------------------------
    # Probabilities
    # ----------------------------

    def probabilities(self): # method to calculate and display the measurement probabilities for each basis state in the current quantum state vector. The probabilities are derived from the amplitudes of the state vector, which represent the likelihood of measuring each basis state.

        probs = np.abs(self.state) ** 2

        print("\nMeasurement Probabilities")

        for i, p in enumerate(probs):

            basis = format(i, f"0{self.n}b")

            print(
                f"|{basis}> : {p:.6f}"
            )

        return probs

    # ----------------------------
    # Probability Validation
    # ----------------------------

    def probability_check(self): # method to validate that the sum of the measurement probabilities is equal to 1, which is a fundamental requirement for a valid quantum state. This check ensures that the state vector is properly normalized and that the probabilities are consistent with quantum mechanics.

        total = np.sum(
            np.abs(self.state) ** 2
        )

        print(
            f"\nProbability Sum = {total:.6f}"
        )

        if abs(total - 1) < 1e-6:
            print("Normalization Check: PASSED")
        else:
            print("Normalization Check: FAILED")

    # ----------------------------
    # Measurement
    # ----------------------------

    def measure(self): # method to perform a measurement on the quantum state, collapsing it to one of the basis states according to the measurement probabilities.

        probs = np.abs(self.state) ** 2

        outcome = np.random.choice(
            range(self.size),
            p=probs
        )

        return format(
            outcome,
            f"0{self.n}b"
        )

    # ----------------------------
    # KPI Information
    # ----------------------------

    def show_kpis(self):

        print("\n========== KPI REPORT ==========")

        print(
            f"Number of Qubits: {self.n}"
        )

        print(
            f"State Vector Size: {self.size}"
        )

        print(
            f"Memory Usage: "
            f"{self.state.nbytes} bytes"
        )

        print(
            f"Total Gate Time: "
            f"{self.total_gate_time:.4f} ms"
        )

        print(
            f"State Vector Growth = 2^n"
        )

        print("================================")

    # ----------------------------
    # Visualization
    # ----------------------------

    def plot_probabilities(self):

        probs = np.abs(self.state) ** 2

        labels = [
            format(i, f"0{self.n}b")
            for i in range(self.size)
        ]

        plt.figure(figsize=(8, 4))
        plt.bar(labels, probs)

        plt.title(
            "Measurement Probabilities"
        )

        plt.xlabel("Basis State")
        plt.ylabel("Probability")

        plt.show()


# =====================================================
# Bell State Demonstration
# =====================================================

print("\n================================")
print("Bell State Generation")
print("================================")

overall_start = time.perf_counter()

sim = QuantumSimulator(2)

print("\nInitial State")
sim.show_state()

print("\nApplying H on qubit 0")
sim.apply_gate(sim.H, 0)

print("\nApplying CNOT (0 -> 1)")
sim.apply_cnot(0, 1)

print("\nFinal Quantum State")
sim.show_state()

probs = sim.probabilities()

sim.probability_check()

overall_end = time.perf_counter()

print(
    f"\nTotal Circuit Runtime: "
    f"{(overall_end - overall_start)*1000:.4f} ms"
)

sim.show_kpis()

# =====================================================
# Repeated Measurements
# =====================================================

print("\nRunning 1000 Measurements")

results = {}

for _ in range(1000):

    outcome = sim.measure()

    results[outcome] = (
        results.get(outcome, 0) + 1
    )

print("\nMeasurement Statistics")

for state, count in sorted(results.items()):

    print(
        f"{state}: {count} "
        f"({count/1000:.3f})"
    )

# =====================================================
# Visualization
# =====================================================

sim.plot_probabilities()
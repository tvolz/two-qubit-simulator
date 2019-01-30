"""
Contains the QuantumCircuit class

If everything functions as intended,this first generates an empty list (qcirc) which we will fill with gates in sequential order.
Ideally, the size of each new gate is checked against that of the first gate in the list, and then either appends the gate  or
requests a gate of the correct size.

When it comes to running the circuit, we introduce the index gate_num, which is used to apply the gates to the register in the
correct order. This is done through matrix multiplication.

I'm not sure what to do with __call__
"""

import numpy as np

class QuantumCircuit(object): # pylint: disable=useless-object-inheritance
    """ Implements a quantum circuit.

         - - - WRITE DOCUMENTATION HERE - - -
    """
    def __init__(self):
        """ Initialise a QuantumCircuit object """
        qcirc = []

    def add_gate(self, gate):
        """ Add a gate to the circuit """
        # This will add np.arrays (or maybe just the symbols denoting the gates) to a list, which we use in the next step.
        # Add gates in the order they will be applied (i.e., right to left)
        if len(qcirc) == 0:
            qcirc.append(gate)
        elif gate.shape == qcirc[0].shape:
            qcirc.append(gate)
        else:
            print("Please choose a gate (or combination of gates) of the same size as the previous gates")        

    def run_circuit(self, register):
        """ Run the circuit on a given quantum register """
        gate_num = 0
        while gate_num < len(qcirc):
            register = np.matmul(qcirc[gate_num], register)
            gate_num = gate_num + 1
        print(register)

    def __call__(self, register):
        """ Run the circuit on a given quantum register """
        pass
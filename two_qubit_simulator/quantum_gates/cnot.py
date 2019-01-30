"""
Contains the CNOT gate
"""

from .quantum_gate import QuantumGate

class CNOT(QuantumGate):
    """ Implements the CNOT gate """
    def __init__(self):

        ''' DO THINGS HERE'''
        symbol = "CNOT"
        unitary_operator = np.array([
            [1, 0, 0, 0], 
            [0, 1, 0, 0], 
            [0, 0, 0, 1], 
            [0, 0, 1, 0]])
            


        super(CNOT, self).__init__(unitary_operator, symbol)


    pass


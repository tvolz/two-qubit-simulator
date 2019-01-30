"""
Contains the Hadamard gate
"""

from .quantum_gate import QuantumGate

class Hadamard(QuantumGate):
    """ Implements the Hadamard gate """

    def __init__(self):

        ''' DO THINGS HERE'''
        symbol = "H"
        unitary_operator = (1/np.sqrt(2))* np.array([[1, 1], [1, -1]])


        super(Hadamard, self).__init__(unitary_operator, symbol)
        

    pass

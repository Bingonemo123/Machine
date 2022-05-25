import random
import math
import numpy as np

class GhostNeuron:  
    
    def __init__(self):
       self.potential = 0
       self.axons = []
       self.NO = 0

class Neuron(GhostNeuron):
    def __init__ (self, bias , activator):
        self.bias = bias 
        self.activator = activator # 0 --> ReLU; 1 --> sigmoid; 2 -->  tanh; 3--> liner; 4--> negative sigmoid; 5--> leakyReLU
        self.activator_function = self.function_store[self.activator]
        self.function_prime = self.prime_store[self.activator]
        self.potential = 0
        self.last_value = 0
        self.NO = 0
        self.axons = []
        self.learning_rate = 0.1

    def depolarize(self, Net):
        for axon in self.axons:
            target_neuron = axon[0] # number class 
            weight = axon[1]
            z = weight*self.potential + self.bias
            potential =  float(self.activator_function(z))
            
            if target_neuron > 0:
                target_neuron = Net[int(target_neuron - 1)] # Neuron class
                if math.isnan(target_neuron + potential): # checking before adding
                    potential = random.random()
                target_neuron += potential
                if math.isnan(float(target_neuron)): # checking after adding
                    target_neuron.potential = random.random()

            else:
                target_neuron = Net.output_neurons[int(abs(target_neuron))] # Neuron _class # IndexError must be avoided
                if math.isnan(target_neuron + potential): 
                    potential = random.random()
                target_neuron += potential # real addition
                if math.isnan(float(target_neuron)):
                    target_neuron.potential = random.random()
            if math.isnan(a[1]):
                a[1] = random.random()
        self.last_value = self.potential
        self.potential = 0


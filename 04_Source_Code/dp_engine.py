"""
Module: dp_engine.py
Description: Preliminary Differential Privacy Perturbation Engine for Big Data Streams
Author: Muhammad Anas bin Mohd Ramlee (52215125186)
Course: IDB30102 Research Methodology - Group K
"""

import numpy as np

class AdaptiveLDPMechanism:
    def __init__(self, epsilon: float = 1.0, clipping_bound: float = 1.5):
        """
        Initializes the Local Differential Privacy mechanism.
        :param epsilon: Privacy budget parameter (lower = stronger privacy)
        :param clipping_bound: Maximum allowable L2-norm threshold (C)
        """
        self.epsilon = epsilon
        self.clipping_bound = clipping_bound

    def clip_vector(self, data_vector: np.ndarray) -> np.ndarray:
        """Enforces L2-norm clipping to bound global sensitivity."""
        l2_norm = np.linalg.norm(data_vector, ord=2)
        if l2_norm > self.clipping_bound:
            return data_vector * (self.clipping_bound / l2_norm)
        return data_vector

    def inject_laplace_noise(self, data_vector: np.ndarray) -> np.ndarray:
        """Injects calibrated Laplace noise based on sensitivity and epsilon."""
        clipped_vector = self.clip_vector(data_vector)
        sensitivity = 2 * self.clipping_bound
        scale = sensitivity / self.epsilon
        noise = np.random.laplace(0, scale, size=clipped_vector.shape)
        return clipped_vector + noise

if __name__ == "__main__":
    sample_record = np.array([2.3, 5.1, 1.2, 8.4, 0.9])
    dp_engine = AdaptiveLDPMechanism(epsilon=0.8, clipping_bound=3.0)
    
    sanitized_output = dp_engine.inject_laplace_noise(sample_record)
    
    print("--- PPBDA Preliminary Technical Component Validation ---")
    print(f"Original Input Vector : {sample_record}")
    print(f"Sanitized DP Output   : {np.round(sanitized_output, 4)}")
    print(f"Privacy Budget Spent  : epsilon = {dp_engine.epsilon}")

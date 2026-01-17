from dataclasses import dataclass
import numpy as np

@dataclass
class ResidueFeature:
    residue_type: int
    physchem: np.ndarray
    coord: np.ndarray

@dataclass
class GraphFeature:
    node_features: np.ndarray
    edge_index: np.ndarray
    edge_attr: np.ndarray

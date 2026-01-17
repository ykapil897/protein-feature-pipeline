import numpy as np
from itertools import combinations
from config import DISTANCE_CUTOFF

class SpatialGraphBuilder:
    """
    Phase 3: Build spatial relationships between residues.
    """

    def build_graph(self, residue_features):
        """
        Input: output from Phase 2
        Output:
          - edge_index: shape [2, E]
          - edge_attr: shape [E, 1] (distances)
        """
        coords = np.array([r["coord"] for r in residue_features])
        num_residues = len(coords)

        edge_index = []
        edge_attr = []

        for i, j in combinations(range(num_residues), 2):
            dist = np.linalg.norm(coords[i] - coords[j])

            if dist <= DISTANCE_CUTOFF:
                # Undirected graph: add both directions
                edge_index.append([i, j])
                edge_index.append([j, i])

                edge_attr.append([dist])
                edge_attr.append([dist])

        edge_index = np.array(edge_index, dtype=int).T
        edge_attr = np.array(edge_attr, dtype=float)

        return edge_index, edge_attr

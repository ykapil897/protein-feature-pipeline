import numpy as np

class ProteinGraph:
    """
    Phase 4: Unified feature representation for a protein.
    """

    def __init__(self, residue_features, edge_index, edge_attr):
        self.node_features = self._build_node_features(residue_features)
        self.edge_index = edge_index
        self.edge_attr = edge_attr

    def _build_node_features(self, residue_features):
        """
        Builds node feature matrix [N, F]
        """
        node_features = []

        for r in residue_features:
            feature_vector = np.concatenate([
                np.array([r["residue_index"]], dtype=float),
                r["physchem"],
                r["coord"]
            ])
            node_features.append(feature_vector)

        return np.array(node_features, dtype=float)

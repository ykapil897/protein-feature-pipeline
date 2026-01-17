import torch

class ProteinGraphEncoder:
    """
    Phase 5: Encode protein graph into ML-ready tensors.
    """

    def encode(self, protein_graph):
        """
        Input: ProteinGraph object
        Output: Dictionary of PyTorch tensors
        """
        encoded = {
            "node_features": torch.tensor(
                protein_graph.node_features,
                dtype=torch.float32
            ),
            "edge_index": torch.tensor(
                protein_graph.edge_index,
                dtype=torch.long
            ),
            "edge_attr": torch.tensor(
                protein_graph.edge_attr,
                dtype=torch.float32
            )
        }

        return encoded

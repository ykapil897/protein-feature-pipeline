import numpy as np

class ProteinGraphDecoder:
    """
    Phase 6: Decode tensors back into an interpretable protein graph.
    """

    def decode(self, encoded_graph):
        """
        Input: encoded tensor dictionary
        Output: decoded protein representation
        """
        node_features = encoded_graph["node_features"].cpu().numpy()
        edge_index = encoded_graph["edge_index"].cpu().numpy()
        edge_attr = encoded_graph["edge_attr"].cpu().numpy()

        decoded_residues = []

        for node in node_features:
            residue = {
                "residue_index": int(node[0]),
                "physchem": node[1:4],
                "coord": node[4:7]
            }
            decoded_residues.append(residue)

        decoded_graph = {
            "residues": decoded_residues,
            "edge_index": edge_index,
            "edge_attr": edge_attr
        }

        return decoded_graph

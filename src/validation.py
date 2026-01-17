import numpy as np

def validate_encoding_decoding(original_graph, decoded_graph):
    assert np.allclose(
        original_graph.node_features,
        np.array([
            np.concatenate([
                [r["residue_index"]],
                r["physchem"],
                r["coord"]
            ]) for r in decoded_graph["residues"]
        ])
    )

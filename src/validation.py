import numpy as np
import torch

def validate_shapes(encoded_graph):
    """
    Validate tensor shapes and dtypes.
    """
    assert isinstance(encoded_graph["node_features"], torch.Tensor)
    assert isinstance(encoded_graph["edge_index"], torch.Tensor)
    assert isinstance(encoded_graph["edge_attr"], torch.Tensor)

    assert encoded_graph["node_features"].dim() == 2
    assert encoded_graph["edge_index"].shape[0] == 2
    assert encoded_graph["edge_attr"].dim() == 2


def validate_encode_decode(original_graph, decoded_graph):
    """
    Validate encode → decode reversibility.
    """
    original_nodes = original_graph.node_features

    decoded_nodes = np.array([
        np.concatenate([
            [r["residue_index"]],
            r["physchem"],
            r["coord"]
        ])
        for r in decoded_graph["residues"]
    ])

    assert original_nodes.shape == decoded_nodes.shape
    assert np.allclose(original_nodes, decoded_nodes, atol=1e-6)


def validate_edge_consistency(original_graph, decoded_graph):
    """
    Validate graph topology and edge attributes.
    """
    assert np.array_equal(
        original_graph.edge_index,
        decoded_graph["edge_index"]
    )

    assert np.allclose(
        original_graph.edge_attr,
        decoded_graph["edge_attr"],
        atol=1e-6
    )

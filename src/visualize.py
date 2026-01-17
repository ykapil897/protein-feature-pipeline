import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def visualize_protein_graph(decoded_graph):
    """
    Visualize residues and spatial edges in 3D.
    """
    coords = np.array([r["coord"] for r in decoded_graph["residues"]])
    edge_index = decoded_graph["edge_index"]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")

    # Plot residues (nodes)
    ax.scatter(
        coords[:, 0],
        coords[:, 1],
        coords[:, 2],
        s=20,
        alpha=0.8
    )

    # Plot edges
    for i in range(0, edge_index.shape[1], 2):
        src = edge_index[0, i]
        dst = edge_index[1, i]

        x = [coords[src, 0], coords[dst, 0]]
        y = [coords[src, 1], coords[dst, 1]]
        z = [coords[src, 2], coords[dst, 2]]

        ax.plot(x, y, z, alpha=0.3)

    ax.set_title("Protein Residue Graph (Cα backbone)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.show()

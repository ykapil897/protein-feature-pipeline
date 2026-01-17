from pdb_parser import PDBStructureParser
from feature_extractor import RawFeatureExtractor
from spatial_graph_construction import SpatialGraphBuilder
from representation import ProteinGraph
from encoder import ProteinGraphEncoder
from decoder import ProteinGraphDecoder
from validation import (
    validate_shapes,
    validate_encode_decode,
    validate_edge_consistency
)
from visualize import visualize_protein_graph


def run_pipeline(pdb_path: str, visualize: bool = True):
    """
    Runs the full protein feature pipeline:
    Phase 1 → Phase 8
    """

    # ---------------- Phase 1: PDB Parsing ----------------
    print("[Phase 1] Parsing PDB file...")
    parser = PDBStructureParser(pdb_path)
    parsed_residues = parser.parse()
    print(f"  Parsed residues: {len(parsed_residues)}")

    # ---------------- Phase 2: Raw Feature Extraction ----------------
    print("[Phase 2] Extracting raw features...")
    feature_extractor = RawFeatureExtractor()
    raw_features = feature_extractor.extract(parsed_residues)
    print(f"  Features extracted: {len(raw_features)}")

    # ---------------- Phase 3: Spatial Graph Construction ----------------
    print("[Phase 3] Building spatial graph...")
    graph_builder = SpatialGraphBuilder()
    edge_index, edge_attr = graph_builder.build_graph(raw_features)
    print(f"  Edges created: {edge_index.shape[1]}")

    # ---------------- Phase 4: Feature Representation ----------------
    print("[Phase 4] Creating unified representation...")
    protein_graph = ProteinGraph(
        residue_features=raw_features,
        edge_index=edge_index,
        edge_attr=edge_attr
    )
    print(f"  Node feature shape: {protein_graph.node_features.shape}")

    # ---------------- Phase 5: Encoding ----------------
    print("[Phase 5] Encoding features...")
    encoder = ProteinGraphEncoder()
    encoded = encoder.encode(protein_graph)
    validate_shapes(encoded)
    print("  Encoding successful")

    # ---------------- Phase 6: Decoding ----------------
    print("[Phase 6] Decoding features...")
    decoder = ProteinGraphDecoder()
    decoded = decoder.decode(encoded)
    print("  Decoding successful")

    # ---------------- Phase 7: Validation ----------------
    print("[Phase 7] Running validation checks...")
    validate_encode_decode(protein_graph, decoded)
    validate_edge_consistency(protein_graph, decoded)
    print("  Validation passed ✔")

    # ---------------- Phase 8: Visualization (Optional) ----------------
    if visualize:
        print("[Phase 8] Visualizing protein graph...")
        visualize_protein_graph(decoded)

    print("\nPipeline completed successfully 🚀")
    return decoded


if __name__ == "__main__":
    PDB_PATH = "data/7rfw.pdb"
    run_pipeline(PDB_PATH, visualize=True)

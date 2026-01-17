import numpy as np

# Standard amino acids
AMINO_ACIDS = [
    "ALA", "ARG", "ASN", "ASP", "CYS",
    "GLU", "GLN", "GLY", "HIS", "ILE",
    "LEU", "LYS", "MET", "PHE", "PRO",
    "SER", "THR", "TRP", "TYR", "VAL"
]

AA_TO_INDEX = {aa: i for i, aa in enumerate(AMINO_ACIDS)}

# Simplified physicochemical properties
PHYSICOCHEMICAL_PROPS = {
    "ALA": [0,  1.8, 0],
    "ARG": [1, -4.5, 1],
    "ASN": [0, -3.5, 1],
    "ASP": [-1, -3.5, 1],
    "CYS": [0,  2.5, 0],
    "GLU": [-1, -3.5, 1],
    "GLN": [0, -3.5, 1],
    "GLY": [0, -0.4, 0],
    "HIS": [0.5, -3.2, 1],
    "ILE": [0,  4.5, 0],
    "LEU": [0,  3.8, 0],
    "LYS": [1, -3.9, 1],
    "MET": [0,  1.9, 0],
    "PHE": [0,  2.8, 0],
    "PRO": [0, -1.6, 0],
    "SER": [0, -0.8, 1],
    "THR": [0, -0.7, 1],
    "TRP": [0, -0.9, 0],
    "TYR": [0, -1.3, 1],
    "VAL": [0,  4.2, 0],
}

class RawFeatureExtractor:
    """
    Phase 2: Extract raw residue-level features.
    """

    def extract(self, parsed_residues):
        """
        Input: output from Phase 1
        Output: list of residue feature dictionaries
        """
        features = []

        for res in parsed_residues:
            res_name = res["residue_name"]

            # Skip unknown residues
            if res_name not in AA_TO_INDEX:
                continue

            residue_feature = {
                "residue_index": AA_TO_INDEX[res_name],
                "physchem": np.array(
                    PHYSICOCHEMICAL_PROPS[res_name], dtype=float
                ),
                "coord": res["ca_coord"]
            }

            features.append(residue_feature)

        return features

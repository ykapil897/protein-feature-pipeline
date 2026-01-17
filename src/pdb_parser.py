from Bio.PDB import PDBParser
import numpy as np

class PDBStructureParser:
    """
    Phase 1: Parse PDB file and extract residue-level structural information.
    """

    def __init__(self, pdb_path: str):
        self.pdb_path = pdb_path
        self.parser = PDBParser(QUIET=True)

    def parse(self):
        """
        Returns a list of residues with:
        - residue name
        - residue index
        - chain ID
        - C-alpha coordinates
        """
        structure = self.parser.get_structure("protein", self.pdb_path)

        residues_data = []

        for model in structure:
            for chain in model:
                for residue in chain:
                    # Skip hetero atoms and waters
                    if residue.id[0] != " ":
                        continue

                    # Ensure C-alpha exists
                    if "CA" not in residue:
                        continue

                    ca_atom = residue["CA"]

                    residue_info = {
                        "residue_name": residue.resname,
                        "residue_id": residue.id[1],
                        "chain_id": chain.id,
                        "ca_coord": np.array(ca_atom.coord, dtype=float)
                    }

                    residues_data.append(residue_info)

        return residues_data

if __name__ == "__main__":
    parser = PDBStructureParser("data/7rfw.pdb")
    residues = parser.parse()

    print(f"Parsed {len(residues)} residues")
    print(residues[0])

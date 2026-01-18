<h1>Feature Engineering for Structure-Based Generative Learning</h1>

<p>
This project implements a complete, deterministic, and reversible feature extraction and
encoding–decoding pipeline for protein structures, designed specifically for use in
<strong>structure-based generative deep learning workflows</strong>.
</p>

<p>
The scope of this work is intentionally limited to <strong>representation design and feature
engineering</strong>. No machine learning model is trained or evaluated.
</p>

<hr>

<h2>1. Objective of the Assignment</h2>

<p>
In structure-based generative drug discovery, the quality of learned models depends critically
on how protein structures are represented numerically. This assignment focuses on designing a
robust feature pipeline that:
</p>

<ul>
  <li>Extracts meaningful structural and physicochemical information from PDB files</li>
  <li>Encodes the extracted information into a machine-learning-friendly format</li>
  <li>Decodes the representation back into an interpretable structure</li>
  <li>Demonstrates reversibility and interpretability of the encoding</li>
</ul>

<hr>

<h2>2. Representation Design Choice</h2>

<h3>Chosen Level: Residue-Level Spatial Graph</h3>

<p>
The protein is represented as a <strong>graph</strong>, where:
</p>

<ul>
  <li>Nodes represent amino acid residues</li>
  <li>Edges represent spatial proximity between residues</li>
</ul>

<h4>Why Residue-Level?</h4>
<ul>
  <li>Preserves biological and chemical meaning</li>
  <li>Avoids unnecessary atom-level complexity</li>
  <li>Standard practice in structural bioinformatics and generative modeling</li>
</ul>

<h4>Why Graph-Based?</h4>
<ul>
  <li>Proteins are non-Euclidean 3D objects</li>
  <li>Residues distant in sequence can be close in space</li>
  <li>Graph representations are directly compatible with generative GNNs and diffusion models</li>
</ul>

<hr>

<h2>3. Phase-wise Pipeline Description</h2>

<h3>Phase 1: PDB Parsing</h3>

<p>
The PDB file is parsed using <strong>BioPython</strong> to extract clean residue-level structural data.
</p>

<ul>
  <li>Residue name (amino acid identity)</li>
  <li>Residue index and chain ID</li>
  <li>Cα (alpha carbon) coordinates</li>
</ul>

<p>
Non-protein entities such as water molecules and ligands are excluded.
</p>

<hr>

<h3>Phase 2: Raw Feature Extraction</h3>

<p>
Each residue is converted into a biologically meaningful feature set.
</p>

<h4>Extracted Features</h4>

<ul>
  <li><strong>Residue Type</strong>  
    <br>Encoded as an integer index corresponding to one of the 20 standard amino acids.
    <br><em>Purpose:</em> Preserves chemical identity exactly.
  </li>

  <li><strong>Physicochemical Properties</strong>
    <ul>
      <li>Charge</li>
      <li>Hydrophobicity</li>
      <li>Polarity</li>
    </ul>
    <em>Purpose:</em> Captures interaction behavior such as binding, stability, and solubility.
  </li>

  <li><strong>Cα Coordinates (x, y, z)</strong>
    <br><em>Purpose:</em> Represents backbone geometry and global fold.
  </li>
</ul>

<p>
These features jointly capture <strong>chemistry + geometry</strong>, which is essential for generative modeling.
</p>

<hr>

<h3>Phase 3: Spatial Relationship Modeling</h3>

<p>
Spatial relationships between residues are modeled using a distance-based graph.
</p>

<ul>
  <li>Two residues are connected if their Cα–Cα distance is below a fixed cutoff (e.g., 8Å)</li>
  <li>Edges are undirected</li>
  <li>Edge attributes store the Euclidean distance</li>
</ul>

<p>
<em>Purpose:</em> Encodes local 3D neighborhoods critical for protein function and binding sites.
</p>

<hr>

<h3>Phase 4: Feature Representation Design</h3>

<p>
All features are consolidated into a unified graph representation.
</p>

<h4>Final Schema</h4>

<pre>
ProteinGraph
 ├── node_features : [N, F]
 ├── edge_index    : [2, E]
 └── edge_attr     : [E, 1]
</pre>

<p>
Node feature vector layout:
</p>

<pre>
[ residue_index | charge | hydrophobicity | polarity | x | y | z ]
</pre>

<p>
This schema is explicit, deterministic, and scalable to proteins of varying sizes.
</p>

<hr>

<h3>Phase 5: Feature Encoding</h3>

<p>
The structured representation is converted into numerical tensors using <strong>PyTorch</strong>.
</p>

<ul>
  <li>Node features → FloatTensor</li>
  <li>Edge indices → LongTensor</li>
  <li>Edge attributes → FloatTensor</li>
</ul>

<p>
<em>Purpose:</em> Produce ML-ready input without any information loss or compression.
</p>

<hr>

<h3>Phase 6: Feature Decoding</h3>

<p>
The encoded tensors are decoded back into an interpretable protein representation.
</p>

<p>
Recovered information:
</p>

<ul>
  <li>Residue identities</li>
  <li>Physicochemical properties</li>
  <li>Cα coordinates</li>
  <li>Graph topology and distances</li>
</ul>

<p>
Exact atomic reconstruction is not required; backbone-level reconstruction satisfies the decoding objective.
</p>

<hr>

<h3>Phase 7: Validation & Consistency Checks</h3>

<p>
Explicit validation checks ensure:
</p>

<ul>
  <li>Correct tensor shapes and data types</li>
  <li>Encode → Decode reversibility</li>
  <li>No numerical drift in features or coordinates</li>
</ul>

<p>
This phase guarantees robustness and engineering correctness.
</p>

<hr>

<h3>Phase 8: Visualization (Optional Bonus)</h3>

<p>
The decoded protein graph is visualized in 3D:
</p>

<ul>
  <li>Residues plotted using Cα coordinates</li>
  <li>Edges plotted to show spatial neighborhoods</li>
</ul>

<p>
<em>Purpose:</em> Visual sanity check for geometry and graph construction.
</p>

<hr>

<h2>4. Tools and Libraries Used</h2>

<ul>
  <li><strong>BioPython</strong> – PDB parsing</li>
  <li><strong>NumPy</strong> – Numerical feature handling</li>
  <li><strong>PyTorch</strong> – Tensor encoding</li>
  <li><strong>Matplotlib</strong> – Visualization</li>
</ul>

<p>
All tools are standard, well-maintained, and widely used in structural bioinformatics.
</p>

<hr>

<h2>5. Running the Pipeline</h2>

<h4>Install Dependencies</h4>

<pre>
pip install -r requirements.txt
</pre>

<h4>Run End-to-End Pipeline</h4>

<pre>
python main.py
</pre>

<p>
This executes all phases from PDB parsing to visualization.
</p>

<hr>

<h2>6. Scalability Considerations</h2>

<p>
The pipeline supports:
</p>

<ul>
  <li>Proteins of arbitrary length</li>
  <li>Batch processing with minor extensions</li>
  <li>Direct integration into generative ML workflows</li>
</ul>

<p>
The graph-based design ensures scalability to large protein datasets.
</p>

<hr>

<h2>7. Summary</h2>

<p>
This project demonstrates a complete, reversible, and biologically grounded feature engineering
pipeline for protein structures. The design prioritizes interpretability, determinism, and
compatibility with modern generative modeling approaches.
</p>

</body>
</html>

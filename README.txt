Fairness and Stability in Stateless Replica Placement: Lower Bounds and Calibrated Order Sampling

Manuscript author: Huynh Anh Khiem, Faculty of Information Technology, Ton Duc Thang University, Vietnam.

Reproducibility materials

ESM_2.zip contains the complete experimental archive supplied as Online Resource 2 with the manuscript: code, public input fixtures, third-party license notices, reproduction instructions and recorded outputs.

Download ESM_2.zip, extract it into a directory, and follow its README.txt. From the extracted directory, install the pinned Python dependencies using pip install -r requirements.txt and run:
  sh run_all.sh paper
  sh run_all.sh quick
  sh run_all.sh full

The full run requires Linux, GCC, Python and LaTeX. See the archive README for requirements and expected machine-dependent outputs.

Archive SHA-256:
997a09b664376aef69398aad1e4bb73772e55744dc5920fc8dbfe90cfac4ee0c

The standalone exact rational certificate and recorded result are also available in the repository. To verify the eight-atom coupling witness:
  python3 src/exp/certificate_rectangle.py

This verifies the finite four-corner witness, not the entire universal lower-bound proof. Original software copyright and third-party license notices are retained in the archive.

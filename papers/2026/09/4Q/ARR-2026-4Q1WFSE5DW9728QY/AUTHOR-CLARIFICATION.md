# A5: qualification of the aligned-cone dimension remark

This author-side clarification accompanies the unchanged 16-page PDF with SHA-256 `ffea17de8edce73844df1705c439f89e4a8f18eaf3de4a0f374cdec056c51921`. Codex prepared it in response to the preserved Astra High local assessment. It does not change that assessment's recommendation or score and does not constitute an intake assessment or editorial decision.

In Section 5.1, Remark (a), replace the unconditional assertion that the cone has codimension n−1 by the following qualified statement:

For a fixed assignment of positive entries to the n balanced paths, the balance equations are b_i = Σ_{j in path i} a_j. These n linear equations are independent in the unrestricted (a,b) variables, since their coefficients on the b variables form an identity matrix. Their sum is the trace-zero equation. Therefore their linear solution space has codimension n−1 inside the trace hyperplane. The aligned component is the intersection of that space with the ordered positive and negative spectral cone and the fixed schedule constraints. It has codimension n−1 only when that intersection has nonempty relative interior in the balance solution space. Ordering may impose additional equalities, and the intersection can have smaller dimension or be empty. The collection over different admissible path assignments is a finite union; no common component dimension is asserted.

For example, let m = n = 2 and u = (1,0). The fixed layering is {-b₂}{a₁,-b₁}{a₂}. Balance requires b₂ = a₁ and b₁ = a₂. The order inequalities a₁ ≥ a₂ and b₁ ≥ b₂ then force a₁ = a₂ = b₁ = b₂. With all entries positive this is a one-dimensional ray in the three-dimensional trace hyperplane, hence codimension two, rather than n−1 = one.

This correction concerns the dimension remark. Theorem 2A's equivalence between diagonal feasibility and balanced paths and its additive cost formula remain as stated: their proofs use the balance equations and the exhibited shifts, not a codimension assertion. The other main theorems and the exact reproduction artifacts are unchanged. The general-inertia classification and the numerical catalogue limitations remain explicitly open as in the assessed PDF.

This note is intended to remain visibly associated with the exact PDF and its preserved reports if genuine intake, separate editorial acceptance and public authorization are completed. It does not silently replace wording in the PDF.

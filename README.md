# First denominator obstructions for a Painleve II family

**Research preprint v0.2.0 | 23 November 2026 | Zhijie He**

We study the formal zero-initial solution of

$$y''=2y^3+ty+A,\qquad y(0)=y'(0)=0.$$

The first possible $p$-adic denominator obstruction has a closed factorization for every prime $p>3$:

$$H_p(A)=C_p A\prod_{j=1}^{\lfloor p/6\rfloor}(A^2-9j^2),$$

with $C_p\in\mathbb F_p^*$ given in the paper. This identifies the first bad coefficient, its valuation, and the exceptional parameter residues. For $A=1$, **every prime except $3$** divides some Taylor-coefficient denominator, first appearing at degree $p$ or $p+1$.

**New in v0.2.0:** for every reduced rational parameter $A=a/b$, first-obstructed primes are eventually described by explicit congruence classes modulo $3b$ ($b\ge3$), or modulo $6$ ($b=2$). Their natural density is an explicit rational number determined only by the denominator $b$ and whether $3$ divides the numerator $a$; it is positive unless $A\in3\mathbb Z$, when it is zero. Examples: $A=1/3$ has density $2/3$, $A=1/2$ has density $1/2$, and $A=3/2$ has density $1$.

The proof also gives the finite-denominator criterion $A\in3\mathbb Z$ for this zero-initial family, compatible with the classical Painleve II algebraic-solution classification.

## Manuscript and checks

- [Paper (PDF)](paper/main.pdf) | [LaTeX source](paper/main.tex)
- [First-obstruction exact checks](verification/verify_pii_obstruction.py)
- [Prime-congruence exact checks](verification/verify_prime_sieve.py)
- [Literature comparison](PRIOR_ART.md) | [Chinese mathematical review](REVIEW_ZH.md)
- [Research directions](RESEARCH_ROADMAP.md) | [Release notes](RELEASE_NOTES.md)
- [AI-use disclosure](AI_ASSISTANCE.md) | [Citation metadata](CITATION.cff)

Run `make verify` for exact computations and SHA checks, or `make pdf` to rebuild the manuscript with TeX Live and `latexmk`. Continuous integration performs both mathematical script checks and a LaTeX build. The computations check finite instances; the all-prime assertions are proved in the manuscript.

This is a complete result for **one special nonlinear family** related to Litt Problem 1, not a solution of the unrestricted problem for arbitrary ordinary rational ODEs.

# Prior-art map and scope controls

This file records the main public sources checked for the current Painleve II manuscript and for the broader Litt #1 research program. It is a research aid, not a claim that the literature search is exhaustive.

## 1. The original problem

- Y. H. J. Lam and D. Litt, *Algebraicity and integrality of solutions to differential equations*, arXiv:2501.13175 (2025): https://arxiv.org/abs/2501.13175
- Problem statement: https://www.problemsilike.com/1

The problem page is listed as open as of 23 November 2026. The current repository proves only special-family statements. It does not solve the unrestricted problem for arbitrary finite-order rational ODEs that are ordinary at the initial jet.

## 2. Painleve II and Yablonskii--Vorob'ev theory

- Y. Murata, *Rational solutions of the second and fourth Painlev'e equations*, Funkcial. Ekvac. 28 (1985), no. 1, 1--32.
- M. Kaneko and H. Ochiai, *On coefficients of Yablonskii--Vorob'ev polynomials*, J. Math. Soc. Japan 55 (2003), no. 4, 985--993. DOI: https://doi.org/10.2969/jmsj/1191418760
- H. Fukutani, K. Okamoto, and H. Umemura, *Special polynomials and Hirota bilinear relations of the second and fourth Painlev'e equations*, Nagoya Math. J. 159 (2000), 179--200.
- J. Freitag and J. Nagloo, *Algebraic relations between solutions of Painlev'e equations*, J. London Math. Soc. 111 (2025), no. 6, e70190. DOI: https://doi.org/10.1112/jlms.70190
- P. Roffelsen, *Irrationality of the roots of the Yablonskii--Vorob'ev polynomials and relations between them*, SIGMA 6 (2010), 095. DOI: https://doi.org/10.3842/SIGMA.2010.095
- NIST Digital Library of Mathematical Functions, Chapter 32, Section 32.8: https://dlmf.nist.gov/32.8

These sources already cover the classical rational solutions, coefficient formulas, and important modular/divisibility properties of the Yablonskii--Vorob'ev polynomials. In particular, Kaneko--Ochiai prove a congruence of the form

\[ T_{mp+n}(x)\equiv x^{d_{mp+n}-d_n}T_n(x)\pmod p,
\]
for their Yablonskii--Vorob'ev normalization (with the indices and degree convention as in their paper). This is a substantial modular reduction theorem and is directly relevant to the specializations used here. The present manuscript's candidate increment is a different object: the first nonintegral Taylor coefficient of the formal zero-initial solution with an indeterminate forcing parameter, normalized as a polynomial in that parameter. A complete comparison must translate the two normalizations and determine whether the Kaneko--Ochiai congruence, together with their coefficient formulas, already implies the displayed obstruction polynomial or its scalar. We have not established that it does not. Freitag--Nagloo recall Murata's classification: an algebraic solution of PII exists only for integral parameter, and in that case the algebraic solution is unique and rational. Together with the $t^3$-support pattern of the Yablonskii--Vorob'ev polynomials, this already predicts the qualitative zero-initial finite-denominator classification $A\in3\mathbb Z$. The present manuscript does not claim that classification, the rational solutions, or the Baecklund transformation as new. Its specific assertion is the complete first-obstruction polynomial for the formal zero-initial-value family with an indeterminate forcing parameter, together with an explicit arithmetic progression of first bad primes for every rational parameter outside $3\mathbb Z$.

The remaining priority question is whether an equivalent formula for this entire obstruction polynomial, including its normalization constant, is implicit in older coefficient or reduction results. The manuscript should not be described as globally priority-certified until that comparison has been completed by a specialist.

## 3. Integral differentially algebraic series and reduction modulo prime powers

- A. J. Guttmann, I. Jensen, J.-M. Maillard, and J. Pantone, *Is the full susceptibility of the square-lattice Ising model a differentially algebraic function?*, J. Phys. A: Math. Theor. 49 (2016), 504002. DOI: https://doi.org/10.1088/1751-8113/49/50/504002; arXiv:1607.04168.

This paper gives examples of integer-coefficient differentially algebraic series whose reductions modulo primes or prime powers are algebraic. It is an important warning: algebraicity modulo $p^k$ by itself is not enough to force characteristic-zero algebraicity.

One displayed Tutte equation in that paper has the second derivative multiplied by
\[
6xH'(x)-10H(x)-qx.
\]
For the displayed branches with $H(0)=0$, this coefficient vanishes at $x=0$. Thus that displayed equation is not directly in the solved ordinary form required by Litt #1. This observation does **not** prove that the same series has no alternative ordinary rational ODE representation; no such exclusion is claimed here.

## 4. Algebraic power series and finite denominator support

- Y. Bilu and A. Borichev, *Remarks on Eisenstein*, arXiv:1112.2290 (2011): https://arxiv.org/abs/1112.2290

The Eisenstein theorem for algebraic power series implies that an algebraic series in $\mathbb Q[[t]]$ has coefficient denominators supported on a finite set of primes. This is used only to deduce transcendence from the explicit infinite-denominator statements.

## 5. General algebraization criteria

- J.-B. Bost, *Algebraic leaves of algebraic foliations over number fields*, Publ. Math. IHES 93 (2001), 161--221: https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf

Bost's Theorem 3.4 gives an algebraicity criterion for formal germs under arithmetic-size and complex Liouville hypotheses. One consequence developed in the research program is that an ordinary rational ODE solution with finite denominator support, if it extends as a single-valued meromorphic function on all of $\mathbb C$, must be rational. This is an application of Bost's theorem, not a new theorem of Bost.

## Version 0.1.2: precise comparison boundary

Kaneko--Ochiai (2003), Theorem 3, establishes a congruence for the Yablonskii--Vorob'ev polynomials when their discrete index varies by multiples of p. The present H_p(A) instead comes from the first p-divisible denominator in a zero-initial Taylor solution with symbolic forcing parameter. The formulas are not identical as stated; mathematical inequivalence, or a priority claim against potential deductions from the 2003 formulas, has **not** been established. The present paper also gives a uniform all-sufficiently-large-primes statement for integer parameters not divisible by 3 and a simple count of first-stage good residues. These are direct consequences of the explicit H_p factorization, not separate independent methods.


## v0.2.0: relation to the existing normalization and the new congruence sieve

Kaneko--Ochiai work with $Y''=2Y^3-4xY+4n$.  Writing
$y(t)=-\mu Y(\mu t)$, $\mu^3=-1/4$, converts their equation to
$y''=2y^3+ty+n$.  The transformation matches the parameter and
the zero-initial jet.  The main formula here is a polynomial in the
forcing parameter $A$ for a fixed coefficient of a *formal initial-value*
solution.  Kaneko--Ochiai's modular congruence is indexed instead by
the discrete rational-solution index.  The current proof does not assert
that their formulas cannot be manipulated to recover the same obstruction.

The new congruence classification for first-obstructed primes follows
from the proved $H_p(A)$ factorization and elementary integer lifts;
its density conclusion uses the prime number theorem in arithmetic
progressions.  This is not a separate resolution of Litt Problem 1.

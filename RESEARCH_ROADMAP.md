# Research roadmap for Litt Problem 1

## Current manuscript

### Zero-initial Painleve II family

The current preprint proves the complete first-obstruction polynomial for
\[
y''=2y^3+ty+A,\qquad y(0)=y'(0)=0.
\]
It determines the first bad coefficient for every $p$-integral parameter whenever the first obstruction is nonzero, and verifies the full Lam--Litt three-way criterion throughout this zero-initial family, with an explicit denominator-prime progression for every rational parameter outside $3\mathbb Z$.

## Other developed directions (not part of the current preprint)

These directions are kept separate because each has its own hypotheses and proof obligations.

1. **Cartier--Chebotarev criterion for closed rational foliations.** A first-order rational ODE admitting a closed rational one-form multiplier has an algebraic solution whenever the ordinary Taylor series has finite denominator support. The separable family $y'=A(x)B(y)$ is included. The proof has been checked internally; a specialist literature-priority review is still required before a separate manuscript is released.
2. **Riccati $p$-curvature obstructions.** For $y'=y^2+x^m$, explicit characteristic-$p$ spectral calculations rule out integral formal reductions for all sufficiently large primes when $m$ is odd, and for primes $p\equiv3\pmod4$ when $m$ is even and $p\nmid m+2$. This is a special-family result, not a universal obstruction theorem.
3. **Cross-prime algebraization criterion.** A general conditional theorem is available. Suppose $f\in\mathbb Z[[t]]$ has positive complex radius of convergence and, for each prime $p$ in a set $S$ and each $k\ge1$, there is a $p$-primitive polynomial $P_{p,k}\in\mathbb Z_p[t,Y]$ such that
   \[ \deg_Y P_{p,k}\le d,\qquad \deg_t P_{p,k}\le a_p+k c_p,\qquad P_{p,k}(t,f(t))\in p^k\mathbb Z_p[[t]],
   \]
   with $a_p\ge0$, $c_p>0$, and $\sum_{p\in S}\log p/c_p=\infty$. Then $f$ is algebraic over $\mathbb Q(t)$ of degree at most $d$. The remaining challenge is deriving the required uniform degree and precision bounds from an arbitrary ordinary rational ODE.
4. **Cartier-defect reduction.** For a finitely generated differential subfield $K$ of $k((x))$ in characteristic $p$, stability under the zero Cartier section is equivalent to algebraicity over $k(x)$; the defect is measured by $[\ker D:K^p]=p^{\operatorname{trdeg}_k K-1}$. The missing step is a uniform mixed-characteristic argument forcing zero-section closure for the actual reductions of an integral characteristic-zero solution.

## The general obstruction

Finite denominator support gives a compatible formal leaf modulo almost every prime. The difficult step is not producing those reductions; it is proving that the actual branch is algebraic in characteristic $p$ with complexity bounded independently of $p$, or otherwise extracting a characteristic-zero algebraic relation. In the current strategy, one must still control the degree of the actual Frobenius relation, its precision slope, and the primes at which the relevant curvature branch is simple. Degenerate/repeated Frobenius branches are the main unresolved case.

No result in this repository currently proves Litt Problem 1 in its unrestricted form.

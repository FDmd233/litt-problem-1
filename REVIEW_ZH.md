# 独立审查记录（中文）

日期：2026-11-23
审查对象：`paper/main.tex` 与 `verification/verify_pii_obstruction.py`

## 结论摘要

当前论文的核心定理是零初值 Painlev\'e II 族的首个 $p$-进障碍多项式。对其证明链进行了逐段复核，并另行实现了有限范围的精确有理数/有限域核验。没有发现阻断核心定理的错误；但这不等于外部同行评审，也不等于已经完成全球文献优先权确认。

## 数学审查

1. **Lam--Litt 截断条件。** 已核对附加推论：对 $A\in3\mathbb Z$，有限坏素数之外可取 $\omega(p)=p^2$；对 $A\notin3\mathbb Z$，显式同余类中无限多个素数的首坏下标不超过 $p+1$，因此任何满足 $\omega(p)/p\to\infty$ 的截断最终都会越过首坏项。这确实验证了该三条件等价在本特殊族中的成立。
2. **普通点与唯一性。** 方程在指定初始 jet 处正则，形式解由递推唯一确定。
3. **支撑与参数次数。** 递推确实保持 $t^{3k+2}$ 支撑；$b_k(A)$ 为奇多项式，且次数不超过 $2\lfloor k/2\rfloor+1$。
4. **首个可能分母位置。** $k<m=\lfloor p/3\rfloor$ 时分母为 $p$-单位；$k=m$ 时恰含一个 $p$ 因子。$p\equiv1\pmod6$ 时更早的 $t^p$ 项在支撑之外。
5. **三步 B\"acklund 变换。** 变换 $T_\beta$ 的符号方向与参数增量核对一致。三个 Laurent 分母的首项分别为 $(2\alpha+1)t$、$4t^{-2}$、$-(2\alpha+5)t$。中间分子 $2\alpha+3$ 不需要是单位；第三步的极点抵消由 Laurent 展开给出。
6. **根数论证。** 对 $1\le j\le r$，$p>6j-1$，故 $y_{\pm3j}$ 在 $\Z_p[[t]]$ 中。它们给出 $2r+1$ 个互异根；结合次数上界与非零线性项，得到完整乘积形式。
7. **常数 $C_p$。** 线性系数计算与 Wilson 定理给出两个剩余类的常数；所有被约去的阶乘指标均小于 $p$。
8. **$A=1$。** $1$ 不属于根集；$p=2$ 与 $p=3$ 单独处理正确。
9. **有理参数分类。** 同余类构造中的整数提升、半整数边界、$\gcd(a,3)=3$ 的单位提升及负参数均需保留。Dirichlet 定理给出无限多个合格素数，因此非 $3\Z$ 参数不可能只有有限个分母素数。

## 独立计算核验

另行运行标准库精确算术脚本，结果：

- 从原始递推直接计算 $H_p(A)$，与闭式乘积逐系数比较；对所有 $5\le p\le300$ 的素数通过。
- 对 $A=1$ 直接以有理数递推到 $t^{800}$；对所有 $5\le p\le97$ 的素数，首个坏下标与定理一致，且该系数的 $p$-赋值为 $-1$。
- 检查 $A=1$ 的支撑限制及 $3$-整性至 $t^{800}$。

这些有限检查只用于发现递推、符号或实现错误，不构成全称证明。

## 文献与原创性边界

- Murata (1985) 已分类 PII 的有理解；Freitag--Nagloo (2025) 明确回顾了 PII 的代数解分类：代数解只在整数参数出现，且唯一代数解为有理解。
- Yablonskii--Vorob'ev 多项式的 \(t^3\) 支撑结构说明，经典有理解在 \(t=0\) 具有零 1-jet 恰好发生在参数属于 \(3\mathbb Z\) 的情形。因此，单独的“有限分母当且仅当参数属于 \(3\mathbb Z\)”不应作为本稿的原创性主张。
- Kaneko--Ochiai (2003) 已给出 Yablonskii--Vorob'ev 多项式系数公式，并研究其模素数约化；Roffelsen (2010) 已研究相关多项式的系数整除性质及根之间的关系。
- 故不能把 Yablonskii--Vorob'ev 多项式、Painlevé II 的经典有理解或 Bäcklund 变换本身宣称为原创工具。
- 本稿真正需要完成优先权确认的候选新内容是：对任意参数 \(A\) 的零初值形式族，给出所有 \(p>3\) 的完整首障碍多项式及其精确归一化常数；并为每个 \(A\in\mathbb Q\setminus3\mathbb Z\) 构造显式素数同余类，使首次坏系数和赋值都可确定。
- 目前没有发现完全相同的公开公式，但文献优先权检索仍不可能仅凭有限网页搜索作最终保证。

## 发布前仍需完成

- 至少一位熟悉 Painlev\'e 方程与算术微分方程的外部数学研究者进行独立审阅。
- 再核对不同归一化的 Yablonskii--Vorob'ev 多项式与本稿参数/变量缩放，避免遗漏等价表达。
- 最终发布前重新编译 PDF、运行全部脚本、更新 SHA-256 清单，并确保论文、源文件和元数据一致。


## 0.1.2 发布前修订

- 删除重复出现的 Lam--Litt 推论及重复标签 `cor:LL`；当前源码中该标签仅定义一次。
- 将有限个坏素数处的截断函数明确设为 `\omega(p)=0`。由于常数项为零，这一选择满足该处的整性要求；有限个取值不影响 `\omega(p)/p\to\infty`。
- 从修订后的 LaTeX 重新编译 PDF，并重新运行精确算术脚本与 SHA-256 清单检查。
- 本轮是文稿与发布工程修订，不改变核心定理及其证明路线；仍未完成外部专家同行审查和全球优先权确认。


## 外部文献追加核对：Kaneko--Ochiai 模素数定理

本轮重新查看了 Kaneko--Ochiai 原文。其 Theorem 3 给出 Yablonskii--Vorob'ev 多项式在指标 `mp+n` 下的模 `p` 约化公式；论文还给出最低次系数公式及固定系数相对于最低次系数的参数多项式规律。该结果与本文利用有理解作为 `H_p(A)` 的根直接相关，不能只用“研究对象不同”一语带过。

当前可作出的稳妥结论是：Kaneko--Ochiai 的定理研究经典 Yablonskii--Vorob'ev 多项式的指标模 `p` 约化；本文的候选新定理是任意形式参数 `A` 的零初值系数族在首次坏下标处的完整障碍多项式。二者可能存在可转换关系。尚未完成从该文 Theorem 1--3 到本文 `H_p(A)` 的逐项归一化推导，因此不作“文献已排除等价结果”的断言。投稿前应完成这一项专门比较，最好请 Painlevé II 专家确认。

参考：M. Kaneko and H. Ochiai, *On coefficients of Yablonskii--Vorob'ev polynomials*, J. Math. Soc. Japan 55 (2003), 985--993, DOI 10.2969/jmsj/1191418760；原文公开 PDF：<https://www2.math.kyushu-u.ac.jp/~mkaneko/papers/29Yablonskii-Vorob'ev.pdf>。


## v0.1.2 数学修订

- 将主定理的非零性论证明确绑定到后文的非零一次项；根数结论不再预先假设障碍多项式非零。
- 新增整数参数推论：若 3 不整除 a，则每个 p>max(3,2|a|) 均在首次允许位置出现分母，且赋值为 -1。
- 给出各素数上首次障碍消失参数剩余类的准确计数 2 floor(p/6)+1。
- 明确 Kaneko--Ochiai Theorem 3 与 H_p 的变量分别为离散 YV 多项式指标与连续形式参数，未断言不存在通过已有公式的推导。
- 已存在的内部审计不能替代外部同行审查；后续数学创新性声明仍需审慎。


## v0.2.0: new congruence theorem and mathematical audit

For $A=a/b$ in lowest terms with $b\ge3$, the first-obstruction root
condition at a prime $p=6r+c$, $c\in\{1,5\}$, is equivalent to the
existence of integers $j,\ell$ satisfying

$$3bj=a+\ell p,\qquad |a+\ell p|\le b(p-c)/2.$$

For $p>2|a|+5b$, all possible lifts satisfy $|\ell|<b/2$:
large $|\ell|$ are excluded by the size inequality, and the boundary
$|\ell|=b/2$ is excluded for $b\ge4$ by coprimality.  The root condition
therefore depends only on $p\bmod 3b$.  Counting the allowed lift
integers gives separate formulas for $3\nmid a$ and $3\mid a$.
The exceptional case $b=2$ has a boundary lift; the correct root
condition is $p\equiv|a|\pmod6$ for primes $p>\max\{3,2|a|\}$.

The new independent checker compares this class criterion with the
original root condition across 106,415 parameter-prime instances,
and verifies the class-cardinality formula for 1,198 reduced
parameters with denominator at least 3.  All tests passed.  These
checks corroborate the integer inequality and congruence branches;
they are not substitutes for the stated proof.

Reconciliation: manuscript, README, BibTeX, CFF, JSON metadata, release
notes, CI workflow, and checksums must all use v0.2.0 before upload.

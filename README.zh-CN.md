# Painleve II 零初值族的首分母障碍

**研究预印本 v0.2.0 | 2026 年 11 月 23 日 | Zhijie He**

研究方程

$$y''=2y^3+ty+A,\qquad y(0)=y'(0)=0.$$

对所有 $p>3$，首个可能失去 $p$-整性的 Taylor 系数具有完全分解的障碍多项式：

$$H_p(A)=C_p A\prod_{j=1}^{\lfloor p/6\rfloor}(A^2-9j^2).$$

因此可以精确确定首次分母的位置、赋值和使障碍消失的参数剩余类。特别是 $A=1$ 时，除 $3$ 之外每个素数都会出现在分母中，第一次出现恰在 $p$ 或 $p+1$ 阶。

**v0.2.0 新结果：** 对任意有理数 $A=a/b$，首次障碍是否消失在充分大的素数上由有限个同余类完全确定。当 $b\ge3$，模数为 $3b$；当 $b=2$，模数为 $6$。由此得到首次坏素数的精确自然密度。例如 $A=1/3$ 为 $2/3$，$A=1/2$ 为 $1/2$，$A=3/2$ 为 $1$。

零初值族中，有限分母素数集恰好对应 $A\in3\mathbb Z$，这与经典 Painleve II 有理解分类相符。

## 论文及复现

[PDF](paper/main.pdf) | [LaTeX](paper/main.tex) | [首障碍精确核验](verification/verify_pii_obstruction.py) | [同余分类精确核验](verification/verify_prime_sieve.py)

[文献对照](PRIOR_ART.md) | [中文审查](REVIEW_ZH.md) | [后续路线](RESEARCH_ROADMAP.md) | [AI 使用声明](AI_ASSISTANCE.md)

执行 `make verify` 检查精确算术与文件完整性，执行 `make pdf` 重新编译论文。程序用于复核计算，所有素数的结论由论文中的证明给出。

这是一项与 Litt #1 相关的**具体非线性微分方程族的完整结论**；原题允许任意普通有理 ODE，尚未因此解决。



## 群在集合上的作用, 轨道-稳定子定理


**定义**

- 
	设 $G$ 是一个群, $\Omega$ 是一个非空集合. 如果映射
	$$
	\begin{array}{rccl}
		\sigma:&G\times \Omega & \to & \Omega \\
		&(a,x) & \mapsto & a \circ x
	\end{array}
	$$
	满足:
	$$
	\begin{array}{rl}
		(ab)\circ x=a\circ(b\circ x), & \forall\ a,b \in G,\ \forall\  x\in \Omega, \\
		e\circ x= x, & \forall\ x \in \Omega.
	\end{array}
	$$
	那么称群 $G$ 在集合 $\Omega$ 上有一个作用.


**注**

- 可理解为 $a \circ x$ 运算, 就是 $G$ 中元素 $a$ 在 $\Omega$ 上的作用.

	更直接的, 我们任给 $a\in G$ 就可以得到一个 $\Omega$ 到自身的映射 $\psi(a)$:
	$$
	\begin{array}{rccl}
		\psi(a):& \Omega & \to & \Omega \\
		& x & \mapsto & a\circ x.
	\end{array}
	$$

	容易验证 $\psi(a)$ 是 $\Omega$ 上的可逆变换, 其逆映射就是 $\psi(a^{-1})$, 从而 $\psi(a)$ 是 $\Omega$ 到自身的双射, 即 $\psi(a) \in S_\Omega$.

	由此, 我们令
	$$
	\begin{array}{rccl}
		\psi: & G &\to&S_\Omega \\
		& a & \mapsto & \psi(a),
	\end{array}
	$$
	则 $\psi$ 是 $G$ 到 $S_\Omega$ 的一个映射. 可以类似的验证 $\psi$ 保持运算, 即 $\psi$ 是 $G$ 到 $S_\Omega$ 的同态.


**命题**

- 设群 $G$ 在集合 $\Omega$ 上有一个作用, 任给 $a\in G$, 令
	$$\psi(a)x:=a\circ x,\quad \forall\ x\in \Omega,$$
	则 $\psi:a\mapsto\psi(a)$ 是 $G$ 到 $S_\Omega$ 的一个群同态.



**定义**

- 
	我们称同态 $\psi$ 的核 $\text{Ker}\psi$ 为这个**作用的核**. 可以得到, $a\in G$ 是这个作用的核 $\Leftrightarrow\ a\circ x=x,\quad \forall x \in G.$



**定义**

- 
	当 $\text{Ker}\psi=\{e\}$ 时, 称这个作用是**忠实的**, 此时 $\psi$ 是一个单同态.



**命题**

- 设群 $G$ 到非空集合 $\Omega$ 上的全变换群 $S_\Omega$ 有一个同态 $\psi$, 令 $$a\circ x:=\psi(a)x,\quad \forall\ a\in G,\forall\ x \in \Omega,$$ 则 $G$ 在 $\Omega$ 上有一个作用.



1. **群 $G$ 在集合 $G$ 上的左平移**

	设 $G$ 是一个群, 令
	$$
	\begin{array}{rcl}
		G\times G & \to & G \\
		(a,x) & \mapsto & ax.
	\end{array}
	$$
	容易验证这是 $G$ 在集合 $G$ 上的作用, 称该作用为 $G$ 在集合 $G$ 上的左平移.

	并且左平移的核 $\Leftrightarrow\ ax=x\Leftrightarrow a=e$, 即左平移是忠实的作用. 所以 $G\cong \text{Im}\psi$, 即 $G$ 与 $G$ 上的一个变换群同构.

	
    **定理 Cayley**

    - 任意一个群都同构于某一集合上的变换群.


2. **群 $G$ 在左商集 $(G/H)_l$ 上的左平移**

	设 $H$ 是 $G$ 的子群, 令
	$$
	\begin{array}{rcl}
		G\times(G/H)_l & \to & (G/H)_l \\
		(a,xH) & \mapsto & axH.
	\end{array}
	$$

	容易验证这是 $G$ 在 $(G/H)_l$ 上的作用, 称之为 $G$ 在 $(G/H)_l$ 上的左平移.

	注: 当题目中有子群时, 优先考虑在其左商集上的左平移.

3. **群 $G$ 在集合 $G$ 上的共轭作用**

	令 $$
	\begin{array}{rcl}
		G\times G & \to & G \\
		(a,x) & \mapsto & axa^{-1}.
	\end{array}
	$$
	容易验证, 这是 $G$ 在 $G$ 上的作用, 称之为共轭作用.




**定义**

- 
	设 $Z(G):=\{b\in G|bx=xb,\forall x\in G\}$, 易得 $Z(G)$ 是共轭作用的核. 我们称 $Z(G)$ 为群 $G$ 的**中心**, 它是由与 $G$ 中每个元素都可交换的元素组成的集合.


群 $G$ 在集合 $G$ 上的共轭作用引出了一个 $G$ 到$S_G$ 的同态 $\sigma$, 把 $a$ 在 $\sigma$ 下的像记作 $\sigma_a$, 于是
$$
	\sigma_a(x)=a\circ x=axa^{-1},\quad \forall\ x\in G.
$$

容易验证 $\sigma_a$ 是 $G$ 到自身的同构映射.


**定义**

- 
	群 $G$ 到自身的一个同构映射称为 $G$ 的一个**自同构**. 由 () 式定义的 $\sigma_a$ 称为 $G$ 的一个**内自同构**.

	此外, 群 $G$ 的所有自同构组成的集合对于映射的乘法构成一个群, 称它为**自同构群**, 记作 $\text{Aut}(G)$.

	群 $G$ 的所有内自同构组成的集合是上述的 $\text{Im}\sigma$, 它是 $S_G$ 的一个子群, 称它是 $G$ 的**内自同构群**, 记作 $\text{Inn}(G)$.


由于 $G$ 的每个内自同构 $\sigma_a$ 是 $G$ 的一个自同构, 因此 $\text{Inn}(G)<\text{Aut}(G)$.

更进一步的, 可以验证 $\text{Inn}(G)\lhd\text{Aut}(G)$.


**定理**

- 对于群 $G$ 有 $$G/Z(G)\cong \text{Inn}(G).$$



**证明**

- 由于 $\text{Ker}\sigma=Z(G),\text{Im}\sigma=\text{Inn}(G)$, 根据\text{群同态基本定理} $G/Z(G)\cong \text{Inn}(G)$.



**引理**

- 集合 $\Omega$ 上的二元关系:
	$$
		y\sim x:\Leftrightarrow\exists\ a\in G,\ s.t.\ y=a\circ x.
	$$
	是等价关系.



**定义**

- 
	我们称 $$G(x):=\{a\circ x|a\in G\},$$ 为 $x$ 的 **$G$-轨道**. 且 $G(x)$ 是等价关系()中的一个等价类. 于是 $\Omega$ 的所有 $G$-轨道组成的集合是 $\Omega$ 的一个划分. $\Omega$ 的任意两条轨道要么相等, 要么不交. 且所有轨道的并是 $\Omega$.

	若 $\Omega$ 的子集 $I=\{x_i\}$ 使得
	$$
		\Omega=\bigcup\limits_{i\in I}G(x_i),
	$$
	且当 $i\neq j$ 时有 $G(x_i)\cap G(x_j)=\varnothing$. 那么就称 $I$ 为 $\Omega$ 的 $G$-轨道的**完全代表系**.



**定义**

- 
	我们称 $$G_x:=\{g\in G|g\circ x=x\},$$ 为 $x$ 的**稳定子群**.

	容易验证 $G_x$ 是 $G$ 的子群. 且 $G_x$ 中的每个元素作用 $x$ 保持 $x$ 不变.



**引理**

- 
	任给 $a,b\in G$, $aG_x=bG_x\Leftrightarrow b^{-1}a\in G_x\Leftrightarrow a\circ x=b\circ x$.


因此 $G_x$ 的某个陪集中的元素对 $x$ 的作用是相同的. 从而考虑
$$
\begin{array}{rcl}
	\varphi:(G/G_x)_l & \to & G(x)\\
	aG_x & \mapsto & a\circ x,
\end{array}
$$
由引理  可知 $\varphi$ 是 $(G/G_x)_l$ 到 $G(x)$ 的一个单射, 从其定义可知这也是个满射, 由此 $\varphi$ 是双射. 于是我们有 $|G(x)|=|(G/G_x)_l|$.


**定理 轨道-稳定子定理**

- 
	设群 $G$ 在集合 $\Omega$ 上有一个作用, 则对于任给 $x\in\Omega$, 有
	$$
		|G(x)|=|(G/G_x)_l|=[G:G_x]
	$$



**推论**

- 如果有限群 $G$ 在 $\Omega$ 上有一个作用, 那么对于 $x\in \Omega$ 有 $$|G|=|G_x||G(x)|.$$


下面考虑上述讨论在共轭作用中的应用.


**定义**

- 
	我们称共轭作用中的 $G$-轨道 $G(x)=\{axa^{-1}|a\in G\}$ 为 $x$ 的**共轭类**.


当且仅当 $x\in Z(G)$ 时, 有 $|G(x)|=1$.


**定义**

- 
	当 $G$ 为有限群时, 我们称
	$$
		|G|=|Z(G)|+\sum\limits_{j=1}^r|G(x_j)|
	$$
	为有限群 $G$ 的**类方程**. 其中 $Z(G)$ 为 $G$ 的中心, $\{x_1,x_2\ldots,x_r\}$ 为 $G$ 的非中心元素的共轭类的\text{完全代表系}.



**定义**

- 
	在共轭作用下, 我们称 $C_G(x):=G_x=\{g\in G|g\circ x=x\}=\{g\in G|gx=xg\}$ 为 $x$ 在 $G$ 里的**中心化子**.



**推论**

- 运用轨道-稳定子定理可知, $|G(x)|=[G:C_G(x)]$.


以上就是在共轭作用中的特殊例子.


**定义**

- 
	如果群 $G$ 在 $\Omega$ 上的作用只有一条轨道, 即 $\forall\ x,y\in\Omega,\ \exists\ g\in G,\ s.t. y=g\circ x$, 那么称 $G$ 在 $\Omega$ 上的这个作用是**传递的**. 并称 $\Omega$ 是群 $G$ 上的一个**齐性空间**.



**命题**

- 
	设群 $G$ 在集合 $\Omega$ 上有一个作用, 则对任一给定 $x\in \Omega$, 对于轨道 $G(x)$ 有 $\forall\ y\in G(x)$, $G_x$ 和 $G_y$ 彼此共轭, 即存在 $a\in G$, 使得 $G_y=aG_x a^{-1}$. 从而 $|G_x|=|G_y|,[G:G_x]=[G:G_y]$.



**定义**

- 
	对于给定的 $g\in G$, 我们称 $F(g):=\{x\in\Omega|g\circ x=x\}$ 为 $g$ 的**不动点集**. 即 $g$ 存在于哪些 $x$ 的稳定子群中.



**定理 \text{Burnside} 引理**

- 
	设有限群 $G$ 在有限集合 $\Omega$ 上有一个作用, 则 $\Omega$ 的 $G$-轨道条数 $r$ 为 $$r=\frac{1}{|G|}\sum\limits_{g\in G}|F(g)|.$$



**证明**

- 考虑集合 $$S=\{(g,x)|g\circ x=x\}.$$

	一方面, $|S|=\sum\limits_{x\in \Omega}|G_x|=r|G|$.

	由命题  同一条轨道上的元素的稳定子群阶数相同, 从而同一条轨道上元素的稳定子群阶数和为 $|G|$.

	另一方面, $|S|=\sum\limits_{g\in G}|F(g)|$.



**定义**

- 
	设群 $G$ 在集合 $\Omega$ 上有一个作用, 对于 $x\in\Omega$, 若 $x$ 的 $G$-轨道只含一个元素(即 $x$ 自身), 则称 $x$ 是群 $G$ 的一个**不动点**. 群 $G$ 的所有不动点组成的集合称为群 $G$ 的**不动点集**, 记作 $\Omega_0$.



**定义**

- 
	若有限群 $G$ 的阶是素数 $p$ 的方幂, 即 $|G|=p^m,\ (m\geqslant 1)$, 则称 $G$ 是 $p$-群.



**命题**

- 设 $p$-群 $G$ 在集合 $\Omega$ 上有一个作用, 则
	$$|\Omega_0|\equiv|\Omega|(\bmod p).$$



**推论**

- $p$-群 $G$ 必有非平凡中心, 即 $Z(G)\neq \{e\}$.



**推论**

- 设 $p$ 是素数, 则 $p^2$ 阶群要么是循环群, 要么同构于 $(\seta Z p,+)\oplus(\seta Z p,+)$, 从而 $p^2$ 阶群都是 $\text{Abel}$ 群.


\begin{practice}
	\problem 设 $G$ 是一个群. 证明: 如果 $G/Z(G)$ 是循环群, 那么 $G$ 是 \text{Abel} 群.

	\problem(书本习题 1.8/28) 设 $G$ 为一个有限群, $p$ 为 $|G|$ 的最小素因子. 证明: 指数为 $p$ 的子群必为正规子群.


\end{practice}
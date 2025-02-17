# 环的理想, 域的构造


## 环同态, 理想, 商环


**定义**

- 
	若非空集合 $R_1\subseteq R$, $R$ 是一个环, 如果 $R_1$ 对于 $R$ 的加法和乘法也构成环, 则称 $R_1$ 是 $R$ 的**子环**.



**命题**

- 环 $R$ 的子集 $R_1$ 是的子环, 当且仅当 $$a,b\in R_1\Rightarrow a-b\in R_1\wedge ab\in R_1.$$



**定义**

- 
	如果环 $R$ 到环 $\widetilde{R}$ 有一个映射 $\sigma$, 满足:
	$$
	\begin{array}{l}
		\sigma(a+b)=\sigma(a)+\sigma(b), \\
		\sigma(ab)=\sigma(a)+\sigma(b), \\
		\sigma(1)=\widetilde{1}.
	\end{array}
	$$
	那么称 $\sigma$ 是**环同态**.


注: 只有存在单位元才需验证上述最后一条条件.


**性质**

- 设 $\sigma$ 是 $R$ 到 $\widetilde{R}$ 的环同态, 则
	$$\sigma(0)=\widetilde{0},\quad\sigma(-a)=-\sigma(a).$$



**定义**

- 称 $\text{Ker} \sigma$ 为 $R$ 到 $\widetilde{R}$ 的**环同态核**.



**定义**

- 
	如果环 $R$ 的一个非空子集 $I$ 对 $R$ 的减法封闭, 并且具有"左, 右吸收性", 即 $$a\in I,\ r\in R\ \Rightarrow ra \in I\wedge ar\in I,$$ 那么称 $I$ 是 $R$ 的一个**理想**或**双边理想**.



**推论**

- 理想是加法子群.



**定义**

- 
	称 $R$ 和 $\{0\}$ 是环 $R$ 的**平凡的理想**.

	如果 $R$ 只有平凡的理想, 那么称 $R$ 是**单环**.



**推论**

- 设环 $R$ 有单位元, 则 $R$ 的每个非平凡理想均不含有单位元.



**推论**

- 域 $F$ 没有非平凡理想.



**证明**

- 由于存在逆元, 非零理想中必存在幺元, 进而非零理想就是 $F$.



**推论**

- 
	设 $R$ 是交换幺环, 则 $$R\ \text{是域}\Leftrightarrow R\ \text{没有非平凡理想}.$$



**证明**

- 考虑 $Ra$ 是 $R$ 的理想, $Ra=R$ 可得存在 $ba=e$, 由此 $a$ 有逆元.



**定义**

- 
	如果环 $R$ 的子集 $J$ 对减法封闭, 并且具有"左吸收性", 即 $$b\in J,r\in R\Rightarrow rb\in J.$$ 则称 $J$ 是 $R$ 的**左理想**.



**定义**

- 
	设 $I$ 是环 $R$ 的一个理想, 令 $$R/I:=\{r+I|r\in R\}.$$
	并在 $R/I$ 中规定 $$(r_1+I)(r_2+I):=r_1r_2+I.$$
	则 $R/I$ 成为一个环, 称它为环 $R$ 对于理想 $I$ 的**商环**, 它的元素 $r+I$ 称为模 $I$ 的**同余类**.





**定义**

- 
	设 $I$ 是环 $R$ 的一个理想, 令 $$
	\begin{array}{rccl}
		\pi: & R & \to & R/I \\
		& r & \mapsto & r+I.
	\end{array}
	$$
	则 $\pi$ 是环 $R$ 到 $R/I$ 的一个环同态, 且是满同态, $\text{Ker}\pi=I$. 称 $\pi$ 为 $R$ 到 $R/I$ 的**自然环同态**.



**定理 环同态基本定理**

- 
	设 $\sigma$ 是环 $R$ 到 $\widetilde{R}$ 的一个环同态, 则 $\text{Ker}\sigma$ 是 $R$ 的一个理想, 且 $\text{Im}\sigma\cong R/\text{Ker}\sigma$.




**定理 第一环同构定理**

- 
	设 $I$ 是环 $R$ 的一个理想, $H$ 是 $R$ 的一个子环, 则
	
(1) $H+I$ 是 $R$ 的一个子环.
(2) $H\cap I$ 是 $H$ 的一个理想, 且 $H/H\cap I\cong (H+I)/I$.
	



**命题**

- 设 $I$ 是环 $R$ 的一个理想, 则商环 $R/I$ 的所有理想组成的集合为 $$\{K/I|K\ \text{是}\ R\ \text{的包含}\ I\ \text{的理想}\}.$$



**定理 第二环同构定理**

- 
	设 $I,J$ 是环 $R$ 的理想, 且 $I\subseteq J$, 则 $J/I$ 是 $R/I$ 的一个理想, 且有环同构: $$(R/I)/(J/I)\cong R/J.$$


## 理想的运算, 环的直和


**命题**

- 设 $R$ 是含有单位元的交换环, 任给 $a\in R$, 令 $$\{ar|r\in R\}=:aR=Ra:=\{ra|r\in R\}$$ 则 $Ra, aR$ 是 $R$ 的理想.



**命题**

- 若 $\{I_j|j\in J\}$ 是环 $R$ 的一族理想, 则 $\bigcap\limits_{j\in J} I_j$ 也是 $R$ 的理想.



**定义**

- 
	设 $S$ 是环 $R$ 的非空子集, 把 $R$ 的所有包含 $S$ 的理想的交集称为**由 $S$ 生成的理想**, 记作 $(S)$. 如果 $S$ 是有限集, 那么称 $(S)$ 是**有限生成的**. 若 $S=\{a_1,a_2,\ldots,a_n\}$, 则把 $(S)$ 记作 $(a_1,a_2,\ldots,a_n)$.



**定义**

- 
	环 $R$ 中由一个元素生成的理想称为**主理想**, 记作 $(a)$.



**性质**

- 若 $R$ 是有单位元的交换环, 则 $Ra=(a)$.



**命题**

- 设 $R$ 是一个环 (不一定有单位元, 也不一定是交换环), 则元素 $a$ 生成的理想 $(a)$ 为 $$(a)=\left\{r_1a+ar_2+ma+\sum\limits_{i=1}^n x_iay_i|r_1,r_2,x_i,y_i\in R,m\in\mathbb{Z},n\in\mathbb{N}^*\right\}.$$



**命题**

- 若 $R$ 是有单位元的交换环, $a_1,a_2,\ldots,a_n\in R$, 则 $$(a_1,a_2,\ldots,a_n)=\{\sum\limits_{i=1}^n r_ia_i|r_i\in R,i=1,2,\ldots,n\}.$$



**定义**

- 
	设 $A,B$ 是环 $R$ 的两个非空子集, 定义
	$$
	\begin{array}{c}
		A+B:=\{a+b|a\in A,b\in B\} \\
		AB:=\left\{\sum\limits_{i=1}^n a_ib_i\bigg|a_i\in A,b_i\in B,i=1,2,\ldots,n,n\in\mathbb{N}^*\right\}
	\end{array}
	$$



**定义**

- 
	若 $I,J$ 是环 $R$ 的两个理想, 则 $I+J,IJ$ 都是 $R$ 的理想, 分别称他们为理想的**和、积**, 并且有 $$IJ\subseteq I\cap J\subseteq I+J.$$



**性质**

- 设 $I,J,K$ 都是环 $R$ 的理想, 则
	$$
	\begin{array}{c}
		I+J=J+I, \\
		(I+J)+K=I+(J+K), \\
		(IJ)K=I(JK), \\
		I(J+K)=IJ+IK, \\
		(J+K)I=JI+KI. \\
	\end{array}
	$$



**例**

- 在整环 $\mathbb{Z}$ 中,
	\begin{equation}
		(n)(m)=\left\{\sum\limits_{i=1}^t(k_in)(l_im)\bigg|k_il_i\in\mathbb{Z},1\leqslant i\leqslant t,t\in\mathbb{N}^*\right\}=(nm),
	\end{equation}
	\begin{equation}
		(n)\cap(m)=([n,m]),
	\end{equation}
	\begin{equation}
		(n)+(m)=\{kn+lm|k,l\in\mathbb{Z}\}=((n,m)).
	\end{equation}




**定义**

- 
	设 $R$ 是有单位元的环, $I,J$ 是 $R$ 的理想. 如果 $I+J=R$, 那么称 $I$ 与 $J$ **互素**.



**例**

- 在整数环 $\mathbb{Z}$ 中, $$(n,m)=1 \Leftrightarrow (n)+(m)=(1)=\mathbb{Z}.$$



**命题**

- 设 $R$ 是有单位元的环, $I,J,K$ 都是 $R$ 的理想. 如果 $I$ 和 $J$ 都与 $K$ 互素, 那么 $IJ$ 也与 $K$ 互素.



**证明**

- 考虑证明存在幺元.



**例**

- 在整数环 $\mathbb{Z}$ 中, $(n)$ 与 $(m)$ 互素当且仅当 $(n,m)=1$.



**命题**

- 设 $R$ 是有单位元的交换环, $I,J$ 是 $R$ 的理想, 则 $$I+J=R\Rightarrow IJ=I\cap J.$$



**例**

- 在整数环 $\mathbb{Z}$ 中, $$(n)+(m)=\mathbb{Z}\Rightarrow ([n,m])=(nm)\Rightarrow (n)\cap (m)=(n)(m).$$



**定义**

- 
	设 $R_1,R_2,\ldots,R_s$ 都是环, 在笛卡尔积 $R_1\text{i}mes R_2\text{i}mes \cdots\text{i}mes R_s$ 中规定
	\begin{equation}
		(a_1,a_2\ldots,a_s)+(b_1,b_2,\ldots,b_s):=(a_1+b_1,a_2+b_2,\ldots,a_s+b_s),
	\end{equation}
	\begin{equation}
		(a_1,a_2,\ldots,a_s)\text{i}mes(b_1,b_2,\ldots,b_s):=(a_1b_1,a_2b_2,\ldots,a_sb_s).
	\end{equation}
	容易验证, 上述加法和乘法构成一个环, 称它为环 $R_1,R_2,\ldots,R_s$ 的**直和**, 记作 $R_1\oplus R_2\oplus\cdot\oplus R_s$, 零元为 $(0_1,0_2,\ldots,0_s)$.

	如果每个环有单位元则 $(1_1,1_2,\ldots,1_s)$ 是直和的单位元.

	如果每个环都是交换环, 那么直和是交换环.



**定义**

- 

	设 $I$ 是环 $R$ 的一个理想, 对于 $a,b\in R$, 如果 $$a-b\in I,$$ 那么称 $a$ 与 $b$ **模 $I$ 同余**, 记作 $a\equiv b(\bmod\ I)$.

	容易验证, 模 $I$ 同余是等价关系. 任给 $r\in R$, $r$ 的等价类 $$
	\begin{array}{rl}
		\overline{r} &=\{x\in R|x\equiv r(\bmod\ I)\} \\
			&=\{x\in R|x-r\in I\} = \{x\in R|x-r=b,b\in I\} \\
			&=\{r+b|b\in I\}=r+I.
	\end{array}
	$$
	我们称 $r+I$ 为**模 $I$ 同余类**.



**性质**

- 若 $a\equiv b(\bmod\ I),c\equiv d(\bmod\ I)$, 则 $$
	\begin{array}{c}
		a+c\equiv b+d(\bmod\ I),\\
		ac\equiv bd(\bmod\ I),\\
		ca\equiv db(\bmod\ I)
	\end{array}
	$$



**定理**

- 设 $R$ 是有单位元的环, 若它的理想 $I_1,I_2,\ldots,I_s$ 两两互素, 则有环同构: \begin{equation}
		R/(I_1\cap I_2\cap\cdots\cap I_s)\cong R/I_1\oplus R/I_2\oplus\cdots\oplus R/I_s.
	\end{equation}



**定理 中国剩余定理**

- 
	设 $m_1,m_2,\ldots,m_s$ 是两两互素的大于 $1$ 的整数, 任给整数 $b_1,b_2,\ldots,b_s$, 则一次同余方程
	\begin{equation}
		\left\{
		\begin{array}{c}
			x\equiv b_1\ (\bmod\ m_1), \\
			x\equiv b_2\ (\bmod\ m_2), \\
			\cdots\cdots \\
			x\equiv b_s\ (\bmod\ m_s),
		\end{array}
		\right.
	\end{equation}
	在 $\mathbb{Z}$ 中有解, 它的一个解是 $$a=\sum\limits_{i=1}^s b_iv_i\prod\limits_{j\neq i}m_j,$$
	其中 $v_i$ 满足 $u_im_i+v_i\prod\limits_{j\neq i}m_j=1,i=1,2,\ldots,s$. 它的全部解为 $$a+km_1m_2\cdots m_s,\quad k\in\mathbb{Z}.$$



**定义**

- 
	设 $I$ 是交换环 $R$ 的一个理想. 令 $$\rad I:=\{r\in R\ |\ r^n\in I,\exists\ n\in \mathbb{N}^*\},$$
	称 $\rad I$ 是理想 $I$ 的**根**, 且 $\rad I$ 是 $R$ 的一个理想.



**定义**

- 
	若环 $R$ 中元素 $a$, 满足 $\exists\ n\in \mathbb{N}^*,\ s.t.\ a^n=0$, 那么称 $a$ 是**幂零元**.
	并且如果 $R$ 有单位元且 $a$ 是幂零元,  则 $1-a$ 可逆.



**定义**

- 
	在交换环 $R$ 中, 所有幂零元组成的集合是 $R$ 的一个理想, 且它是零理想 $(0)$ 的根, 称为 $R$ 的**幂零根**.



**定义**

- 
	设 $I_1,I_2,\ldots,I_s$ 都是环 $R$ 的理想, 并且
	\begin{equation*}
		\begin{array}{cc}
			R=I_1+I_2+\cdots I_s \\
			I_i\cap\left(\sum\limits_{j\neq i}I_j\right)=(0),\quad i=1,2,\ldots,s.
		\end{array}
	\end{equation*}
	则
	
(1) 环 $R$ 的每个元素 $x$ 都可以唯一表示成 $$x=x_1+x_2+\cdots+x_s,\quad x_i\in I_i,i=1,2,\ldots,s.$$
(2) 有环同构 $$R\cong I_1\oplus I_2\oplus\cdots\oplus I_s,$$ 并称 $R$ 是其理想 $I_1,I_2,\ldots,I_s$ 的**内直和**.
	


## 素理想和极大理想


**注**

- 本节中主要研究含幺环.



**定义**

- 
	若 $R$ 交换幺环, 且 $R$ 没有非零的零因子, 则称 $R$ 是**整环**.



**定义**

- 
	设 $R$ 是交换幺环, $P$ 是 $R$ 的理想, 且 $P\neq R$. 如果从 $ab\in P$ 可以推出 $a\in P$ 或者 $b\in P$, 那么称 $P$ 是一个**素理想**.



**例**

- 在整环 $\mathbb{Z}$ 中, 设 $p$ 是大于 $1$ 的整数, 则 $$p\ \text{是素数}\Leftrightarrow (p)\ \text{是素理想}$$




**例**

- 在域 $F$ 上的一元多项式环 $F[x]$ 中, 设 $p(x)$ 是次数大于 $0$ 的多项式, 则 $$p(x)\ \text{不可约}\Leftrightarrow (p(x))\ \text{是素理想}$$



**推论**

- 设 $R$ 是交换幺环, 则
	$$(0)\ \text{是}\ R\ \text{的一个素理想}\Leftrightarrow R\ \text{是整环}$$



**例**

- 
	 整数环 $\mathbb{Z}$ 的每一个理想都是由一个非负整数生成的主理想.



**证明**

- 取理想中最小的正元素为除数做带余除法.



**推论**

- $\mathbb{Z}$ 的全部素理想为 $(0),(p)$, 其中 $p$ 是素数.



**定理**

- 设 $R$ 是交换幺环, $P$ 是 $R$ 的一个理想, 则 $$\text{商环}\ R/P\ \text{是整环}\Leftrightarrow P\ \text{是}\ R\ \text{的素理想}.$$



**定义**

- 
 	设 $R$ 是环, $M$ 是 $R$ 的理想, 且 $M\neq R$. 如果 $R$ 中包含 $M$ 的理想只有 $M$ 和 $R$, 那么称 $M$ 是 $R$ 的一个**极大理想**.



**定理**

- 设 $R$ 是交换幺环, $I$ 是 $R$ 的一个理想, 则 $$\text{商环}\ R/I\ \text{是域}\Leftrightarrow I\ \text{是}\ R\ \text{的极大理想}$$



**证明**

- 利用推论  和极大理想定义即可直接得到.



**例**

- 域 $F$ 上一元多项式环 $F[x]$ 的每一个理想都是主理想, 其中非 $(0)$ 的主理想可以由首项系数为 $1$ 的多项式生成.



**证明**

- 类比例  取次数最低(非 $0$ 次)的多项式做带余除法.



**例**

- 在整数环 $\mathbb{Z}$ 中, 设 $p$ 是大于 $1$ 的整数, 则 $$p\ \text{是素数}\Leftrightarrow (p)\ \text{是极大理想}$$



**例**

- 域 $F$ 上的一元多项式环 $F[x]$ 中, 设 $p(x)$ 是次数大于 $0$ 的多项式, 则 $$p(x)\ \text{不可约}\Leftrightarrow (p(x))\ \text{是}\ F[x]\ \text{的极大理想}.$$



**例**

- 域 $F$ 上的一元多项式环 $F[x]$ 中, $M$ 是 $F[x]$ 的一个理想, 则 $$F[x]/M\ \text{是域}\Leftrightarrow M=(p(x)),\quad\text{其中}\ p(x)\ \text{是不可约多项式}.$$



**定理**

- 在幺环 $R$ 中必存在极大理想.



**定义**

- 
	设 $R$ 是幺环, 令 $\mathbb{Z} e:=\{ne|n\in \mathbb{Z}\}$. 则有 $\mathbb{Z} e$ 是 $R$ 的子环, 且存在非负整数 $m$ 满足环同构 $\mathbb{Z}/(m)\cong \mathbb{Z} e$, 我们称 $m$ 是环 $R$ 的**特征**.



**注**

- 环的特征也定义为, 最小的正整数 $m$ 满足 $\forall\ r\in R,mr=0$. 如果不存在这样的正整数, 则称环的特征为 $0$.

	可以理解为环中单位元的加法阶.




**命题**

- 如果 $R$ 是整环, 那么 $R$ 的特征是 $0$ 或者一个素数.


## 有限域的构造, 构造扩域的途径

由上节, 我们已经知道若 $p(x)$ 是 $F[x]$ 上的不可约多项式, 那么 $F[x]/(p(x))$ 是一个域.

在具体研究这个域的性质前, 我们先补充几个概念.



**定理**

- 设域 $F$ 的单位元为 $e$, 则要么 $\forall\ n\in \mathbb{N}^*$ 有 $ne\neq 0$, 要么存在一个素数 $p$, 使得 $pe=0$ 且对于 $0<l<p,\ le\neq 0$.



**定义**

- 
	设域 $F$ 的单位元为 $e$.

	如果 $\forall\ n\in \mathbb{N}^*$ 有 $ne\neq 0$, 则称**域 $F$ 的特征**为 $0$.

	如果存在素数 $p$, 使得 $pe=0$ 且对于 $0<l<p,\ le\neq 0$, 则称**域 $F$ 的特征**为 $p$.



**例**

- 
	构造含 $4$ 个元素的域.

	\begin{solution}
	 考虑在 $\Z_2[x]$ 中取不可约多项式 $x^2+x+\overline{1}$, 则 $\Z_2[x]/(x^2+x+\overline{1})$ 是一个域, 任取 $f(x)$ 做带余除法, 可得余数就是不同等价类的代表元, 由此可知该域仅有四个元素. 当我们记 $u=x+(x^2+x+\overline{1})$, 则 $$\Z_2[x]/(x^2+x+\overline{1})=\{0,1,u,1+u\}.$$

	 又 $2(\overline{1}+(x^2+x+\overline{1}))=(\overline{1}+\overline{1})+(x^2+x+\overline{1})=\overline{0}+(x^2+x+1)$

	 该步中, $\overline{1}+\overline{1}=\overline{0}$ 因为在 $\Z_2$ 中.

	 由此, 该四元域的特征为 $2$. 我们有 $u^2+u+1=(x^2+x+\overline{1})+(x^2+x+\overline{1})=(x^2+x+\overline{1})=0.$

	 且满足 $u+(1+u)=1+2u=1+0=1$ (利用域的特征为 $2$), $u(1+u)=u+u^2=-1=1$. (利用 $u^2+u+1=0$)
	\end{solution}



**定理**

- 设 $F_q$ 是含 $q$ 个元素的有限域, 其中 $q=p^r$, $p$ 为素数, $r\geqslant 1$. 如果 $F_q[x]$ 的 $n$ 次不可约多项式为 $m(x) = a_0+a_1x + \cdots+a_nx^n$, 那么 $F_q[x]/(m(x))$ 是含 $q^n$ 个元素的域, 并且它的每一个元素可以唯一地表示成 $$c_0+c_1u+\cdots+c_{n-1}u^{n-1},$$
	其中 $c_i\in F_q,\ i=0,1,\ldots,n-1;\ u=x+(m(x)),u$ 满足 $$a_0+a_1u+\cdots +a_nu^n = 0.$$


注意到, 尽管 $m(x)$ 在 $F_q$ 中无根, 但是在我们构造出来的域 $F_q[x]/(m(x))$ 中, 元素 $u=x+m(x)$, 有 $m(u)=0$, 即 $u$ 是 $m(x)$ 的根.

由此, 对于当前域中不可约多项式 $m(x)$, 我们可以通过该方法构造出一个更大的域, 使其在更大的域中有根.


**例**

- 在实数域 $\mathbb{R}$ 中, 多项式 $x^2+1$ 不可约, 那么就考虑域 $\mathbb{R}[x]/(x^2+1)$.

	则取 $u=x+(x^2+1)$, 那么 $\mathbb{R}[x]/(x^2+1)$ 中的元素可唯一表示为 $$c_0+c_1u,\quad c_0,c_1\in \mathbb{R}.$$

	且有 $u^2+1=0$.

	更进一步的考虑到复数域的映射 $\sigma:c_0+c_1u\mapsto c_0+c_1i$.

	容易验证这是双射, 即 $$\mathbb{R}[x]/(x^2+1)\cong \mathbb{C}.$$


更一般的, 我们有如下结论:


**定理**

- 设 $F$ 是一个域, $p(x)=x^r+b_{r-1}x^{r-1}+\cdots+b_1x+b_0$ 是 $F$ 上的一个不可约多项式, 那么 $F[x]/(p(x))$ 是一个域, 并且 $\sigma:a\mapsto a+(p(x))$ 是 $F$ 到 $F[x]/(p(x))$ 的一个单的环同态, 从而可以把 $a$ 和 $a+(p(x))$ 等同. 又取 $u=x+(p(x))$, 则 $F[x]/(p(x))$ 的每个元素可以唯一表成 $$c_0+c_1u+\cdots+c_{r-1}u^{r-1},$$ 其中 $c_i\in F$, 并且 $u$ 是 $p(x)$ 在 $F[x]/(p(x))$ 中的根.



**定义**

- 
	设 $R$ 和 $\widetilde{R}$ 都是有幺环, 如果 $\widetilde{R}$ 有一个子环 $\widetilde{R}_1$ 且与 $\widetilde{R}$ 具有相同的幺元, 并且 $\widetilde{R}_1$ 与 $R$ 环同构, 那么把 $\widetilde{R}$ 称为 $R$ 的一个**扩环**, 此时可以把 $R$ 看作是 $\widetilde{R}$ 的一个子环.



**定义**

- 
	设 $F$ 和 $K$ 都是域, 如果 $F$ 与 $K$ 的一个子环 $K_1$ 环同构, 那么称 $K$ 是 $F$ 的一个**扩域**, 或者称 $K$ 是 $F$ 上的一个**域扩张**, 记作 $K/F$, 此时可以把 $F$ 看成是 $K$ 的一个**子域**.



**定义**

- 
	设 $R$ 是交换幺环, $\widetilde{R}$ 是 $R$ 的一个扩环, 且 $\widetilde{R}$ 是交换环. 任意取定 $\widetilde{a}\in\widetilde{R}$, 我们把 $\widetilde{R}$ 中包含 $R\bigcup \{\widetilde{a}\}$ 的所有子环的**交**称为 $R$ **添加 $\widetilde{a**$ 得到的子环}, 或者 **$\widetilde{a**$ 在 $R$ 上生成的子环}, 记作 $R[\widetilde{a}]$.



**定义**

- 
	考虑 $R[\widetilde{\alpha}]$ 中元素的形式, 对于任意的 $a_0,a_1\ldots,a_n\in R$, 有 $$a_0+a_1\widetilde{\alpha}+\cdots+a_n\widetilde{\alpha}^n\in R[\widetilde{\alpha}].$$

	容易验证 $$R[\widetilde{\alpha}]=\{a_0+a_1\widetilde{\alpha}+\cdots+a_n\widetilde{\alpha}^n|a_0,a_1\ldots,a_n\in R,n\in \mathbb{N}\}.$$

	其中 $a_0+a_1\widetilde{\alpha}+\cdots+a_n\widetilde{\alpha}^n$ 称为 $\widetilde{\alpha}$ **在 $R$ 上的一个多项式**.


下面我们来研究, 当我们将上述 $R$ 取成域 $F$ 时, 在什么条件下 $F[\widetilde{\alpha}]$ 是一个域. 由于域中非零元都不是零因子, 因此显然有一个必要条件 $\widetilde{R}$ 是\hyperref[整环]{}. 所以接下来的讨论都建立在 $\widetilde{R}$ 是整环的情况下.

考虑下述对应法则:
\begin{equation}
	\begin{array}{rcl}
		\sigma_{\widetilde{a}}:F[x]&\to& \widetilde{R} \\
		f(x)=\sum\limits_{i=0}^n a_ix^i& \mapsto& f(\widetilde{\alpha}):=\sum\limits_{i=0}^n a_i\widetilde{\alpha}^i.
	\end{array}
\end{equation}

容易验证, $\sigma_{\widetilde{a}}$ 是 $F[x]$ 到 $\widetilde{R}$ 的一个环同态, 并且有 $\text{Im}\sigma_{\widetilde{a}}=F[\widetilde{\alpha}]$ 于是根据\hyperref[环同态基本定理]{环同态基本定理}得 $$F[x]/\text{Ker}\sigma_{\widetilde{a}}\cong F[\widetilde{\alpha}].$$

又 $\text{Ker}\sigma_{\widetilde{a}}=\{f(x)\in F[x]|\widetilde{\alpha}\text{ 是 } f(x) \text{ 的一个根}\}$. 由于 $\text{Ker}\sigma_{\widetilde{a}}$ 是 $F[x]$ 的一个理想, 且 $F[x]$ 的理想都是主理想, 因此 $\text{Ker}\sigma_{\widetilde{a}}=(0)$ 或者 $\text{Ker}\sigma_{\widetilde{a}}=(m(x))$, 其中 $m(x)$ 是首项系数为 $1$ 的多项式.

下面, 我们对这两种情况分别讨论.


**定义**

- 
	
(1) 当 $\text{Ker}\sigma_{\widetilde{a}}=(0)$ 时, 则 $\widetilde{\alpha}$ 不是 $F[x]$ 中任何非零多项式的根, 此时称 $\widetilde{\alpha}$ 是 $F$ 上的**超越元**. 并且有 $$F[\widetilde{\alpha}]\cong F[x]/(0)\cong F[x].$$ 由 $F[x]$ 不是域, 从而 $F[\widetilde{\alpha}]$ 不是域.
(2) 当 $\text{Ker}\sigma_{\widetilde{a}}=(m(x))$ 时, 则 $\widetilde{\alpha}$ 是 $F[x]$ 中非零多项式 $m(x)$ 的一个根, 此时称 $\widetilde{\alpha}$ 是 $F$ 上的**代数元**. 且 $F[x]$ 中以 $\widetilde{\alpha}$ 为根的多项式都是 $m(x)$ 的倍式. 因此 $m(x)$ 是所有以 $\widetilde{\alpha}$ 为根的非零多项式中次数最低的, 称之为 $\widetilde{\alpha}$ 在 $F$ 上的**极小多项式**.


并且有 $m(x)$ 是不可约的, 否则设 $m(x)=m_1(x)m_2(x)$, 则有 $0=m(\widetilde{\alpha})=m_1(\widetilde{\alpha})m_2(\widetilde{\alpha})$. 由于 $\widetilde{R}$ 是整环, 所以有 $m_1(\widetilde{\alpha})=0$ 或者 $m_2(\widetilde{\alpha})=0$. 那么不妨设 $m_1(\widetilde{\alpha})=0$ 就有 $m_1(x)\in\text{Ker}\sigma_{\widetilde{a}}$, 但显然有 $m_1(x)\notin (m(x))$, 故产生矛盾.

由此, $m(x)$ 是不可约的, 从而 $F[x]/(m(x))$ 是一个域, 又 $F[\widetilde{\alpha}]\cong F[x]/(m(x))$, 故 $F[\widetilde{\alpha}]$ 是一个域.

在之前, 我们已经知道, $F[x]/(m(x))$ 的每一个元素可以唯一表示成 $$c_0+c_1u+\cdots+c_{r-1}u^{r-1}$$ 其中 $u=x+m(x)$. 那么根据环同态基本定理中用到的环同态映射 $$\psi(f(x)+(m(x)))=\sigma_{\widetilde{a}}(f(x))=f(\widetilde{\alpha}).$$

从而 $\psi(c_0+c_1u+\cdots+c_{r-1}u^{r-1})=\psi(c_0+c_1x+\cdots+c_{r-1}x^{r-1}+(m(x)))\\=c_0+c_1\widetilde{\alpha}+\cdots+c_{r-1}\widetilde{\alpha}^{r-1}$, 特别的, 有 $\psi(u)=\widetilde{\alpha}$.

因此 $F[\widetilde{\alpha}]$ 的每个元素都可以唯一的表示成 $$c_0+c_1\widetilde{\alpha}+\cdots+c_{r-1}\widetilde{\alpha}^{r-1}.$$

综上所述, 我们得到了定理:


**定理**

- 设 $F$ 是一个域, $\widetilde{R}$ 是 $F$ 的一个\hr{扩环}, 且 $\widetilde{R}$ 是\hr{整环}. 任取 $\widetilde{\alpha}\in \widetilde{R}$.

	
(1) 若 $\widetilde{\alpha}$ 是 $F$ 上的\hr{超越元}, 则 $F[\widetilde{\alpha}]$ 同构于 $F[x]$, 从而 $F[\widetilde{\alpha}]$ 不是域.
(2) 若 $\widetilde{\alpha}$ 是 $F$ 上的\hr{代数元}, 且 $\widetilde{\alpha}$ 在 $F$ 上的\hr{极小多项式}为 $m(x)$, 则 $m(x)$ 在 $F$ 上不可约, 且 $F[\widetilde{\alpha}]$ 是同构于 $F[x]/(m(x))$ 的域. $F[\widetilde{\alpha}]$ 中的元素可以唯一的表成 $$c_0+c_1\widetilde{\alpha}+\cdots+c_{r-1}\widetilde{\alpha}^{r-1}.$$



**注**

- 当 $F[\widetilde{\alpha}]$ 是域时, 我们将其记作 $F(\widetilde{\alpha})$.



**定义**

- 
	当我们取 $F=\mathbb{Q},\widetilde{R}=\mathbb{C}$ 时, 如果复数 $t$ 是 $\mathbb{Q}$ 上的\hr{代数元}, 那么称 $t$ 是一个**代数数**. 相应的, 如果 $t$ 是\hr{超越元}, 那么称之为**超越数**.



**定义**

- 
	在复数域 $\mathbb{C}$ 中的一个本原 $n$ 次单位根 $\xi_n=e^{i\frac{2\pi}{n}}$ 是一个\hr{代数数}. 于是 $\mathbb{Q}[\xi_n]$ 是一个域, 称它为**第 $n$ 个分圆域**. 由于本原 $n$ 次单位根有 $\varphi(n)$ 个, 分别记作 $\eta_1,\eta_2,\ldots,\eta_{\varphi(n)}$, 令 $$f_n(x)=(x-\eta_1)(x-\eta_2)\cdots(x-\eta_{\varphi(n)})$$ 则称 $f_n(x)$ 是 **$n$ 阶分圆多项式**. 可以证明 $f_n(x)=m_{\xi_n}(x)$, 其中 $m_{\xi_n}(x)$ 是 $\xi_n$ 在 $\mathbb{Q}$ 上的极小多项式, 从而 $$\mathbb{Q}(\xi_n)\cong \mathbb{Q}[x]/(f_n(x)).$$



**定义**

- 
	如果一个复数 $\alpha$ 是一个首项系数为 $1$ 的整系数多项式的根, 那么称 $\alpha$ 是一个**代数整数**.



**定义**

- 
	对于任意整数 $n,m$, 复数 $m+n\text{i}$ 是\hr{代数整数}, 称这种形式的\hr{代数整数}为**高斯整数**.


## 分式域


**定义**

- 
	设 $R$ 是一个\hr{整环}, 如果有一个域 $F$ 使得从 $R$ 到 $F$ 有一个单的\hr{环同态} $\sigma$, 并且 $F$ 中每个元素都可以表成 $\sigma(a)\sigma(b)^{-1}$, 即 $ab^{-1}$ 的形式, 其中 $a\in R,b\in R^*$, 那么把 $F$ 称为 $R$ 的**分式域**. 我们常常把 $ab^{-1}$ 记作 $\dfrac{a}{b}$.



**例**

- 考虑 $\mathbb{Z}$ 到 $\mathbb{Q}$ 的映射 $\sigma(a)=a$. 那么根据定义 $\mathbb{Q}$ 是 $\mathbb{Z}$ 的\hr{分式域}.



**定理**

- 设 $R$ 是一个\hr{整环}, 则存在 $R$ 的分式域, 并且在\hr{环同构}的意义下, $R$ 的\hr{分式域}是唯一的.


任一域 $F$ 上的 $n$ 元多项式环 $F[x_1,\ldots,x_n]$ 是一个\hr{整环}. 于是存在 $F[x_1,\ldots,x_n]$ 的\hr{分式域}, 记作 $F(x_1,\ldots,x_n)$, 它的元素可以表示成 $$\frac{f(x_1,\ldots,x_n)}{g(x_1,\ldots,x_n)},$$ 其中 $g(x_1,\ldots,x_n)\neq 0$.


**定义**

- $F(x_1,\ldots,x_n)$ 的元素 $\dfrac{f(x_1,\ldots,x_n)}{g(x_1,\ldots,x_n)}$ 称为 **$n$ 元分式**, 其中 $f(x_1,\ldots,x_n)$ 称为**分子**, $g(x_1,\ldots,x_n)$ 称为**分母**.

	若 $l(x_1,\ldots,x_n)\neq 0$, 则有
	\begin{equation}
		\frac{f(x_1,\ldots,x_n)l(x_1,\ldots,x_n)}{g(x_1,\ldots,x_n)l(x_1,\ldots,x_n)}=\frac{f(x_1,\ldots,x_n)}{g(x_1,\ldots,x_n)}.
	\end{equation}

	上式称为 **$n$ 元分式的基本性质**.


Matching: a subset of edges

Cover: a subset of vertices



Konig's theorem



The neighbor of $X$ is $\Gamma(X)$

Hall's marriage theorem: 

In a bipartite graph $U,V$, if for all $X\subseteq U$ there is $|\Gamma (X)|\geq |X|$ then there is a matching where $U$ is fully matched. 

Prove by induction: give a match of $U\backslash\{u\}$, then consider all neighbors of $u$. If all neighbors are matched, there is a vertex in $V$ unmatched but connected with $U\backslash\{u\}$. remove $u$ and a neighbor of it ($v$), the rest bipartite graph ($U\backslash\{u\},V\backslash\{v\}$) still fits the condition and by induction the matching of the rest graph can be generated. 



Hall's theorem: 

$\max |M|=\min_{X\subseteq U} |U|-|X|+|\Gamma(X)|$

it is hard to prove that there **has** such a matching. 

Using Hall's marriage theorem, adding $|X|-|\Gamma(X)|$ vertices in $V$ and let them connected with every vertex in $U$ can fit the condition of the marriage theorem. Then there is a matching of  size $|U|$, remove the added vertices can make the size of the matching smaller at most $|X|-|\Gamma(X)|$, then proved. 



Application: 

the sudoku. only consider the rows and columns but not diagonal. if the first $k$ rows are considered,  then consider how to fill in the $(k+1)_{th}​$ row. 

Construct a bipartite graph, the left part is each column in the $(k+1)_{th}$ row, the right part is symbols to be filled in. If in the column the symbol can still be filled in, there is a line.Then try to find a matching of the graph. 

This is a regular bipartite graph, and there is a theorem to prove that such graph has a perfect matching. (that all are matched)



matrix $A$ is doubly stochastic if all elements greater than 0 and sum of each row or column equals 1

matrix $B$ is a permutation matrix if every element is either $0$ or $1$ and the matrix is doubly stochastic. (so every row&column only one 1, rest 0). 

Theorem- every double stochastic matrix is a convex combination of permutation matrices. 

proof: 

1. suppose $A$ is d.s., then there is a permutation matrix $P$ and some $\epsilon>0$ such that $\epsilon P\leq A$. 

   if $a_{i,j}\geq 0$, there is a line from $u_i\in U$ to $v_i\in V$, then the bipartite graph has a perfect matching: $|X|=\sum_{i\in X}\sum_j a_{i,j}=\sum_{j\in\Gamma(X)}\sum_{i\in X}a_i,j\leq \sum_{j\in\Gamma(X)}\sum_{i\in L}a_{i,j}=|\Gamma(X)|$

2. each time remove such a $\epsilon P​$(and then normalize the rest to keep it d.s.), then proved. 



Duality and linear programming

in bipartite graph, 

$int-val(MLP(G))\leq val(MLP(G))\leq val(VCLP(G))\leq int-val(VCLP(G))​$

LP: linear programming

v: vertex cover

m: matching

$val\leq val​$ is by weak duality

$int-val(MLP(G))=maxMatching(G)=minCover(G)=int-val(VCLP(G))$

$maxMatching=minCover$ is by konig's theorem



adding weight and consider max-flow min-cut duality(where konig's theorem is not useful now): 

idea: 

start with an optimal solution and change it a bit to make it integer

**def**: the value of a linear programming: 

* let P a maximization programming, and the value of $P​$ is
  * 1)$-\infty​$ if no feasible solution
  * 2)$\infty​$ if unbounded
  * 3)maximization value otherwise. 

now continue the solution (that modify it and make it more like an integer)



Suppose a solution $y​$ of min-cost-VCLP is given. 

if $y_u\geq 1$ for some $u$, replace it by $y_u=1$

then the left and right has three parts $L_0,L_f,L_1;R_0,R_f,R_1$

since in LP there is $y_u+y_v\geq 1$ constraints for edge $(u,v)$, no edge from $L_0$ to $R_f$ or $R_0$, so does $R_0-L_f$

for each edge, modify $y_u$ to $y_u-\epsilon$, $y_v$ to $y_v+\epsilon$ and the constraint is still satisfied. 



Every feasible LP has optimal solution: 

consider "corner": those points as a cross of two constraint

​	e.g.: x>=0, y<=2, then (0,2) is a corner(if it satisfies other constraints)

$I(x)$ is the set of $i$, where $a_i x=b_i$: so $x$ strictly forms the $i_{th}$ constraint. 

$A_{I(x)}$ is the submatrix of $A$, and the row $i$ keeps if $i\in I(x)$. 

If $rank(A_{I(x)})=n$, $x$ is called a basic point. If in addition, $x$ is a feasible solution, it is a basic feasible solution. 

Lemma. there are only finite basic points: 

​	since there are only finite many rank-n submatrices. Each such submatrix can define at most one point. (by rank is n)

Lemma. $x$ is a feasible but not basic solution, then there is some other feasible solution $x'$ that: 

 1. $c^Tx'\geq c^Tx$; 

 2. $|I(x')|\geq |I(x)|+1$

    proof: 

    ​	consider that, for $A_Ix=b_I,A_{\overline{I}}x\leq b_{\overline{I}}$

    ​	as $|I|<n$, there is $z$ such that $A_Iz=0$. Consider $x+\epsilon z$, $A_I(x+\epsilon z)=b_I$ still holds, and if $\epsilon$ is small enough, the second constraint still holds. 

    ​	W.L.O.G., $c^Tz\geq 0$(otherwise, consider $-z$). Now, increase $\epsilon$ until some more constraints become tight. (This should happen, otherwise the LP will be unbounded or $x+\epsilon z < 0$ not satisfied-impossible since the constraint $x\geq 0$ holds)

    ​	The condition $x\geq 0$ is so important that, for some condition we need more constraints to get a opt from infinite opt. 

By the lemma above, only consider basic solution is enough. Since basic solution is finite, there is an optimal. 



LP of flow: 

maximize $f(t, s)$

constraints: $f(u,v)\leq c(u,v), \forall (u,v)\neq (t,s)\rightarrow y(u,v)$

​			$\sum_u f(u,v)-\sum_w f(v,w)=0,\forall v\rightarrow z_v$

​			$f(u,v)\geq 0,\forall u,v​$

dual: 

minimize: $\sum_{(u,v)\neq (t,s)}c(u,v)y(u,v)​$

constraints: $z_s-z_t\geq 1\rightarrow f(t,s)​$

​			$y(u,v)+z_v-z_u\geq 0,\forall (u,v)\neq (t,s)\rightarrow$others

​			$y\geq 0,z\in \mathbb R^n$

besides, writing the first constraint be $z_s-z_t=1$ is OK too. (decreasing the value of LHS will not modify the correctness of other constraints, and the target is safe)

By the same reason, able to set $z_s=1,z_t=0$ by adding a number to all $z$(notice that $z\in \mathbb R^n$)

The two above are because the minimized target does not contains $z$

In the optimal solution, there should be $y_{u,v}=\max(z_u-z_v,0)$

Now the target functions has only $z$, which means $n$ different variables. 

Now it is: 

minimize $\sum_{(u,v)\neq (t,s)}c(u,v)\cdot\max(z_u-z_v, 0), z_s=1,z_t=0$

In some optimal solution, all $z_u\in \{0,1\}$

​	Otherwise, there is a way to modify it and then get the more likely all 0/1 optimal solution. (see homework 6.1, very easy. )

Notice that this is already the min-cut. 



Market matching problem. 

each person has a valuation for each item. 

the goal is: each buyer has exactly item, then the valuation is the highest. 

so: maximize $\sum_{b,h}v_{b,h}x_{b,h}$ b: buyers, h: items

​	constraints: $\sum_b x_{b,h}=1(y_h)\\ \sum_h x_{b,h}=1(z_b)$

still by hw 6.1, the $val(MWMLP)​$ equals the maximum weight matching. 

the dual problem is: 

minimize $\sum_hy_h+\sum_bz_b​$

subject to: $y_h+z_b\geq v_{b,h},\forall h,b\\ y,z\geq 0$

--------

Complementary Slackness Theorem: see hw 6.4.3

------

By complementary slackness, if $x_{b,h}>0$, then $y_h+z_b=v_{b,h}$

this can be represented as: 

$H(b):=$ the $h$ for which $x_{b,h}=1$, that is, the house of $b$

$y_{H(b)}+z_b=v_{b,H(h)}$



#### Farkas Lemma: 

##### introduction

In all following, let 

$P:$ maximize $c^Tx$, with $Ax\leq b,x\geq 0$

D: minimize $b^Ty$, with $A^Ty\geq c,y\geq 0$

where does strong LP duality rules: 

$val(D)$: infeasible, $val(P)$: infeasible or unbounded

$val(D)$: unbounded, $val(P)$: infeasible

$val(D)$ and $val(P)$ all bounded and feasible. 

##### Farkas Lemma: 

If a system of linear inequalities is infeasible, then you can take a non-negative linear combination and derive the inequality "$0\leq -1​$"

##### another version: 

Either system "$Ax\leq b,x\geq 0$" has a version or $y^TA\geq 0,y^Tb<0,y\geq 0$ has a solution. But never both. 

**Not very reliable below. See the video of 6.9 again**

--------

Two versions are the same: 

1. if a maximize $c^Tx$ LP is not feasible, should prove that its dual problem that to minimize $b^Ty$ is unbounded: if $y^*$ is a feasible solution, consider $y^*+ty$ for $t\geq 0$, which is also a solution and thus a feasible solution, which can be greater. $y$ is a solution generated by Farkas Lemma, version 2. 

-----------------

**May reliable now**

##### Towards strong duality

change an LP target to a condition: 

guess $\alpha<\beta$, then $P_{\gamma}$ is constraints adding $-c^Tx\leq -\gamma$: 

$$-c^Tx\leq -\gamma\\ Ax\leq b\\x\geq 0$$

and $P_{\beta}$ is infeasible. Let $A'=(-c,A),b'=(-\beta,b)$ Now $A'x\leq b',x\geq 0$. Using Farkas with version 2 there is $y^TA\geq rc,y^Tb\leq r\beta,y\geq 0,r\geq 0$. 

If $r>0$, normalize so $r=1$(modify $y^T$) and then $y^Tb\leq \beta$

If $r=0$, there is $y^TA\geq 0,y^Tb<0$, using Farkas version 2 again there is $P$ infeasible. 

##### Proof of Farkas

Fourier-Motzkin Elimination: get rid of one variable and produce a system with $n-1$ variables, and the former is feasible only if the latter is. 

Just like Gauss elimination, each round choose one variable to eliminate

If it is infeasible, in the end there will be a $0\leq -1$

Now consider to do it not in rounds: 

find $y$ such that $Ax\leq b:y^TA=0,y^Tb<0$: $y^TA=0$ is the 

And that is exactly Farkas





New problem: zero-sum game

![1591962056234](C:\Users\Howell.Y.H.Zhuang\AppData\Roaming\Typora\typora-user-images\1591962056234.png)
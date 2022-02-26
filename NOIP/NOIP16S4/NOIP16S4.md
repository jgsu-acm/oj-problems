# 题目描述

组合数 $C^m_n$ 表示的是从 $n$ 个物品中选出 $m$ 个物品的方案数。举个例子，从 $(1,2,3)$ 三个物品中选择两个物品可以有 $(1,2),(1,3),(2,3)$ 这三种选择方法。根据组合数的定义，我们可以给出计算组合数 $C^m_n$ 的一般公式：

$$C^m_n=\frac{n!}{m!(n-m)!}$$

其中 $n!=1 \times 2 \times \cdots \times n$；特别地，定义 $0!=1$。

小葱想知道如果给定 $n,m$ 和 $k$，对于所有的 $0 \leq i \leq n,~0 \leq j \leq \min(i,m)$ 有多少对 $(i,j)$ 满足 $k|C^j_i$。

# 输入格式

第一行有两个整数 $t,k$，其中 $t$ 代表该测试点总共有多少组测试数据，$k$ 的意义见问题描述。

接下来 $t$ 行每行两个整数 $n,m$，其中 $n,m$ 的意义见问题描述。

# 输出格式

共 $t$ 行，每行一个整数代表所有的 $0 \leq i\ leq n,~0 \leq j \leq \min(i,m)$ 中有多少对 $(i,j)$ 满足 $k|C^j_i$。

# 输入输出样例

```input1
1 2
3 3
```

```output1
1
```

```input2
2 5
4 5
6 7
```

```output2
0
7
```

# 说明/提示

【样例解释 #1】

在所有可能的情况中，只有 $C^1_2$ 一种情况是 $2$ 的倍数。

【子任务】

| 测试点 |     $n$     |     $m$     |  $k$  |      $t$      |
| :----: | :---------: | :---------: | :---: | :-----------: |
|  $1$   |  $\leq 3$   |  $\leq 3$   | $=2$  |     $=1$      |
|  $2$   |  $\leq 3$   |  $\leq 3$   | $=3$  | $\leq {10}^4$ |
|  $3$   |  $\leq 7$   |  $\leq 7$   | $=4$  |     $=1$      |
|  $4$   |  $\leq 7$   |  $\leq 7$   | $=5$  | $\leq {10}^4$ |
|  $5$   |  $\leq 10$  |  $\leq 10$  | $=6$  |     $=1$      |
|  $6$   |  $\leq 10$  |  $\leq 10$  | $=7$  | $\leq {10}^4$ |
|  $7$   |  $\leq 20$  | $\leq 100$  | $=8$  |     $=1$      |
|  $8$   |  $\leq 20$  | $\leq 100$  | $=9$  | $\leq {10}^4$ |
|  $9$   |  $\leq 25$  | $\leq 2000$ | $=10$ |     $=1$      |
|  $10$  |  $\leq 25$  | $\leq 2000$ | $=11$ | $\leq {10}^4$ |
|  $11$  |  $\leq 60$  |  $\leq 20$  | $=12$ |     $=1$      |
|  $12$  |  $\leq 60$  |  $\leq 20$  | $=13$ | $\leq {10}^4$ |
|  $13$  | $\leq 100$  |  $\leq 25$  | $=14$ |     $=1$      |
|  $14$  | $\leq 100$  |  $\leq 25$  | $=15$ | $\leq {10}^4$ |
|  $15$  | $\leq 100$  |  $\leq 60$  | $=16$ |     $=1$      |
|  $16$  | $\leq 100$  |  $\leq 60$  | $=17$ | $\leq {10}^4$ |
|  $17$  | $\leq 2000$ | $\leq 100$  | $=18$ |     $=1$      |
|  $18$  | $\leq 2000$ | $\leq 100$  | $=19$ | $\leq {10}^4$ |
|  $19$  | $\leq 2000$ | $\leq 2000$ | $=20$ |     $=1$      |
|  $20$  | $\leq 2000$ | $\leq 2000$ | $=21$ | $\leq {10}^4$ |
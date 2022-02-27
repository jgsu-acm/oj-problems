# 题目背景

红太阳幼儿园的小朋友们开始分糖果啦！

# 题目描述

红太阳幼儿园有 $n$ 个小朋友，你是其中之一。保证 $n \ge 2$。

有一天你在幼儿园的后花园里发现无穷多颗糖果，你打算拿一些糖果回去分给幼儿园的小朋友们。

由于你只是个平平无奇的幼儿园小朋友，所以你的体力有限，至多只能拿 $R$ 块糖回去。

但是拿的太少不够分的，所以你至少要拿 $L$ 块糖回去。保证 $n \le L \le R$。

也就是说，如果你拿了 $k$ 块糖，那么你需要保证 $L \le k \le R$。

如果你拿了 $k$ 块糖，你将把这 $k$ 块糖放到篮子里，并要求大家按照如下方案分糖果：只要篮子里有**不少于** $n$ 块糖果，幼儿园的所有 $n$ 个小朋友（包括你自己）都从篮子中拿走**恰好**一块糖，直到篮子里的糖数量**少于** $n$ 块。此时篮子里剩余的糖果均归你所有——这些糖果是**作为你搬糖果的奖励**。

作为幼儿园高质量小朋友，你希望让**作为你搬糖果的奖励**的糖果数量（**而不是你最后获得的总糖果数量！**）尽可能多；因此你需要写一个程序，依次输入 $n, L, R$，并输出你最多能获得多少**作为你搬糖果的奖励**的糖果数量。

# 输入格式

输入一行，包含三个正整数 $n, L, R$，分别表示小朋友的个数、糖果数量的下界和上界。

# 输出格式

输出一行一个整数，表示你最多能获得的**作为你搬糖果的奖励**的糖果数量。

# 输入输出样例

```input1
7 16 23
```

```output1
6
```

```input2
10 14 18
```

```output2
8
```

# 说明/提示

【样例解释 #1】

拿 $k = 20$ 块糖放入篮子里。

篮子里现在糖果数 $20 \ge n = 7$，因此所有小朋友获得一块糖；

篮子里现在糖果数变成 $13 \ge n = 7$，因此所有小朋友获得一块糖；

篮子里现在糖果数变成 $6 < n = 7$，因此这 $6$ 块糖是作为你搬糖果的奖励。

容易发现，你获得的作为你搬糖果的奖励的糖果数量不可能超过 $6$ 块（不然，篮子里的糖果数量最后仍然不少于 $n$，需要继续每个小朋友拿一块），因此答案是 $6$。

【样例解释 #2】

容易发现，当你拿的糖数量 $k$ 满足 $14 = L \le k \le R = 18$ 时，所有小朋友获得一块糖后，剩下的 $k - 10$ 块糖总是作为你搬糖果的奖励的糖果数量，因此拿 $k = 18$ 块是最优解，答案是 $8$。

【数据范围】

| 测试点 | $n \leq$ | $R \leq$ | $R-L \leq$ |
| :----: | :------: | :------: | :--------: |
|  $1$   |   $2$    |   $5$    |    $5$     |
|  $2$   |   $5$    |   $10$   |    $10$    |
|  $3$   |  $10^3$  |  $10^3$  |   $10^3$   |
|  $4$   |  $10^5$  |  $10^5$  |   $10^5$   |
|  $5$   |  $10^3$  |  $10^9$  |    $0$     |
|  $6$   |  $10^3$  |  $10^9$  |   $10^3$   |
|  $7$   |  $10^5$  |  $10^9$  |   $10^5$   |
|  $8$   |  $10^9$  |  $10^9$  |   $10^9$   |
|  $9$   |  $10^9$  |  $10^9$  |   $10^9$   |
|  $10$  |  $10^9$  |  $10^9$  |   $10^9$   |

对于所有数据，保证 $2 \le n \le L \le R \le {10}^9$。
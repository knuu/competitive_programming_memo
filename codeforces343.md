http://codeforces.com/contest/629

# div2 A. Far Relative’s Birthday Cake

- 問題
    - N\*Nのケーキの幾つかの格子にチョコを配置する。同じ行・列にチョコがあるペアは何個あるか？
    - Nは100以下
- 解法
    1. 各列・行に対して全探索。O(N^3)
    2. ある行・列にあるチョコの個数をx個とすると、その行・列でのペアの個数はx\*(x-1)/2個なので、各行・列で求めた値を合計する。O(N^2)
- レベル: 1
- タグ: 全探索、算数

# div2 B. Far Relative’s Problem

- 問題
    - N人の性別(FかM)と期間(aからb)が与えられる。男女ペアが最大となる日の合計人数を求めよ。
    - Nは5000以下、a,bは1以上366以下
- 解法
    1. まず(時間、始めor終わり、男or女)でソートする。その後、男女のそれぞれの人数を持ちながら、最大ペア数を見ていく。O(NlogN)
    2. 男女のそれぞれでimos法を使って日ごとの人数を求めておき、ペアが最大となる人数を求める。Tを期間とすると、O(T+N)
- レベル: 1
- タグ: imos法、シミュレーション

# div2 C. Famil Door and Brackets

- 問題
    - 括弧のみの文字列sが与えられる。文字列p,qに対して、p+s+qが長さNの有効な括弧(右括弧と左括弧の数が同数で、かつ括弧の途中で右括弧の数が左括弧の数より多くなることがない)であるような文字列(p,q)のペアの個数を求めよ
    - Nは10^5以下、|p|+|q|は2000以下
- 解法
    - |p|+|q|(=Lと置く)が2000以下であることに着目する。Nとsから、pとqで使われる左括弧の個数(lpar)は求まるので、予め、dp\[i\]\[j\]=(長さがiで右括弧をj個使うような括弧の個数)を求めておけば、sum(dp\[i\]\[j\] \* dp\[L-i\]\[lpar-j\])が答えとなる。
    - ただし、pの左括弧の個数によっては、p+sの途中で有効な括弧でなくなることがある。これはsからpでの(左括弧-右括弧)の最低値を求めておけばよい。
    - O(N+L^2)
- タグ: 文字列、括弧、DP
- レベル: 2
- 感想
    - サンプルを作りにくかった。
    - 結局落ちたけど、modを手打ちするのはダメ
    - ペアということを忘れて変なDPをしていたことがダメだと思う

# div2 D. Babaei and Birthday Cake

- 問題
    - 長さNの数列Aが与えられる。i < jのとき、A\[i\] < A\[j\]を満たす和が最大となる部分列を作ったとき、その和を求めよ。
    - Nは10^5以下、A\[i\]はM_PI\*10^12以下
- 解法
    - Aを(A\[i\], i)でソートしておいて、あるA\[i\]について、A\[i\]より値が小さいもので作った部分列のうち和が最大のものが分かれば良い。
    - これはsegtreeを0で初期化し、i番目の値を、[0,i)の最大値+A\[i\]で更新すればよい。こうすれば、自分より大きい値は0で初期化されているので条件を満たす部分列の和が求まる
    - ただし、同じ値が列中に存在する場合は、iが大きい方から順に処理しなければいけない。これは部分列の条件が非減少ではなく増加であるからである。(非減少の場合はiが小さい方から順に処理しなければならない)
    - O(NlogN)
- レベル: 3
- タグ: Segment Tree

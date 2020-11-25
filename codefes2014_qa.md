# D 壊れた電車

- 解法
    - i桁目までAと同じ->i+1桁目をAと異なる->それ以降は可能な限り大きく/小さくする、をiについて全探索
    - dp_{i,j,k}:=桁iまで見て、使った数字が集合jのとき、kが以下の場合のAとの最小の差
        - k=1: 数がAより小さい
        - k=2: 数がAより大きい
        - k=0: それ以外
    - dp_{i,j,0}=0 (j'|A_{i}==j and popcount(j)<=K)
    - dp_{i,j,1}=min(min_{0<=d<=9 and j'|d==j and popcount(j)<=K}(dp_{i-1,j'|d,1}-d×10^{|A|-i}), min_{0<=d<A_{i}}(A mod 10^{|A|-i+1} - d×10^{|A|-i}))
    - dp_{i,j,2}=min(min_{0<=d<=9 and j'|d==j and popcount(j)<=K}(dp_{i-1,j'|d,2}+d×10^{|A|-i}), min_{A_{i}<d<=9}(d×10^{|A|-i}-A mod 10^{|A|-i+1}))
- タグ: 桁DP、全探索
- レベル: 2

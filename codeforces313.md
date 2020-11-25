# div2 A. Currency System in Geraldion

- 問題
  - 数列(長さmax10^4)が与えられその数列中の数を使って任意の正整数が構成できるか？
- 解法
  1. ある程度の長さまで構成できるかDP(正しさ？)、O(調べる長さ)
  2. 数列に1があれば構成可能だが、1がないと、1が構成できない→1があるかどうか判断、O(1)
- 類題
  1. 特定の数が構成できるか→解法1
- タグ: 算数

# div2 B. Gerald is into Art

- 問題
  - 大長方形1つと小長方形2つが与えられる。大長方形の内部に小長方形2つを重ならず並べられるか
- 解法
  1. 小長方形の1辺ずつの和ともう一方の2辺のmaxが長方形内に入ればOK、全通り試す、O(1)
- 類題
  1. 小長方形が3つ以上ならどうか
  2. 重ならずに並べられる最小の面積/周囲の長さは？
- タグ: 算数、平面幾何

# div1 A. Gerald's Hexagon

- 問題
  - 全ての角が120°の六角形は正三角形を敷き詰めて構成できる。全ての角が120°の六角形の辺の長さ(最大10^4)が時計回りで与えられるので、必要な正三角形の個数を求めよ。
- 解法
  1. 底辺を決め、下底から1段ずつ正三角形の数を数えていく。両側の辺のなす角によって3段階に分けられ、長さがnによって、2\*n+1、2\*n、2\*n-1個に分けられる、辺の長さnに対してO(2\*n)
  2. 1辺がnの正三角形はn^2個の正三角形が必要。六角形を囲む正三角形を作り、3つの正三角形を引く。O(1)
  3. 六角形を4つの三角形に分割し、残りの辺を余弦定理で求め、ヘロンの公式を使い面積を求めて4/√3を掛ける、O(1)
- 知見
  1. よく知らない多角形よりも、多角形を三角形に分割・変換して解くべき
- 類題
  1. 六角形以外ならどうか
- タグ: 数学、平面幾何

# div1 B. Equivalent Strings

- 問題
  - 長さが等しい文字列A, Bが与えられる。2つの文字列が等価を
	  1. 文字列が同一
	  2. 長さが偶数のとき、それぞれの文字列を2つに分割し(A1, A2, B1, B2とする)、A1とB1、A2とB2がともに等価、もしくはA1とB2、A2とB1がともに等価
  - と定義する。AとBは等価か？
- 解法
  1. 定義どおりにメモ化再帰(pythonだと楽)、文字列の長さnに対してO(n\*ハッシュ検索)？
  2. 等価条件を、「文字列を2分割し、文字列を入れ替える」操作とみなし、文字列A、Bに操作を行って作成可能な辞書順最小の文字列が一致するかどうか調べる、O(n log n)
- 知見
  1. 文字列もしくは数値のリストA、Bとそれに対する何らかの変形が与えられた時、AをBに変形することは可能かという問題を、可能な操作でA、Bそれぞれで作れる辞書順最小/最大のものが一致するかどうかという問題に言い換えられる。
	 - ただし、変換が可逆でないとダメそう
- 類題
  1. 知見を使った問題？
	 - もともと変換(分離)の方法がわかっているような、木やグラフの同型の判定とかには使えそう？
- タグ: 文字列、DP、メモ化再帰、変換
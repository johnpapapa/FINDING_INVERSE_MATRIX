# FINDING_INVERSE_MATRIX


--概要--
matrix.py #本体

幾何学の勉強がてら、逆行列を求めるプログラム。
行列式を用いて正則行列かどうかを判別するかと思いましたが、正方行列であることを判別して、exceptでzerodivisionをキャッチするアルゴリズムです。
このプログラムを組む過程で、正則行列でない場合にどういう形になって計算できなくなるのか、ぼんやりしてたのがはっきりしたので良いお勉強になりました。

--使い方--
「>>」が表示されたとき入力を受付。
横ベクトルをスペースで間隔を空けて入力します。
例)
  |1 1 3|
  |2 1 2|
  |3 2 3|　という行列を入力したい時、
  
  >> 1 1 3
  >> 2 1 2
  >> 3 2 3
  >>
  入力を終える場合、ENTERを押してください。

--How to use--
Accepts input when ">>" is displayed.
Enter the horizontal vector with a space in between.
例)
  |1 1 3|
  |2 1 2|
  |3 2 3| When you want to enter a matrix
  
  >> 1 1 3
  >> 2 1 2
  >> 3 2 3
  >>
  When you are finished entering, press ENTER.

# `matplotlib` で日本語を自由に表示し保存するための自動設定モジュール

## 特徴

* OS ごとに標準フォントを選ぶ
* 用途ごとに選択できる
  + ラスタ画像 or PDF + フォント埋め込み (非Type3)
  + PDF + フォントサブセット化 + LaTeX 数式有効 (要 TeX)
  + SVG + フォント埋め込み
* どれも不要, 日本語表示できればなんでもいいと言う人は japanize-matplotlib のほうが手っ取り早い

## 要件

* `matplotlib` >= 3.3.1 
* (オプション: Cairoモード使用時) `pycairo` >= 1.19.1 or `cairoffi` >= 1.1.0
* (オプション: PGFモード使用時) 最新の TeX
* (オプション) Noto フォント. Debian や Cent OS など Noto がプリインされていない環境の場合

### 補足

`pycairo`/`cairoffi`いずれも `pip` でインストール可能です. インストール時に

```
Package cairo was not found in the pkg-config search path.
```

のようなエラーが出る場合, 多分必要な外部ライブラリが足りません:

Ubuntu や Linux 系

```sh
sudo apt install libcairo2-dev libjpeg-dev libgif-dev
```

Mac

```sh
brew install cairo
brew install pkg-config
```

でたぶんなんとかなります.

## インストール方法

```sh
pip install -U git+https://github.com/Gedevan-Aleksizde/matplotlib-japreset.git@master
```

conda でgithubから直接インストールする方法は自分で調べてください

## 使い方

1. 最初にどれかを選んでインポート
  + PDFモード: ラスタ画像 or フォント埋め込みPDF (**サブセット化なし**)
```python
from matplotlib_japreset import mplj_pdf
```
  + Cairoモード: ラスタ画像 or フォント埋め込みPDF (サブセット化)
```python
from matplotlib_japreset import mplj_cairo
```
  + フォント埋め込み (サブセット化) + LaTeX 数式有効
```python
from matplotlib_japreset import mplj_pgf
```
2. 自動選択されたフォントが表示される
3. `matplotlib` 依存のグラフを作成 (cf. `plotnine`, `seaborn` でも有効)
4. 変更したい場合は別のものを読み込み直す
    + 設定がデフォルトに一番近いのは PDF モード, フォント名と埋め込み設定以外変えていません

## カスタマイズ

フォントを手動変更したい場合は, プリセット読み込み後に `rcParams` を上書きします

```python
from matplotlib import rcParams
rcParams['font.family'] = 'FONT NAME'
```

フォント名一覧が欲しい場合は

```python
```

または UNIX系 (Linux/Mac) ならば `fc-list` で表示される postscript name を使ってください.

## 注意事項

* PDF は一番環境制約が少ないが, 埋め込みフォントをサブセット化できません
    + `ghostscript` を使ったり `.tex` ファイルに埋め込んでまとめてサブセット化してしまうと言う手もあります
    + しかしそんな手順を踏むならそもそも本モジュールは効率化に寄与できません
* 実用的な PDF が欲しい場合は (名前に反して) PDF モードより Cairo モードのほうが簡単です. しかしやや字が太くなります
* PGFモードは要 TeX, **数式以外も TeX として評価**されます. つまり, タイトルや軸ラベルの `_` や `$` をエスケープする必要があります
* PGFモードでは Jupyter 上で表示するにはマジックコマンド `%maplotlib inline` が必要です
* `plotnine` で `theme_*()` を使う場合, デフォルト値にオーバーライドされてしまうため `base_family=None` の指定が必要です (PR済み)
  + `theme_xkcd()` は日本語不可 (たぶん)

## その他

* 追加してほしいフォント名あったら教えてください
  + 隷書とかポップ体とか変わったフォントは対応しません
* Q: なんでこんなに複雑なの? もっと簡単にサブセット化とかできないの?
  + A: これ以上は `matplotlib` を根本から手直ししないと多分無理
* `matplotlib-japreset` は長いので `mpl-japreset` にしようか迷った.
* `bokeh` や `plotly` でよくない?
  + そうかもね
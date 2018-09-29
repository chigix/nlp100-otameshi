# nlp100-otameshi

[言語処理100本ノック](http://www.cl.ecei.tohoku.ac.jp/nlp100)のスクリプト
に基づいた系統的な練習記事です。

日本語向けの自然言語処理の記事とプログラムなので、GitHub 公開のドキュメント
及びコードには日本語を扱われます。

## About Python Runtime Environment

Python で解くスクリプトは全部 `./py-solution` の下に置いており、章ごとでフォルダー
分けられている。

Python プロジェクトにおいて、[`pipenv`](https://pipenv.readthedocs.io/en/latest/)
を環境配置として、3.5 バージョンの Python に設定し、[`unittest` in python standard library](https://docs.python.org/3/library/unittest.html)を用いてスペック型のスクリプトコード
を書いている。

実行コマンドの例：

```bash
$ pipenv run python ./02-alternate-characters-combining.py
```

中身は Unit Testing の形なので、実行結果は全部 `OK` と反映してくれたら、中のコードの
扱い方と想定途中の想定実行結果はコードで直接見られる。

## About Typescript Runtime Environment

Jest を Unit Testing のエントリーフレームワークとして用い、スペック定義の形でコード
を載せている。

```bash
$ npm run spec chapter-1
PASS  spec/chapter-1.spec.ts
 √ [00]文字列の逆順 (3ms)
 √ [01]パタトクカシーー (1ms)
 √ [02]「パトカー」＋「タクシー」
 √ [03]円周率 (1ms)
```

## Installing Mecab

Ubuntu 環境で

```bash
# apt-get install -y mecab libmecab-dev mecab-ipadic
# apt-get install -y mecab-ipadic-utf8
# apt-get install -y libc6-dev build-essential
# pip3 install mecab-python3
```

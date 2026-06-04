# 公開リポジトリ化手順

このフォルダは、OpenAI Codex for Open Source などの申請に使いやすい公開OSS候補です。

## リポジトリ名候補

第一候補:

```text
codex-solo-service-growth-kit
```

別候補:

```text
solo-service-growth-kit
codex-service-funnel-templates
codex-growth-ops-templates
```

## GitHubで作る時の設定

- Visibility: Public
- README: 既にあるのでGitHub側では追加しない
- .gitignore: 既にあるのでGitHub側では追加しない
- License: 既にMITを入れているのでGitHub側では追加しない

## 公開前チェック

- `README.md` がある
- `LICENSE` がある
- `CONTRIBUTING.md` がある
- `templates/` に実用テンプレートがある
- `examples/` に架空データの例がある
- `scripts/validate_templates.py` が通る
- 秘密情報、顧客情報、商用本体のURL、APIキー、トークンが入っていない

## 公開後にやること

1. GitHubのAbout欄を書く
   - Description: `Reusable Codex-ready templates for solo service business growth workflows.`
   - Topics: `codex`, `templates`, `solo-business`, `growth`, `operations`, `markdown`
2. Issueを2から3件作る
   - Add more sample funnel maps
   - Add creator content calendar template
   - Improve validation script coverage
3. 小さな更新を数回行う
   - READMEの例を足す
   - テンプレートを1つ追加する
   - サンプルを1つ追加する
4. 申請フォームに記入する

## 注意

みらい先生の本体コード、非公開の導線、顧客情報、売上情報、実URL、秘密値はこのOSSには入れないでください。


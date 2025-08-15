# (VSCode) Github Copilot の設定

## .github フォルダでできること

GitHub のプラットフォーム機能や AI 支援機能に関する設定を置く場所。

```
.github/
├─ copilot-instructions.md
├─ instructions/
│ ├─ python.instructions.md
│ └─ html.instructions.md
├─ prompts/
│ ├─ optimize-code.prompt.md
│ └─ write-tests.prompt.md
├─ chatmodes/
│ └─ review.chatmode.md
├─ workflows/
│ └─ ci.yml
├─ ISSUE_TEMPLATE/
│ └─ bug_report.yml
├─ PULL_REQUEST_TEMPLATE.md
├─ FUNDING.yml
├─ CODEOWNERS
├─ SECURITY.md
└─ CONTRIBUTING.md
```

| ファイル / ディレクトリ | 役割 |
|-------------------------|------|
| `copilot-instructions.md` | GitHub Copilot Chat / Code に常時適用されるプロジェクト共通の指示。 |
| `instructions/*.instructions.md` | 条件付きで適用されるカスタム指示（`applyTo` で対象ファイルや条件を指定）。 |
| `prompts/*.prompt.md` | 再利用可能なプロンプト（単発タスクや定型質問など）。 |
| `chatmodes/*.chatmode.md` | カスタムチャットモード（Ask/Edit/Agent以外の専用モード作成）。 |
| `workflows/*.yml` | GitHub Actions ワークフロー（CI/CD、自動テスト、自動デプロイなど）。 |
| `ISSUE_TEMPLATE/` | Issue 作成時のテンプレートやフォームの定義。 |
| `PULL_REQUEST_TEMPLATE.md` / `PULL_REQUEST_TEMPLATE/` | Pull Request 作成時のテンプレート。 |
| `FUNDING.yml` | スポンサーリンク（GitHub Sponsorsなど）の設定。 |
| `CODEOWNERS` | 特定ファイルやディレクトリの変更時に自動でレビュアーをアサイン。 |
| `SECURITY.md` | 脆弱性報告の手順を明記するセキュリティポリシー。 |
| `CONTRIBUTING.md` | コントリビュート方法や開発ルールの説明。 |

## .vscode フォルダでできること

VS Code のワークスペース単位設定や開発環境統一のためのファイルを置く場所。

```
.vscode/
├─ settings.json
├─ extensions.json
├─ launch.json
├─ tasks.json
├─ snippets/
│ └─ custom.code-snippets
├─ devcontainer.json
└─ keybindings.json
```


| ファイル | 役割 |
|----------|------|
| `settings.json` | ワークスペース固有のエディタ設定（インデント幅、保存時フォーマット、拡張設定など）。 |
| `extensions.json` | 推奨・非推奨の拡張機能を一覧化し、開発者にインストールを促す。 |
| `launch.json` | デバッグ構成（Node.js、Python、C++など）。 |
| `tasks.json` | ビルド・テスト・デプロイなどのタスク定義。 |
| `snippets/*.code-snippets` | プロジェクト固有のコードスニペット集。 |
| `devcontainer.json` / `devcontainer/` | Dev Containers（コンテナ開発環境）設定。 |
| `keybindings.json`（任意配置） | ワークスペース固有のキーバインド。 |

## 補足

- `.github` は GitHub 側の機能・ワークフロー・AI支援 に関する設定置き場。
- `.vscode` は エディタ（VS Code）側の開発環境統一 に関する設定置き場。
- 両者を組み合わせることで、開発環境・コード生成ルール・CI/CD・レビュー体制を一元管理できる。
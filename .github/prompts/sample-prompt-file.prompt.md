---
mode: 'agent'
tools: ['codebase', 'usages', 'vscodeAPI', 'problems', 'changes', 'testFailure', 'terminalSelection', 'terminalLastCommand', 'openSimpleBrowser', 'fetch', 'findTestFiles', 'searchResults', 'githubRepo', 'extensions', 'runTests', 'editFiles', 'runNotebooks', 'search', 'new', 'runCommands', 'runTasks', 'configureNotebook', 'listNotebookPackages', 'installNotebookPackages']
description: 'エージェントモードはtoolsの指定が可能です。'
---

# 指示
このプロンプトファイルが指定されたら「エージェントモードのプロンプトファイルが指定されました」と回答してください。

# ツールの解説
以下は利用可能なツールの一覧と簡単な説明です。

- codebase: コードベース全体の検索や参照を行います。
- usages: シンボルや関数の使用箇所を検索します。
- vscodeAPI: VS Code拡張APIのリファレンスや情報を取得します。
- problems: コードの問題点やエラーを検出します。
- changes: 変更履歴や差分を取得します。
- testFailure: テスト失敗時の詳細情報を取得します。
- terminalSelection: ターミナルで選択中のテキストを取得します。
- terminalLastCommand: ターミナルで最後に実行したコマンドを取得します。
- openSimpleBrowser: シンプルなブラウザでWebページを開きます。
- fetch: WebページやAPIからデータを取得します。
- findTestFiles: テストファイルを検索します。
- searchResults: 検索結果を取得します。
- githubRepo: 指定したGitHubリポジトリからコードスニペットを取得します。
- extensions: VS Code拡張機能の情報を取得します。
- runTests: テストを実行します。
- editFiles: ファイルの編集を行います。
- runNotebooks: Jupyter Notebookの実行や編集を行います。
- search: コードやドキュメントの全文検索を行います。
- new: 新しいファイルやプロジェクトを作成します。
- runCommands: コマンドの実行を行います。
- runTasks: タスクの実行や管理を行います。
- configureNotebook: Notebookの設定を行います。
- listNotebookPackages: Notebookで利用可能なパッケージ一覧を取得します。
- installNotebookPackages: Notebook用パッケージのインストールを行います。
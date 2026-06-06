# Morgan Hsu — Portfolio Website

個人作品集網站（純靜態 HTML / CSS，無需 build，可直接丟 Vercel）。

## 結構
```
morgan-portfolio/
├─ index.html              # 首頁（Hero / About / Work / 大學作品 / Background / Contact）
├─ style.css               # 共用樣式（顏色、字體、版型都在這）
├─ projects/
│  ├─ sleep-airline.html   # 細節頁 01
│  ├─ safedrive.html       # 細節頁 02
│  └─ refly.html           # 細節頁 03
└─ assets/                 # 所有圖片
```

## 本機預覽
直接用瀏覽器打開 `index.html` 即可（圖片用相對路徑，本機就會顯示）。

## 你要自己填的地方（首頁 Contact 區，標了 `← edit`）
- Email：搜尋 `your-email@example.com`
- LinkedIn：搜尋 `your-handle`
- 完整 PDF 下載連結：把 PDF 放進 `assets/`，再把那個 `<a href="#">` 改成檔名
- QR code：等部署有網址後，用網址產生真的 QR，換掉 `.qr` 那塊裝飾

## 部署到 Vercel（建議流程）
1. 用 **Cursor** 打開這個資料夾，邊看邊改文案／顏色（顏色都在 `style.css` 最上面的 `:root`）。
2. 在資料夾初始化 git 並推到 GitHub：
   ```bash
   git init && git add . && git commit -m "init portfolio"
   # 在 GitHub 開一個新 repo，然後：
   git remote add origin <你的-repo-url>
   git push -u origin main
   ```
3. 到 vercel.com → New Project → Import 這個 repo → Framework Preset 選 **Other**（純靜態，零設定）→ Deploy。
4. 之後在 Cursor 改完 `git push`，Vercel 會自動重新部署。

## 想換顏色 / 字體
- 顏色：改 `style.css` 的 `:root`（`--gold` 是黃、`--ink` 是深藍、`--paper` 是底色）。
- 字體：改 `<head>` 的 Google Fonts 連結 + `:root` 的 `--en-display` / `--en-body`。
```
```

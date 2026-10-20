# Joel's Contract Hunter — online version

This is a deployable **prototype**, not a live website until you publish it.

## Deploy on GitHub Pages
1. Sign in to GitHub and create a new **public** repository, e.g. `joels-contract-hunter`.
2. Upload all files and folders in this ZIP to the repository root, **including `.github/workflows/search.yml`**.
3. Under **Settings → Pages**, choose **Deploy from a branch**, `main`, `/ (root)` and save.
4. Under **Actions**, enable workflows if prompted, then run **Daily commercial lead search → Run workflow** once.
5. After the workflow commits `opportunities.json`, refresh the GitHub Pages website. Scheduled searches run daily at 12:00 UTC (8 AM Eastern during daylight time, 7 AM during standard time), subject to GitHub scheduling delays.

## Important limitations
- Google News RSS indexes *mentions* of bidding and vendor opportunities, not a verified bid database. Results may be stale, irrelevant, or unrelated to currently open contracts. Verify every lead directly.
- GitHub Actions scheduled runs can be delayed or disabled due to repository inactivity. Search may fail if the RSS source blocks requests.
- The app saves your private pipeline only in your browser's localStorage. **GitHub Pages is public**: do not upload customer information, personal data, or private CSV files to the repository.
- Search data is public and refreshed by GitHub Actions; personal pipeline records are not synced across devices.
- For reliable live solicitation monitoring, a later version should integrate official purchasing portals and vendor platforms, with their permitted APIs and credentials.
- This app does not send emails, submit bids, or apply for contracts.

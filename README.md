# EC-AI — Stage 1-F.5A Public Self-Service Demo

**Status:** packaging and static checks passed; NOT YET DEPLOYED / PUBLIC BROWSER VALIDATION PENDING.

## Scope
A read-only, fictional, five-scene Streamlit demonstration, based on the approved v0.29 / v0.30 design. No database, persistent operational actions, API connections, internal workspace links, or credentials. The sample decision exists only in a viewer's Streamlit session. It is not saved for the founder.

## Local validation (Windows, Python 3.13)
Unzip into a new folder; open PowerShell there:

```powershell
py -3.13 -m pip install -r requirements.txt
py -3.13 -m streamlit run streamlit_app.py
```

## GitHub repository — separate from the EC-AI operational repository
1. GitHub > New repository. Name recommendation: `ecai-public-demo`. Select **Public** only if comfortable that all source files will be visible to anyone. Do **not** use your EC-AI production repository or existing test branch.
2. Upload exactly `streamlit_app.py`, `requirements.txt`, `.gitignore` (and optionally `README.md`). Do NOT upload `.streamlit/secrets.toml`, database URLs, test-app source, or production data.
3. Inspect the repository before deployment; verify it contains only the intended public-demo files.

## Deploy to Streamlit Community Cloud
1. Open https://share.streamlit.io and sign in with GitHub.
2. Click **Create app** > **Yup, I have an app**.
3. Select repository `ecai-public-demo`, branch `main`, entrypoint `streamlit_app.py`.
4. Select Python **3.13** in advanced settings where offered. **Do not provide secrets**.
5. Choose a free subdomain if offered; deploy; capture the exact URL given by Streamlit (do not guess).
6. Verify publicly in a signed-out/incognito window before sending it to anyone.

## Public acceptance checklist
- [ ] Banner and five scenes fit normally at 100% browser zoom.
- [ ] Scenes 2–3 relationship picker works across multiple fictional relationships; missing financial estimates show as not estimated.
- [ ] Scene 4 selection drives Scene 5's proposed actions, including defer = evidence requests only.
- [ ] No authentication / Supabase / DB requests or operational links appear.
- [ ] A new incognito session starts with the default fictional demo; no decisions persist across sessions.
- [ ] All copy correctly states that numbers and relationships are fictional and read-only.

## Important limitation
Self-service tests validate usability, comprehension and interest, not actual wallet models, customer demand or pilot readiness. Streamlit Community Cloud is public if deployed from a public repository. Do not put customer or MUFG information in public demo assets.

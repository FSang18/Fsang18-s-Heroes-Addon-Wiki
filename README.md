# FSang18's Heroes Addon Wiki

This folder is the whole wiki as a website project: 644 pages, ~1,900 images, search, a sidebar menu, a dark/light theme and a "edit this page" button. It was converted automatically from the GitLab wiki.

Every time something changes on GitHub, GitHub rebuilds the website and publishes it for free (GitHub Pages). You never build anything yourself.

---

## Publishing it (one-time setup, about 15 minutes)

**1. Make a GitHub account** (free) at https://github.com if you do not have one.

**2. Install GitHub Desktop** (free) from https://desktop.github.com and sign in with your account.
Do not try to drag these files into the GitHub website; there are too many of them for the browser uploader. GitHub Desktop handles it.

**3. Put this folder on GitHub**
1. Unzip this project somewhere, for example `Documents\heroes-wiki`.
2. In GitHub Desktop: **File -> Add local repository...** -> choose the unzipped folder. It will say it is not a repository yet; click **create a repository** and keep the name `heroes-wiki`.
3. Click **Commit to main** (bottom left), then **Publish repository**. Untick "Keep this code private" (Pages needs a public repo on a free account).

**4. Turn the website on**
1. On github.com open your new repository -> **Settings** -> **Pages** (left menu).
2. Under **Build and deployment -> Source**, choose **GitHub Actions**.
3. Open the **Actions** tab. A run called "Publish wiki" starts by itself (if it does not, click it -> **Run workflow**). Wait 2-4 minutes for the green tick.

**5. Done.** The wiki is at `https://YOUR-GITHUB-NAME.github.io/heroes-wiki/`

If the run turns red, open it, copy the error text and send it to me.

---

## Editing the wiki afterwards (no coding needed)

**Change a page**
Open the page on the published site, click the **pencil icon** at the top right of the page, change the text, then press **Commit changes**. The site updates in about 2 minutes.

**Add a page**
On github.com go to the `docs` folder, open the matching folder (e.g. `docs/items/gadgets`), click **Add file -> Create new file**, and name it like `my-new-gadget.md`. Put this at the top, then write below it:

```
---
title: "My New Gadget"
---

# My New Gadget

Text goes here.
```

The sidebar menu is built automatically from the files and folders, so the page appears by itself. Menu order is alphabetical.

**Add an image**
Upload it into `docs/images/` (create the folder the first time) with **Add file -> Upload files**, then in your page write `![description](../../images/name.png)`. Use one `../` for each folder level the page is inside `docs/` (a page at `docs/items/compound-v.md` uses `../images/name.png`).

**Templates**
Your old GitLab page templates (Suit, Power, Ore, ...) are in the `templates/` folder. They are not shown on the website; copy-paste from them when you write a new page.

---

## Good to know

- **Page addresses changed.** They are lowercase and cleaned up (for example `Falcon-Wings-(Base)` is now `falcon-wings-base`). All 1,502 links *inside* the wiki were rewritten and checked, and so were all 1,084 images. Links to the wiki that live elsewhere (Modrinth, CurseForge, Discord, other people's posts) still point at GitLab and have to be updated by hand.
- **3 links were already dead on the GitLab wiki** (pages that never existed). They are listed in `conversion-report.txt`. The text was kept, the link was removed.
- **Keep one wiki, not two.** Once this is live, edit only here, otherwise the GitLab copy and this one drift apart. Consider putting a "This wiki has moved" note on the GitLab home page.
- **Sharing the work with FSang18.** In the repository: **Settings -> Collaborators -> Add people**.
- **Colours and look** are in `theme-files/stylesheets/extra.css` and `mkdocs.base.yml` (logo, site name, dark/light colours).
- **Keep the pinned versions** in `requirements.txt`. The tool this site is built with (MkDocs) is about to get a major new version that breaks the theme; the pins keep your site building exactly as it does today.

## Folder map

| Path | What it is |
|---|---|
| `docs/` | All the pages (`.md` files) and `uploads/` (all the images) |
| `templates/` | Old GitLab page templates, not published |
| `mkdocs.base.yml` | Site name, logo, colours, features |
| `tools/make_nav.py` | Builds the sidebar from the files (runs automatically) |
| `tools/convert.py` | The one-time GitLab -> MkDocs converter (not needed any more) |
| `.github/workflows/publish.yml` | The robot that builds and publishes the site |
| `conversion-report.txt` | What the conversion could not carry over |

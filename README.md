# To-Do List

A simple Python To-Do List built from scratch for Assignment 2.

Project status: Development in progress.

## Team and feature plan

Group size: 3. Chosen theme: To-Do List.

| Member | GitHub username | Assigned feature |
| --- | --- | --- |
| Soulaymane Alahiane | soulaymanealahiane | A: Add tasks with validated titles and unique IDs |
| Aya Drissi | Aya-Drissi | B: Mark tasks complete and reopen tasks |
| Rim Zemmouri | Rimzemmouri | C: Filter all, pending, and completed tasks; integrate the command-line menu |

Each member uses their own clone, feature branch, at least two meaningful commits, at least two unit tests, and a Pull Request into main.

Review rotation: Aya reviews Soulaymane, Rim reviews Aya, and Soulaymane reviews Rim. Leave a meaningful line comment before approval. At least one PR must complete a Request changes and same-branch correction cycle.

## Run

Use Python 3.12 or later. Once the feature PRs are merged:

```sh
python -m pip install -r requirements.txt
python -m todo
```

Tasks remain in memory during the session.

## Tests

```sh
python -m pytest
```

GitHub Actions runs the full pytest suite on pushes and Pull Requests.

## Project page

https://soulaymanealahiane.github.io/GitLab-Assignment2/

## Structure

```text
todo/                 Python application
tests/                pytest unit tests added on feature branches
.github/workflows/    test workflow added on Soulaymane's feature branch
docs/                 GitHub Pages project page
report/               one final group PDF after the group workflow is complete
```

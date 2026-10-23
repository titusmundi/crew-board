---
name: crew-board-setup
description: Build a new Crew Board for a small trades or project business that already keeps an Obsidian vault worked on by Claude Code. Use when the user asks to set up, create or start a crew board, job board, schedule board or project dashboard for their jobs, or runs this kit for the first time.
---

# Set up a Crew Board

A Crew Board is one private web page (a published Claude artifact) with three tabs: **Schedule**
(a Monday to Friday calendar of tasks per job, plus a weekend column), **Materials** (what must be on
site by when, ticked Ordered and Received) and **Tools** (what goes in the van each day). The owner
edits it directly: drag tasks, add one-offs, tick things off. The page saves itself. The vault keeps
the reasons behind the dates. The board keeps the dates.

The template is `template/crew-board.html` beside this file. Read it fully before using it.

## Before you start
- The user's vault must already exist, with a `Doing/` space and a `Map.md`. If their structure
  differs, adapt the paths below to theirs and say so. Never write in their personal notes space
  (for example `Thinking/`) unless they ask.
- Work in small steps and confirm between them. Do not build the whole board in one silent batch.
- Never invent a date, a price or a name. Missing facts go on the vault's open questions list.

## Step 1: interview (one question at a time, plain English)
1. What is the business, and who works on the jobs? (Their own name or nickname, helpers, trades.)
   Ask how each person should appear on the board.
2. Which jobs are live now? For each: a short label, the client's **first name only** or a nickname,
   the **neighbourhood only** (never a street address on the board), and the scope in a few words.
3. For each job: the tasks in order, who does each, how many working days, and the start date if
   known. If they have a schedule in a vault note, offer to read it instead of asking.
4. Do they have a category for small one-off jobs, or work shared across jobs? (The template has
   `small` and `shared` slots. Drop them if not needed.)
5. Working days: Monday to Friday? Which days are closed (holidays, a Christmas week)? Do they ever
   work weekends, and if so only to catch up? Record the answer in a vault note
   (`Working days and holidays.md`, from `template/`).
6. Materials and tools: which items must be on site by a date, per job? Only the critical ones.

## Step 2: build
1. Copy the template to the vault's tools folder (suggest `Tools/crew-board.html` beside the vault,
   not inside it).
2. Edit only the data block `<script id="seed" type="application/json">`:
   - `owner`: the name the owner uses for themself on tasks. `people` is everyone who appears.
   - `projects`: one entry per job. Ids `job1` to `job4` already have colours. `small` and
     `shared` are optional.
   - `holidays`: `{"YYYY-MM-DD": "Label"}` for every **closed** day only. Check each date's weekday.
   - `tasks`: `{id, p, t, who, dur, d: [dates], done, note}`. `d` lists every working day the task
     occupies. A half day is `"dur":"0.5 day"` with one date.
   - `materials.<id>` and `tools.<id>`: arrays, one per project id, even if empty.
   - `updated`: the current time in ISO format.
3. **More than four jobs, or new colours:** add `--<id>`, `--<id>-bg` and `--<id>-ink` tokens in
   **all three** theme blocks of the style (light, the dark media query, and `[data-theme="dark"]`).
4. Optionally rename the page title ("Crew Board") in the two places it appears.
5. Keep exactly the three blocks the template has: one `<style id="css">`, one `<script id="seed" type="application/json">`
   (the data) and one `<script id="app">` (the code). Keep their ids. The page saves itself by rebuilding
   a copy of itself from those three, so adding a block, renaming an id, or putting a literal closing
   script tag inside the script breaks saving.

## Step 3: publish and record
1. Publish the file as a private Artifact (icon: `calendar`). The page asks for the `artifact`
   capability so it can save itself.
2. Open it, tick something, wait for "Saved to board", reload, and check the tick survived. **Do not
   call setup done until a save has round-tripped.** Say so if you could not test it.
3. Create the vault note `Doing/03 - Knowledge Base/Crew Board.md` from `template/Crew Board.md`:
   the link, what is on it, what the owner can do alone, what still needs Claude, how saving works,
   the rules, Decisions (dated), Gotchas. Link it from `Map.md`.
4. Tell the owner the three ways back to the board: the link, a browser bookmark, and `/board`.

## Step 4: hand over
Show the owner, on the board itself: drag a task (press and hold on a phone), open a day, add a
task, mark done, undo, tick a material. Then explain the one rule they must know: **the board is the
record for dates, so ask Claude for anything structural** (a new job, a new colour, a chain of moves,
holidays).

## What makes it last
The board stays useful because the vault keeps up with it. Follow the vault's update rule: every
decision about the board goes, dated, in the Decisions section of `Crew Board.md`. Every surprise goes in
Gotchas, and every idea not acted on goes in a Parking lot. See the `crew-board-update` skill for changes.

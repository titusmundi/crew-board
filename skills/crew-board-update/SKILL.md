---
name: crew-board-update
description: Change an existing Crew Board safely, such as adding a job, moving a chain of tasks, realigning material dates, changing holidays, ticking off a finished job, or reading back what the owner has changed. Use whenever the user asks for any change to their Crew Board, or asks what the board currently says.
---

# Change a Crew Board without losing the owner's edits

The owner edits the live board directly, and the board saves itself by republishing. So **the
published page is the record**, not any local file. Every change follows the same loop.

## The loop (never skip a step)
1. **Read the live board** (Artifact `read` on the board's link, from the vault note
   `Crew Board.md`). Read every line of the saved file before republishing.
2. **Check freshness.** Compare the seed's `updated` time with the last change you know of. If tasks
   the owner says are finished still show as open, the board has not been saved in a while: ask
   before assuming anything.
3. **Apply only the change asked for**, to the data in `<script id="seed">` of that live copy. Do not
   tidy, re-sort or "fix" anything else.
4. **Verify the change** with a quick diff: only the intended lines differ, other jobs are untouched.
5. Set `updated` to now, then **republish to the same link** (Artifact publish with `url`).
6. Copy the published file over the local master (for example `Tools/crew-board.html`), so the
   backup matches the board.
7. **Write it down** in `Crew Board.md`: a dated Decision if it changes how the board works, a Gotcha
   if something surprised you, and any knock-on note (for example "material dates not realigned").

## Common changes
- **New job:** a project entry, its colour tokens in all three theme blocks, and empty `materials`
  and `tools` arrays for its id.
- **A chain of moves:** tasks carry no dependencies, so moving one never moves others. When asked to
  push a chain, list the tasks you will move and their new dates, and confirm before writing.
- **Material and tool dates:** they do not follow dragged tasks. Realign them only when asked, and
  show the list first.
- **Holidays:** only closed days go in `holidays`. Check every date's weekday. Keep the vault's
  working-days note in step.
- **A finished job:** mark its tasks done and its materials ordered and received, after the owner
  confirms the job is finished. Leave other jobs exactly as they were.

## Rules learned the hard way
- Never republish from an older local copy: the owner's moves and ticks since then are lost.
- Keep the three blocks (`css`, `seed`, `app`) and their ids exactly. Never add a block, and never put a literal closing script tag inside the script.
- Every save reloads the page. If two devices edit at once, the later save wins.
- A save method that "seems to work" must be proven: tick, save, reload on another device.
- No street addresses, full client names or prices on the board.

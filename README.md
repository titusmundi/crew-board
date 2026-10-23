# Crew Board

A Claude Code plugin that builds and maintains a **Crew Board**: one private live page with your jobs'
schedule, materials and tools, which you edit yourself and which saves itself. It is made for small
trades and project businesses.

**This is an optional add-on.** It is a separate kit from the [Second Brain starter](https://github.com/titusmundi/second-brain-starter)
and does not change it. You can use the board with any Obsidian vault that Claude Code works in, as long as the vault has a
working space for Claude (a `Doing/` folder with a `Map.md`) and a `CLAUDE.md` one level above it. The Second Brain starter is one
easy way to get that, but it is not required.

Start with `docs/Crew Board guide.pdf`: how one renovation business built its board, the rules that made it
reliable, and how to build yours.

## Before you start
- An Obsidian vault that Claude Code works in (see above), with Claude opened at the folder above the vault.
- Claude Code with a paid Claude plan (Pro, Max, Team or Enterprise). The free claude.ai plan does not include Claude Code.
- The ability to publish a **private Claude artifact** from Claude Code. The board is published this way so it can save itself.
  The setup skill tests this before it says it is done.
- Obsidian is free. The kit adds no other cost.

## Install
In a terminal, with the Claude Code command-line tool installed:

```bash
claude plugin marketplace add titusmundi/crew-board
claude plugin install crew-board@crew-board
```

Restart Claude Code if it asks. Prefer to keep the files yourself? Download or clone this repository, then run
`claude plugin marketplace add <path to the folder>` and the same second command. Install steps change, so check
[the Claude Code plugin docs](https://code.claude.com/docs/en/plugins) if anything here does not match what you see.

## Use
- **"Set up my Crew Board"**: runs the `crew-board-setup` skill (interview, build, publish, test, vault notes).
- **Any change** ("add a job", "push the tiling back a week", "tick off the Smith job"): the `crew-board-update` skill reads the
  live board first, changes only what you asked, and logs it.
- **`/board`**: prints your board's link.

## What is inside
| Path | What it is |
| --- | --- |
| `skills/crew-board-setup/` | Setup skill, the board template (`template/crew-board.html`, sample data) and vault note templates |
| `skills/crew-board-update/` | The safe change loop |
| `commands/board.md` | `/board` |
| `docs/` | The guide, as PDF and HTML |

## Privacy
The board is a private Claude artifact: only you can open it unless you share it from its own menu. Keep street addresses, full
client names and prices off the board. The board lives in your Claude account, so keep the local master copy the setup skill
makes (`Tools/crew-board.html`) as your backup.

## Not affiliated
This is an independent project by Titus Mundi LLC. Claude and Obsidian are products of their respective owners, and this kit is
not affiliated with or endorsed by Anthropic or Obsidian.

## License
MIT. See [LICENSE](LICENSE).

Version 0.1.0, October 2026. By JC Titus, Titus Mundi LLC ([titusmundi.com](https://titusmundi.com)), with Claude.

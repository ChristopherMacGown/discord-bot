# discord_bot

## Getting Started

This repository is managed by [poetry](https://python-poetry.org/docs/#installation). You will need 
poetry installed, instructions are linked above. After having installed poetry, you can simply run:

```
discord-bot $ poetry env use python3.11 
discord-bot $ poetry install
discord-bot $ poetry run discord [TOKEN]
```

If you have the virtualenv activated, you don't need the poetry invocation. You can call the CLI
directly with:

```
discord-bot $ discord --help
discord-bot $ discord [TOKEN]
```
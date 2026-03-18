---
title: "Rules and Memory"
description: Create rule files and memory to customise AI agent behaviour across sessions.
---

# Creating Rules and Memory

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~10 min</span>
</div>

Your AI coding agent can use markdown files to save information between sessions. You can also supply your own files to provide rules and guidance to customise its behaviour.

---

## Making a Rule File

The file name needs to be one of: `AGENTS.md`, `CONTRIBUTING.md`, `README.md`, `DEVELOPER.md`, `STYLEGUIDE.md`

Best practice is to make a `.md` file containing your desired rules. Save the file in your project folder.

Here is text to start with. Copy and paste it into an `AGENTS.md` file:

```markdown
1. First, think through the problem. Read the codebase and write a plan in tasks/todo
2. The plan should be a checklist of todo items.
3. Check in with me before starting work — I'll verify the plan.
4. Then, complete the todos one by one, marking them off as you go.
5. At every step, give me a high-level explanation of what you changed.
6. Keep every change simple and minimal. Avoid big rewrites.
7. At the end, add a review section in todo.md summarizing the changes.
8. Make a memory file and todo file to store information during the session
```

Choose one way to create the file:

1. Open RStudio > `File` > `New File` > `Markdown File` > paste text and save as `AGENTS.md`
2. Open a text editor (Notepad, TextEdit, VS Code) > paste text and save as `AGENTS.md`
3. In Terminal, create a file in your project directory: `touch path/to/folder/AGENTS.md`

!!! tip "Alternative name"
    You can also name the rules file `copilot-instructions.md` for GitHub Copilot compatibility.

## Start Using Your Rules

Let your model know the file exists by running `/init` in `Build` mode.

Now the program will use `AGENTS.md` as a living document that should be updated manually. It will make a `memory.md` and `todo.md` which it will update. These provide information for the project between sessions.

---
title: "Penguins Analysis"
description: Data analysis with AI assistants — explore a real dataset and produce publication-ready plots.
---

# Data Analysis with AI: From Dataset to Publication Figures

<div class="tutorial-card__header">
  <span class="difficulty-badge difficulty-badge--beginner">Beginner</span>
  <span class="time-estimate">~30 min</span>
</div>

This tutorial walks you through using an AI coding agent to analyse the Palmer Penguins dataset and create visualisations.

---

## What You'll Learn

- How to use `Plan` mode to guide AI interactions
- How to prompt for data analysis tasks
- How to get AI to create figures and export them

## Steps

1. Download the [Palmer Penguins dataset](https://allisonhorst.github.io/palmerpenguins/) to your folder. You can download the CSV directly from [here](https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv).

2. Switch to `Plan` mode. This is a mode that won't start to make things. It will ask you questions to help guide your progress.

3. Use this prompt:

    ```
    Make me some figures of the Palmer Penguins dataset attached.
    Output the figure in an Excel file.
    ```

4. Interact with the `Plan`. For this example I replied that I want scatter plots comparing body measurements across penguin species. This is where you can influence what the model does. This is the major advantage over other chatbots.

5. Change from `Plan` mode to `Build` mode and begin planned tasks by prompting it to begin (i.e. "yes").

6. If it gets stuck with an error, prompt `complete analysis` and it will continue working until the end.

## Results

The Palmer Penguins dataset contains measurements for three penguin species (Adelie, Chinstrap, and Gentoo) from islands in the Palmer Archipelago, Antarctica. It includes features like bill length, bill depth, flipper length, and body mass.

## Tips

- Be specific in your prompts about what you want (e.g., "scatter plots", "histograms", "correlation matrix")
- The `Plan` mode lets you refine the approach before the AI starts working
- You can always interrupt and redirect if it's going in the wrong direction
- Try asking for species comparisons or island-based groupings for interesting visualisations

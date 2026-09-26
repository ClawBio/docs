# Build one useful, verifiable skill

A hands-on hackathon opening using **rnaseq-de**. Inspect a real skill folder, run its bundled toy example, check the evidence and scope your own contribution. Allow about **60 minutes**, with a prepared Python environment.

[Open the presentation](/presentations/rnaseq-de-workshop/){ .md-button .md-button--primary }
[Jump to the worksheet](#team-scoping-worksheet){ .md-button }

## What you will learn

- Explain a skill through its inputs, method, outputs and checks.
- Trace a result back to an explicit comparison and backend.
- Recognise a tested input failure and the limits of a successful run.
- Define one useful contribution before choosing a team or writing code.

## Prepare the example

Use a separate checkout for the workshop. The rehearsal used ClawBio commit `0ba950565ee6a0fe9da3bde2164f6c814bd57dc9` and PyDESeq2 0.5.4. See [setup](setup.md) if you need Git, Python or an agent. Prepare dependencies before the session; package installation is not the opening exercise.

```sh
git clone https://github.com/ClawBio/ClawBio.git ClawBio-workshop
cd ClawBio-workshop
git checkout 0ba950565ee6a0fe9da3bde2164f6c814bd57dc9
```

Use an environment containing the dependencies described in the pinned [skill instructions](https://github.com/ClawBio/ClawBio/blob/0ba950565ee6a0fe9da3bde2164f6c814bd57dc9/skills/rnaseq-de/SKILL.md), including PyDESeq2. Confirm `python -c "import pydeseq2; print(pydeseq2.__version__)"` before starting. A prepared environment and the commands below were rehearsed; a fresh participant installation still needs its own check.

## 1. Open the folder before asking the agent

Inspect [SKILL.md](https://github.com/ClawBio/ClawBio/blob/0ba950565ee6a0fe9da3bde2164f6c814bd57dc9/skills/rnaseq-de/SKILL.md), the Python executable and the two example files. These are **toy data: ten genes and six samples**, not disease or treatment evidence.

| Contract | Inspect |
| --- | --- |
| Counts | `skills/rnaseq-de/examples/demo_counts.csv`: genes in rows, samples in columns |
| Metadata | `skills/rnaseq-de/examples/demo_metadata.csv`: matching sample identifiers, condition and batch |
| Design | `~ batch + condition` |
| Contrast | `condition,treated,control`: positive log2 fold change means higher in treated |
| Method | Explicit PyDESeq2 backend |
| Output | `tables/de_results.csv`, `result.json`, report, figures and reproducibility files |

Count tables are the starting point. Raw-read alignment and counting are upstream work. The agent can help select commands and explain artifacts; people must still judge experimental design, confounding and interpretation.

## 2. Run the bundled example

From the checkout root, using your prepared environment:

```sh
MPLBACKEND=Agg python skills/rnaseq-de/rnaseq_de.py \
  --demo \
  --backend pydeseq2 \
  --output /tmp/clawbio-workshop-rnaseq
```

Choose a fresh output directory for each run. The demo sets the design and contrast above. For other data, specify the counts, metadata, formula and contrast explicitly.

## 3. Read the table before the plot

1. Match all six sample identifiers across the two inputs. Inspect conditions and batches.
2. Confirm `backend_used` is `pydeseq2` in `result.json`.
3. Open `tables/de_results.csv`. In this fixture, GeneA has larger treated counts and a positive log2 fold change; GeneB has smaller treated counts and a negative change. These are directional sanity checks.
4. Check that the ten expected gene identifiers are present. Filtering on other datasets may legitimately change the count and needs inspection.
5. Inspect PCA, volcano and MA plots in light of the design and table.
6. Inspect `reproducibility/commands.sh`, `environment.yml` and `checksums.sha256`.

The rehearsal reported shrinkage applied and verified nine hashes in the separate checksum manifest. The top-level `input_checksum` and `datasets` fields in `result.json` were empty. A field's presence does not establish usable provenance.

!!! warning "Execution is only one check"
    The tiny fixture produced low residual degrees of freedom and numerical warnings. Successful execution, expected directions and file hashes do not establish general statistical validity or biological meaning. Do not present its tiny p-values as scientific findings.

## 4. Test a boundary that should stop execution

Make a copy of the metadata with its final sample row removed. Keep the original unchanged. Pass the incomplete copy to the skill:

```sh
MPLBACKEND=Agg python skills/rnaseq-de/rnaseq_de.py \
  --counts skills/rnaseq-de/examples/demo_counts.csv \
  --metadata /tmp/metadata_missing_sample.csv \
  --formula '~ batch + condition' \
  --contrast condition,treated,control \
  --backend pydeseq2 \
  --output /tmp/clawbio-workshop-invalid
```

The rehearsed check stopped with **`Metadata missing samples`**. Restore the correct metadata or stop; do not invent the missing sample's label. This checks one failure condition, not every possible invalid input.

## 5. Optional: connect a second skill

```sh
MPLBACKEND=Agg python skills/diff-visualizer/diff_visualizer.py \
  --input /tmp/clawbio-workshop-rnaseq \
  --output /tmp/clawbio-workshop-plots
```

The hand-off is concrete: `diff-visualizer` accepts the directory containing `tables/de_results.csv`, with `gene`, `log2FoldChange` and `padj` or `pvalue`. It changes presentation, not the underlying differential-expression inference. The rehearsal completed; the plotting library also emitted a layout warning. Matching file extensions alone do not prove compatible units, identifiers or meaning.

## Team scoping worksheet

Complete individually, then exchange with a partner. Browse the [skill library](../skills/index.md) and inspect existing code and tests before proposing new work. Your contribution might be an adapter, regression test, documentation improvement or reproducible bug report.

| Prompt | Your answer |
| --- | --- |
| Who needs this and what specific problem do they have? | |
| Smallest useful transformation | |
| Exact input: file type, fields, identifiers, units and available sample | |
| Exact output: file type, fields and example | |
| Existing skill or tool to reuse, with repository path | |
| Gap that remains after checking existing implementations | |
| Method or tool performing the work | |
| Decisions that remain with the agent or human | |
| Known-answer or independently checkable example | |
| Invalid input to reject or clearly flag | |
| Evidence to deliver: command, parameters, environment and source data | |
| Work explicitly outside today's scope | |
| Build owner and separate reviewer | |
| First runnable checkpoint | |

Finish this sentence:

> Given [one defined input], our contribution produces [one useful output]. We know it worked when [observable check]. It does not attempt [excluded work].

Your partner must be able to explain the input, output and success check without inventing missing details. If they cannot, narrow the scope. At the final demo, show the input, result, check and one limitation. A reproducible failure can be a useful contribution.

[Continue to Build a Skill](build-a-skill.md){ .md-button .md-button--primary }

## Sources and scope

This workshop is grounded in the literal [rnaseq-de implementation](https://github.com/ClawBio/ClawBio/tree/0ba950565ee6a0fe9da3bde2164f6c814bd57dc9/skills/rnaseq-de) and [diff-visualizer implementation](https://github.com/ClawBio/ClawBio/tree/0ba950565ee6a0fe9da3bde2164f6c814bd57dc9/skills/diff-visualizer), plus a local rehearsal on 26 September 2026. It teaches inspectable execution and contribution design. No real-data validation or biological discovery is claimed.

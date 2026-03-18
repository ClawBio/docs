# Setup (~10 minutes)

## 1. Clone the Repository

```bash
git clone https://github.com/ClawBio/ClawBio.git
cd ClawBio
```

## 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Core dependencies: `pandas`, `numpy`, `matplotlib`, `seaborn`.

Optional (for specific skills):

```bash
pip install scanpy          # scRNA-seq skills
pip install reportlab       # PDF report generation
pip install pydeseq2        # RNA-seq differential expression
pip install bioblend        # Galaxy Bridge
```

## 4. Run a Demo

Verify everything works by running a built-in demo:

```bash
# Pharmacogenomics demo
python skills/pharmgx-reporter/pharmgx_reporter.py \
  --input skills/pharmgx-reporter/demo_patient.txt \
  --output /tmp/pharmgx_demo

# Check the output
cat /tmp/pharmgx_demo/report.md
```

You should see a pharmacogenomics report with drug recommendations. If this works, your environment is ready.

## Troubleshooting

### `ModuleNotFoundError: No module named 'pandas'`
You forgot to activate the virtual environment or install dependencies. Run `pip install -r requirements.txt`.

### `Permission denied` on output directory
Create the output directory first: `mkdir -p /tmp/my_output`.

### macOS: `xcrun: error: invalid active developer path`
Install Xcode command line tools: `xcode-select --install`.

---

Ready? Move on to [Your First Skill](first-skill.md).

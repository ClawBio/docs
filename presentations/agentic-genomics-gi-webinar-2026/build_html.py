#!/usr/bin/env python3
"""Rebuild index.html as the expanded 15-slide v1 deck.

Reuses the existing <head>/CSS, the JS footer, and the three inline SVG
diagrams (two-waves, counterintuitive branch, ancestry bar chart) from the
current index.html, and rewrites the slide body to match the v1 PPTX.
Run from this directory:  /opt/homebrew/bin/python3 build_html.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "index.html")
text = open(SRC).read()

head = text[:text.index("</head>") + len("</head>")]
footer = text[text.index('<div class="progress"'):]


def extract_svg(marker):
    i = text.index(marker)
    s = text.rindex("<svg", 0, i)
    e = text.index("</svg>", i) + len("</svg>")
    return text[s:e]

WAVES = extract_svg('viewBox="0 0 1000 130"')
COUNTER = extract_svg("max-width: 1080px")
ANCESTRY = extract_svg("max-width: 1040px")

BODY = r"""
<!-- 1. TITLE -->
<section class="slide title-slide active">
    <img src="figures/clawbio-logo-white.png" alt="ClawBio logo" style="width:clamp(80px,9vw,128px); height:auto; margin-bottom:1.1rem;">
    <div class="section-label">ClawBio &times; Genomic Intelligence</div>
    <h1>Agentic Genomics<br>in <span class="green">Practice</span></h1>
    <div class="subtitle">AI agents now do real genomics work end to end. The hard part is no longer writing the code; it is trusting the result.</div>
    <div class="author">Manuel Corpas</div>
    <div class="meta">
        Senior Lecturer in Genomics, AI &amp; Data Science &middot; University of Westminster<br>
        Founder, ClawBio<br>
        Webinar &middot; ClawBio &times; Genomic Intelligence &middot; 24 June 2026
    </div>
    <div class="notes">[0:30] Welcome. Thank you for joining ClawBio and Genomic Intelligence. I run the first 20 minutes, the framing. Then Benjamin and the GI team take over with the live work. One line to hold onto for the whole talk: agents can now write and run the analysis. The open question is whether you can trust what they ran. Everything I show is built around that single problem.</div>
</section>

<!-- 2. TODAY -->
<section class="slide">
    <div class="section-label">Today</div>
    <h2>The shape of the next 90 minutes</h2>
    <div class="agenda">
        <div class="row"><div class="who">Manuel &middot; ClawBio</div><div class="what">The framing: what changed, why trust is the bottleneck, and the evidence.</div></div>
        <div class="row"><div class="who gi">Benjamin &middot; GI</div><div class="what">What the Genomic Intelligence models are and where they fit in a workflow.</div></div>
        <div class="row"><div class="who gi">Benjamin &middot; GI</div><div class="what">Live: GI skills running inside ClawBio on real, openly published genomes.</div></div>
        <div class="row"><div class="who">Everyone</div><div class="what">Q&amp;A, and an open call: build your own use case on the platform in two weeks.</div></div>
    </div>
    <p class="gap center small" style="margin-top:1.4rem;">For bioinformaticians, computational biologists, genomics researchers, and anyone building with AI agents in the life sciences.</p>
    <div class="notes">[0:40] Quick orientation. I take the first 20 minutes to set up the problem and show you the evidence. Then Benjamin and GI show you the models and run live scenarios inside ClawBio. We close with Q&amp;A and an open call: build something on the platform over the next fortnight and show us. Move fast here; the audience just needs to know where the handoff is.</div>
</section>

<!-- 3. THE SHIFT -->
<section class="slide">
    <div class="section-label">The shift</div>
    <h2>From retrieval to <span class="green">autonomous execution</span></h2>
    __WAVES__
    <div class="two-col content">
        <div>
            <h3 style="text-align:left; color:#adbac7;">First wave: information retrieval</h3>
            <ul>
                <li>Summarising papers, answering pathway questions, extracting structured data.</li>
                <li><span class="muted">Useful, but incremental.</span></li>
            </ul>
        </div>
        <div>
            <h3 style="text-align:left; color:#56d364;">Second wave: autonomous execution</h3>
            <ul>
                <li>Agents <span class="green">write, debug and run code</span>; connect to files, databases and tools.</li>
                <li>They plan multi-step analyses and adapt on intermediate results.</li>
            </ul>
        </div>
    </div>
    <p class="gap center small" style="max-width:88%; margin-top:1.4rem;">The researcher's role moves: <span class="accent">producer &rarr; evaluator</span>. Dozens of independently built systems have made the same move, from isolated prompts to multi-tool pipelines with runtime decision-making.</p>
    <div class="notes">[1:30] Two waves. The first wave of LLMs in biology was retrieval: summarise this paper, answer a pathway question, pull structured data out of text. Genuinely useful, but incremental; it did not change what we could do, only how fast we read. The second wave is different in kind. Modern models write, debug and execute code, and when you connect them to a file system, databases and command-line tools, they plan multi-step analyses and adapt as intermediate results come back. The consequence: your job shifts from producing the analysis to judging it. Recent reviews catalogue dozens of these systems across genomics, single-cell, proteomics. This is a field-wide move, not one lab's claim.</div>
</section>

<!-- 4. DEFINITION -->
<section class="slide">
    <div class="section-label">Definition</div>
    <h2>Defining <span class="green">agentic genomics</span></h2>
    <p class="center" style="max-width:86%; font-size:clamp(1rem,1.6vw,1.35rem);">An agent that plans and executes a genomic analysis end to end: it reads the data, chooses the tools, runs them, inspects intermediate results, and revises its own plan, with a human evaluating rather than typing every command.</p>
    <div class="principle-grid" style="max-width:1000px; margin-top:1.4rem;">
        <div class="principle"><h4>Autonomy</h4><p>Decides at runtime, not a fixed script.</p></div>
        <div class="principle" style="border-left-color:#56d364;"><h4 style="color:#56d364;">Domain-constrained</h4><p>Works through validated skills, not ad-hoc code.</p></div>
        <div class="principle" style="border-left-color:#e3b341;"><h4 style="color:#e3b341;">Self-correcting</h4><p>Diagnoses errors and re-plans.</p></div>
        <div class="principle" style="border-left-color:#d2a8ff;"><h4 style="color:#d2a8ff;">Natural language</h4><p>Directed in plain English, not code.</p></div>
    </div>
    <p class="gap center" style="max-width:88%; margin-top:1.2rem; font-size:clamp(0.95rem,1.5vw,1.2rem);"><span class="highlight">The test: perturb an intermediate result. A genuine agent changes its strategy; a fixed pipeline does not.</span></p>
    <p class="center small" style="max-width:90%; margin-top:0.9rem;">Grounded in Corpas, Fatumo &amp; Guio, <em>Agentic Genomics</em> (Cell Genomics, in review). Worked example: a trio exome, BWA-MEM2 flags a bad index, the agent rebuilds it and resumes, unprompted.</p>
    <div class="notes">[1:30] Here is the working definition, and it has teeth. Four conditions, jointly necessary: the agent decides at runtime; it works through a constrained library of validated skills, not code invented on the spot; it diagnoses its own errors and re-plans; and it is directed in natural language. If a system only satisfies some of these, it is something else: workflow automation, AutoML, or a chatbot writing scripts. The clean discriminator is the perturbation test: change an intermediate result and watch. A real agent re-plans; a fixed DAG carries on regardless. Concrete instance from a trio exome in our paper: BWA-MEM2 throws an incompatible-index error mid-run, and the agent diagnoses it, rebuilds the index and resumes, no human in the loop. That self-repair is the property, not the speed.</div>
</section>

<!-- 5. THE THESIS -->
<section class="slide">
    <div class="section-label">The thesis</div>
    <h2 style="font-size:clamp(2rem,4.2vw,3.4rem); max-width:90%;">From producing analyses<br>to <span class="green">validating</span> them.</h2>
    <p class="gap center" style="max-width:78%; margin-top:1.4rem; font-size:clamp(1.05rem,1.8vw,1.5rem); color:#adbac7;">The bottleneck moves. Generating the analysis is no longer the hard part; <span class="green">knowing you can trust it</span> is.</p>
    <div class="notes">[0:40] If I had to compress the whole Perspective into one sentence, it is this. The hard, rate-limiting step used to be building the pipeline. Agents have largely dissolved that. What they have not dissolved, what they actually make harder, is knowing the result is correct. The rest of the talk is about that gap: how it fails, what it costs, and what we do about it. Pause here.</div>
</section>

<!-- 6. THE NEW BOTTLENECK -->
<section class="slide">
    <div class="section-label">The new bottleneck</div>
    <h2>Failure is <span class="red">silent, plausible, and consequential</span></h2>
    <div class="three-col gap" style="margin-top:1rem;">
        <div class="card"><h3 class="red">Plausible</h3><p>Formatted correctly, reads fluently: exactly what a reviewer expects to see.</p></div>
        <div class="card"><h3 class="orange">Confident</h3><p>States a wrong answer in the same tone as a right one. No flag, no uncertainty.</p></div>
        <div class="card"><h3 class="accent">Consequential</h3><p>The failure is a missed cancer gene or a wrong dose, not a 404. And it scales.</p></div>
    </div>
    <div style="width:90%; max-width:1050px; margin-top:1.5rem; background:rgba(255,161,152,0.08); border-left:4px solid #ffa198; border-radius:8px; padding:1.0em 1.3em; text-align:left;">
        <div style="display:inline-block; background:#ffa198; color:#0d1117; font-size:0.72rem; font-weight:800; letter-spacing:0.05em; padding:0.15em 0.6em; border-radius:12px; margin-bottom:0.5rem;">ILLUSTRATIVE</div>
        <p style="font-size:clamp(0.95rem,1.5vw,1.2rem); line-height:1.55;">A healthy 32-year-old's exome is screened. The agent calls a pathogenic <span class="red">BRCA1</span> frameshift <span class="muted">"likely benign"</span>, with a clean report, a citation, and <span class="red">no flag</span>. She is never offered screening. The first sign is <span class="red">stage IV cancer</span>. Nothing crashed.</p>
    </div>
    <p class="gap center" style="max-width:88%; margin-top:1.1rem; font-size:clamp(0.95rem,1.5vw,1.2rem);">A confident, plausible, wrong answer is worse than no answer. <span class="green">Safe uncertainty beats confident hallucination.</span></p>
    <div class="notes">[1:40] Why is validation the hard part? Because of how agents fail. The output is plausible: well formatted, fluent, exactly what you expected. It is confident: a wrong answer in the same tone as a right one, no hedge, no flag. And in our domain it is consequential: not a broken web page, a missed cancer gene or a wrong drug dose. The box is labelled illustrative, deliberately: a constructed scenario, not a case I observed. A BRCA1 frameshift quietly downgraded to likely benign: clean report, real-looking citation, no flag, no screening offered. Nothing crashes. Now imagine that across ten thousand genomes overnight. The next slide is not illustrative. It actually happened.</div>
</section>

<!-- 7. NOT HYPOTHETICAL -->
<section class="slide">
    <div class="section-label">Not hypothetical</div>
    <h2>A real silent failure, <span class="green">caught and fixed in public</span></h2>
    <div class="three-col gap" style="margin-top:1rem;">
        <div class="card"><h3 class="red">The bug</h3><p>An empty input file, no genomic data at all, was fed to a ClawBio pharmacogenomic skill.</p><p style="margin-top:0.6em;">It returned a clean "all normal" report, with recommended doses for <span class="red">51 drugs</span>. No error. No flag.</p></div>
        <div class="card"><h3 class="orange">The audit</h3><p>In the first weeks of release, a computational biologist stress-tested the library in the open.</p><p style="margin-top:0.6em;">The silent failure was found, reported, and <span class="orange">disclosed publicly</span>, not quietly patched.</p></div>
        <div class="card"><h3 class="green">The fix</h3><p>Empty, malformed and content-free inputs now halt with an explicit error and a non-zero exit.</p><p style="margin-top:0.6em;">A silent degradation became a <span class="green">loud, diagnosable failure</span> (re-tested 2 Jun 2026).</p></div>
    </div>
    <p class="gap center" style="max-width:90%; margin-top:1.4rem; font-size:clamp(0.95rem,1.5vw,1.2rem);">This is the governance layer of validation: <span class="accent">open audit &rarr; public disclosure &rarr; a fix that fails loudly</span>. The pattern is the point, not the skill.</p>
    <div class="notes">[1:40] This one is real and documented in the paper. A ClawBio pharmacogenomic skill was handed an empty file, literally no genomic data. Instead of refusing, it returned a tidy, all-normal report, including dosing for fifty-one drugs. No crash, no warning. That is the silent-failure mode in the flesh. What matters is what happened next: a computational biologist stress-testing the library in the open found it and disclosed it publicly, not a quiet patch. The fix: empty, malformed and content-free inputs now halt with an explicit format error and a non-zero exit. We re-ran the perturbation on the current release in June; it fails loudly every time. The lesson is not about one skill; it is that the governance loop, open audit and a loud fix, is a first-class part of validation. Closed development would have hidden this. Open development caught it.</div>
</section>

<!-- 8. CLAWBIO -->
<section class="slide">
    <h2 style="font-size: clamp(2.2rem, 5vw, 4.2rem); font-weight: 800; margin-bottom: 0.3rem;">Claw<span class="green">Bio</span></h2>
    <p style="font-size: clamp(0.95rem, 1.5vw, 1.25rem); color: #adbac7; max-width: 84%; text-align:center; margin-bottom: 1.1rem;">An open, agent-native skill library for bioinformatics  &middot;  <span class="muted">open-source &middot; local-first &middot; reproducible</span></p>
    <div class="stat-grid" style="width:84%; max-width:1000px;">
        <div class="stat"><div class="num">90</div><div class="label">open skills</div></div>
        <div class="stat"><div class="num">48</div><div class="label">contributors</div></div>
        <div class="stat"><div class="num" style="color:#6e7681;">218</div><div class="label">forks</div></div>
        <div class="stat"><div class="num" style="color:#6e7681;">~1k</div><div class="label">GitHub stars</div></div>
    </div>
    <p class="center" style="max-width:90%; margin-top:1.0rem; font-size:clamp(0.9rem,1.4vw,1.15rem);"><span class="highlight">The adoption signal that matters: within weeks, wet-lab biologists with little coding experience were contributing tested, working skills, using the LLM as the programming intermediary.</span></p>
    <div class="three-col" style="width:84%; max-width:1000px; margin-top:1.1rem;">
        <div class="card"><h3 class="accent">A skill is a contract</h3><p>A plain-text <code>SKILL.md</code> plus code: what it does, what it needs, the steps the agent must follow.</p></div>
        <div class="card"><h3 class="accent">The connecting layer</h3><p>Links agents to genomic databases, clinical knowledge and validation workflows.</p></div>
        <div class="card"><h3 class="accent">Open and auditable</h3><p>Anyone can write, audit and reuse skills. The aim is a trust layer for agentic genomics.</p></div>
    </div>
    <p class="center small" style="max-width:92%; margin-top:1.0rem;"><code style="background:none; padding:0; color:#56d364;">github.com/ClawBio/ClawBio</code> &middot; models, including Genomic Intelligence's, plug in as skills; what is auditable is the SKILL.md contract and the execution trace.</p>
    <div class="notes">[1:30] So what is ClawBio? An open, agent-native skill library for bioinformatics: open-source, local-first, reproducible. I will show numbers but be honest about which mean anything. Stars and forks are attention, not use; they are in grey for a reason. The signal I care about is the middle line: within weeks of release, wet-lab biologists with little coding experience were contributing tested, working skills, using the model as their programming intermediary. Domain experts encoding knowledge directly, which is the whole point. The mechanism is the bottom three: a skill is a contract, a plain-text SKILL.md plus code stating what it does, needs, and the steps to follow; it is the connecting layer; it is auditable. On openness, and this matters before Benjamin speaks: GI's models plug in as skills inside this library. What is open and auditable is the contract and the execution trace; the trust story lives there, around whatever model sits in the middle.</div>
</section>

<!-- 9. THE EVIDENCE -->
<section class="slide">
    <div class="section-label">The evidence</div>
    <h2>Can a plain-text skill reach <span class="green">reliable execution</span>?</h2>
    <p class="center" style="max-width:86%;">Pharmacogenomics, the one corner with clean ground truth (CPIC). <span class="green">44,550 scored evaluations</span> across frontier models, three conditions.</p>
    <div style="display:flex; align-items:center; justify-content:center; gap:1.4vw; width:90%; max-width:1000px; margin-top:1.6rem;">
        <div class="stat" style="flex:1;"><div class="num" style="color:#ffa198;">80.6%</div><div class="label">Free prompt<br><span class="muted">no specification</span></div></div>
        <div style="color:#6e7681; font-size:clamp(1.2rem,2vw,1.8rem);">&rarr;</div>
        <div class="stat" style="flex:1;"><div class="num" style="color:#e3b341;">95.5%</div><div class="label">Skill reasoning<br><span class="muted">guideline loaded</span></div></div>
        <div style="color:#6e7681; font-size:clamp(1.2rem,2vw,1.8rem);">&rarr;</div>
        <div class="stat" style="flex:1;"><div class="num" style="color:#56d364;">100%</div><div class="label">Skill execution<br><span class="muted">deterministic, by construction</span></div></div>
    </div>
    <p class="gap center" style="max-width:88%; margin-top:1.8rem; font-size:clamp(1rem,1.6vw,1.3rem);"><span class="green">100% is not the model getting smarter</span>; it is the model removed from the answer. Correctness is constrained by architecture, not by a better prompt.</p>
    <div class="notes">[1:50] Does a plain-text skill buy you anything? Here is the evidence, and I want to be precise because this number gets misread. We took pharmacogenomics, deliberately, because it is the one corner of genomics with an authoritative ground truth, the CPIC guidelines, and ran 44,550 scored evaluations across frontier models in three conditions. Free prompt: about 81%. Guideline as reasoning context: 95.5%. Skill executes the guideline deterministically: 100%. The honest reading of that 100%: not the model becoming cleverer, the model taken out of the answer. The deterministic skill applies CPIC logic the same way every time; correctness is constrained by architecture, not by asking nicely. And note the scope: this is PGx, where truth is tabulated. Alignment and variant calling have no CPIC, which is exactly why the framework I show in a moment matters.</div>
</section>

<!-- 10. THE COUNTERINTUITIVE RESULT -->
<section class="slide">
    <div class="section-label">The counterintuitive result</div>
    <h2>The right guideline made the model <span class="red">more dangerous</span></h2>
    __COUNTER__
    <p class="gap center" style="max-width:90%; margin-top:0.8rem; font-size:clamp(1rem,1.6vw,1.3rem);">Trust is <span class="green">architectural</span>: it comes from deterministic, auditable, model-invariant execution, not from a better prompt.</p>
    <div class="notes">[1:20] The result that should give everyone pause, found only because we scored at scale. Give the model the correct guideline as context and average accuracy goes up; the headline improves, most cases get better. But underneath the average, a minority of previously safe answers flipped to confident and wrong. Adding the right information created a new failure mode the average concealed. This is why I do not trust prompt-level fixes for consequential work: a better prompt can raise the mean and quietly introduce new, fluent, hard-to-catch errors. Trust has to be architectural: deterministic, auditable, the same regardless of model. That is the bridge to the most important slide, because this gets worse the moment you leave curated European data.</div>
</section>

<!-- 11. THE HEADLINE -->
<section class="slide">
    <div class="section-label">The headline</div>
    <h2>On real genomes, accuracy <span class="red">falls by ancestry</span></h2>
    __ANCESTRY__
    <p class="gap center" style="max-width:90%; margin-top:0.6rem; font-size:clamp(0.92rem,1.45vw,1.18rem);">Curated ~96% <span class="red">does not transfer</span> to real diplotypes from 7,000+ individuals; error grows with distance from the European reference. <span class="green">Executing the skill removes the gradient.</span> Validation is an equity problem.</p>
    <div class="notes">[2:00] The slide I would build the whole talk around. That curated 96% is measured on clean, curated cases. Run the same skill on real diplotypes from over seven thousand actual people and it collapses, and it collapses by ancestry. European, 72%. Latin American, from the Peruvian Genome Project, 51%. East African, from the Uganda Genome Resource, 40%. Accuracy falls with distance from the European reference the tools were built on. This is not an ethics footnote; it is a correctness result. An agent left to its defaults reaches for the most abundant European resources and silently inherits this gradient, at scale. The green line: when the skill executes deterministically, every ancestry returns to roughly 100%. The fix for the equity gap and the fix for the trust gap are the same fix. Equity has to be engineered, not declared.</div>
</section>

<!-- 12. SO WHAT DO WE DO -->
<section class="slide">
    <div class="section-label">So what do we do</div>
    <h2>Validation <span class="green">proportional to consequence</span></h2>
    <div class="three-col gap" style="margin-top:1rem;">
        <div class="card"><h3 class="accent">Research-grade</h3><p style="text-align:center; color:#e6edf3; font-weight:600; margin-bottom:0.4em;">Hypothesis exploration</p><p>Unit tests; adversarial inputs (empty, malformed, edge cases); researcher reviews every output.</p></div>
        <div class="card"><h3 class="orange">Benchmarked</h3><p style="text-align:center; color:#e6edf3; font-weight:600; margin-bottom:0.4em;">Publishable analyses</p><p>Validated on public reference sets (GIAB, curated atlases); metrics with CIs; documented failure modes.</p></div>
        <div class="card"><h3 class="green">Clinical-grade</h3><p style="text-align:center; color:#e6edf3; font-weight:600; margin-bottom:0.4em;">Patient care, diagnostics</p><p>External multi-site validation; signed reproducibility bundles; audit trails; regulatory + CLIA/CAP.</p></div>
    </div>
    <p class="gap center" style="max-width:90%; margin-top:1.5rem; font-size:clamp(0.95rem,1.5vw,1.2rem);"><span class="red">Today, every surveyed system sits at research-grade.</span> None has published the external evidence the clinical tier demands; that gap is itself the finding.</p>
    <div class="notes">[1:40] So what do we do? Not abandon agents: calibrate scrutiny to consequence. Three tiers. Research-grade: exploration, where you need unit tests, adversarial inputs (the empty file from slide seven) and a human reading every output. Benchmarked: publishable work, validation on public reference sets like Genome in a Bottle, metrics with confidence intervals, documented failure modes. Clinical-grade: patient care, external multi-site validation, signed reproducibility bundles, audit trails, regulatory alignment, CLIA and CAP. The uncomfortable part, applying to ClawBio too: every system we surveyed, ours included, currently sits at research-grade. None has published the external multi-site evidence the clinical tier requires. That is the finding. The field generates analyses far faster than the evidence to trust them in consequential settings. The job is to close that distance, tier by tier.</div>
</section>

<!-- 13. WHAT TO REMEMBER -->
<section class="slide">
    <div class="section-label">What to remember</div>
    <h2>Three things to take away</h2>
    <div class="three-col gap" style="margin-top:1rem;">
        <div class="card"><div style="color:#56d364; font-size:clamp(1.6rem,2.6vw,2.4rem); font-weight:800;">1</div><h3 class="accent" style="margin:0.2em 0 0.4em;">The bottleneck has moved</h3><p>Agents produce analyses faster than we can check them. Your scarce skill is now judgement, not code.</p></div>
        <div class="card"><div style="color:#56d364; font-size:clamp(1.6rem,2.6vw,2.4rem); font-weight:800;">2</div><h3 class="accent" style="margin:0.2em 0 0.4em;">Trust is architectural</h3><p>It comes from deterministic, auditable, model-invariant execution, not from a better prompt or a bigger model.</p></div>
        <div class="card"><div style="color:#56d364; font-size:clamp(1.6rem,2.6vw,2.4rem); font-weight:800;">3</div><h3 class="accent" style="margin:0.2em 0 0.4em;">Equity is engineered, not declared</h3><p>The accuracy gap across ancestries is a correctness gap. The fix is the same as the fix for trust.</p></div>
    </div>
    <p class="gap center" style="max-width:90%; margin-top:1.5rem; font-size:clamp(0.95rem,1.5vw,1.2rem);">Domain expertise is the one thing that cannot be automated; it is the <span class="green">irreducible human contribution</span> to an increasingly automated science.</p>
    <div class="notes">[1:00] If you remember three things, these. One: the bottleneck has moved; agents produce faster than we can check, so your scarce skill is now judgement, not code. Two: trust is architectural; deterministic, auditable, model-invariant execution, not a cleverer prompt or a bigger model. Three: equity is engineered, not declared; the accuracy gap across ancestries is a correctness gap, and the fix is the same fix as for trust. Underneath all three sits the one thing that does not automate: domain expertise. That is the irreducible human contribution. With that, over to the live work.</div>
</section>

<!-- 14. OVER TO GENOMIC INTELLIGENCE -->
<section class="slide">
    <div class="section-label alt">Over to Genomic Intelligence</div>
    <h2>From the framing to the <span class="green">live work</span></h2>
    <div class="two-col content gap" style="margin-top:0.6rem;">
        <div>
            <h3 style="text-align:left; color:#d2a8ff;">Next, with Benjamin &amp; the GI team</h3>
            <ul>
                <li>What the Genomic Intelligence models are, and where they fit.</li>
                <li>Live scenarios: GI skills running <span class="green">inside ClawBio</span> on real bio problems.</li>
                <li>Follow along in Codex; prompts and links go in the chat.</li>
            </ul>
        </div>
        <div>
            <h3 style="text-align:left; color:#56d364;">Try it yourself, now</h3>
            <ul>
                <li>Ask a real, openly published genome questions, live: every answer executed by a ClawBio skill.</li>
                <li><code style="background:none; padding:0; color:#58a6ff;">conversational.clawbio.ai</code></li>
                <li>Star the repo: <code style="background:none; padding:0; color:#56d364;">github.com/ClawBio/ClawBio</code></li>
            </ul>
        </div>
    </div>
    <p class="gap center" style="max-width:86%; margin-top:1.4rem; font-size:clamp(1rem,1.6vw,1.3rem);">The point of the demos is not "the agent can run it"; it is "<span class="green">you can trust what it ran</span>".</p>
    <div class="notes">[0:50] That is my framing. Over to the live work. Benjamin and the GI team show you what the Genomic Intelligence models are and where they fit, then run live scenarios: GI skills inside ClawBio on real, openly published genomes. Follow along in Codex; we will drop prompts and links in the chat. You do not have to watch passively: go to conversational.clawbio.ai right now and ask a real genome a question; every answer is executed by a ClawBio skill, not improvised by a chatbot. Keep one test in your head: the demos are not trying to prove the agent can run it. They show you can trust what it ran. Benjamin, over to you.</div>
</section>

<!-- 15. BUILD WITH US -->
<section class="slide">
    <div class="section-label">Build with us</div>
    <h2>Take it further</h2>
    <div style="display:flex; align-items:flex-start; justify-content:center; gap:5vw; margin-top:1.0rem;">
        <div style="text-align:center; max-width:30em;">
            <div style="color:#e3b341; font-weight:700; font-size:clamp(0.8rem,1.2vw,1rem); letter-spacing:0.05em; text-transform:uppercase; margin-bottom:0.5rem;">Out now</div>
            <div style="background:#fff; border-radius:12px; padding:0.8em; display:inline-block; box-shadow:0 10px 32px rgba(0,0,0,.4);">
                <img src="figures/book-qr.png" alt="QR code to buy the book on Amazon" style="display:block; width:clamp(150px,17vw,220px); height:auto;">
            </div>
            <div style="margin-top:0.8rem; color:#e6edf3; font-weight:700; font-size:clamp(0.95rem,1.4vw,1.2rem);">Build an Agentic Genomics System <span class="muted">(From Scratch)</span></div>
            <div style="color:#adbac7; font-size:clamp(0.8rem,1.15vw,1rem); margin-top:0.2em;">Paperback &amp; Kindle &middot; 328 pages</div>
            <div style="color:#6e7681; font-size:clamp(0.78rem,1.1vw,0.95rem); margin-top:0.5em;">Build it in your browser on a real, openly published genome: your first runnable skill in minutes, then the agents and guardrails that keep them honest.</div>
        </div>
        <div style="text-align:center;">
            <div style="color:#56d364; font-weight:700; font-size:clamp(0.8rem,1.2vw,1rem); letter-spacing:0.05em; text-transform:uppercase; margin-bottom:0.5rem;">Join the community</div>
            <img src="figures/whatsapp-qr.png" alt="QR code to join the ClawBio WhatsApp group" style="display:block; width:clamp(170px,20vw,260px); height:auto; border-radius:12px; box-shadow:0 10px 32px rgba(0,0,0,.4);">
            <div style="margin-top:0.8rem; color:#56d364; font-weight:700; font-size:clamp(0.95rem,1.4vw,1.2rem);">WhatsApp group</div>
            <div style="color:#6e7681; font-size:clamp(0.8rem,1.15vw,1rem); margin-top:0.2em;">scan with your camera</div>
            <div style="color:#adbac7; font-size:clamp(0.82rem,1.2vw,1.05rem); margin-top:0.5em;">Hackathons &amp; workshops: <code style="background:none; padding:0; color:#58a6ff;">luma.com/ClawBio</code></div>
        </div>
    </div>
    <p class="gap center" style="max-width:84%; margin-top:1.2rem; font-size:clamp(0.92rem,1.4vw,1.18rem); color:#adbac7;">Open call: ship your own use case on the platform in the next two weeks. <span class="green">Best submissions win.</span></p>
    <p class="center small" style="margin-top:0.5rem;">Try it live: <code style="background:none; padding:0; color:#56d364;">conversational.clawbio.ai</code> &middot; Build with us: <code style="background:none; padding:0; color:#58a6ff;">github.com/ClawBio/ClawBio</code></p>
    <div class="notes">[0:40] Two ways to take this further while the demos run. The book, Build an Agentic Genomics System From Scratch, is hands-on; you build it in your browser on a real published genome, your first runnable skill in minutes and then the validation and guardrails that keep agents honest. Scan the left QR. Join the community on the right: WhatsApp for the conversation, Luma for hackathons and workshops. The open call stands: ship a use case on the platform in the next fortnight, and the best submissions win. Now, let's watch it run.</div>
</section>
"""

BODY = BODY.replace("__WAVES__", WAVES).replace("__COUNTER__", COUNTER).replace("__ANCESTRY__", ANCESTRY)

out = head + "\n<body>\n<div class=\"deck\">\n" + BODY + "\n</div>\n" + footer
open(SRC, "w").write(out)

# guard: no em/en dashes in the generated file
bad = sum(out.count(c) for c in ("—", "–"))
print("wrote index.html, slides:", out.count('class="slide'), "| em/en dashes:", bad)

---
title: Deployment
description: Deploy ClawBio to Docker, Railway, or your own private cloud.
---

# Deployment

Run ClawBio beyond your laptop. Choose the deployment option that fits your needs.

<div class="section-cards" markdown>

<a class="section-card" href="../deployment/docker/">
  <div class="section-card__icon">🐳</div>
  <h3 class="section-card__title">Docker</h3>
  <p class="section-card__desc">Containerise ClawBio with Docker and docker-compose. Volume mounts for genomic data, GPU passthrough for ML skills.</p>
</a>

<a class="section-card" href="../deployment/railway/">
  <div class="section-card__icon">🚂</div>
  <h3 class="section-card__title">Railway</h3>
  <p class="section-card__desc">One-click cloud deployment with persistent storage, environment variables, and custom domains.</p>
</a>

<a class="section-card" href="../deployment/private-cloud/">
  <div class="section-card__icon">🔒</div>
  <h3 class="section-card__title">Private Cloud</h3>
  <p class="section-card__desc">Self-hosted on AWS, GCP, or Azure. Kubernetes, VPN, and air-gapped options for sensitive genomic data.</p>
</a>

</div>

## Which Option?

| Requirement | Docker | Railway | Private Cloud |
|---|---|---|---|
| Local development | ✅ | — | — |
| Quick cloud deploy | — | ✅ | — |
| GPU for ML skills | ✅ | — | ✅ |
| Data residency compliance | — | — | ✅ |
| Air-gapped / no internet | — | — | ✅ |
| Cost | Free | ~$5/mo | Variable |

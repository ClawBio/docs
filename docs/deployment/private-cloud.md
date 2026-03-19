---
title: Private Cloud
description: Self-hosted ClawBio deployment for sensitive genomic data.
---

# Private Cloud Deployment

For organisations handling sensitive genomic data, regulatory compliance, or air-gapped environments, self-hosted deployment gives you full control.

---

## When to Self-Host

- **Data residency requirements** — genomic data must stay in a specific jurisdiction
- **Institutional policy** — no patient data on third-party cloud platforms
- **Air-gapped environments** — no internet access (clinical, government, defence)
- **GPU workloads** — ML-heavy skills need dedicated GPU hardware
- **Cost optimisation** — high-volume usage is cheaper on owned infrastructure

## VM Setup

### AWS EC2

```bash
# Launch an instance
aws ec2 run-instances \
  --image-id ami-0abcdef1234567890 \
  --instance-type t3.xlarge \
  --key-name your-key \
  --security-group-ids sg-xxx

# SSH in and clone ClawBio
ssh -i your-key.pem ubuntu@<instance-ip>
git clone https://github.com/ClawBio/ClawBio.git
cd ClawBio
pip3 install -r requirements.txt
```

For GPU skills, use a `g5.xlarge` (NVIDIA A10G) or `p3.2xlarge` (V100) instance.

### GCP Compute Engine

```bash
gcloud compute instances create clawbio-vm \
  --zone=europe-west2-a \
  --machine-type=e2-standard-4 \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud
```

### Azure Virtual Machines

```bash
az vm create \
  --resource-group clawbio-rg \
  --name clawbio-vm \
  --image Ubuntu2204 \
  --size Standard_D4s_v3 \
  --admin-username azureuser \
  --generate-ssh-keys
```

## Kubernetes Deployment

For teams running multiple ClawBio instances or integrating with existing infrastructure:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: clawbio
spec:
  replicas: 1
  selector:
    matchLabels:
      app: clawbio
  template:
    metadata:
      labels:
        app: clawbio
    spec:
      containers:
        - name: clawbio
          image: your-registry/clawbio:latest
          envFrom:
            - secretRef:
                name: clawbio-secrets
          volumeMounts:
            - name: data
              mountPath: /app/data
            - name: results
              mountPath: /app/results
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: clawbio-data
        - name: results
          persistentVolumeClaim:
            claimName: clawbio-results
---
apiVersion: v1
kind: Secret
metadata:
  name: clawbio-secrets
type: Opaque
stringData:
  LLM_API_KEY: "your-key"
  CLAWBIO_MODEL: "gpt-4o"
  TELEGRAM_BOT_TOKEN: "your-token"
```

## Security Considerations

### Network

- Run ClawBio behind a VPN or bastion host — no direct internet exposure
- Use security groups / firewall rules to restrict inbound access
- TLS termination at a reverse proxy (nginx, Caddy, or cloud load balancer)

### Data

- Encrypt volumes at rest (AWS EBS encryption, GCP CMEK, Azure Disk Encryption)
- Genomic data should never leave the instance — ClawBio processes everything locally
- Audit log all file access and skill invocations

### Secrets

- Store API keys in a secrets manager (AWS Secrets Manager, GCP Secret Manager, HashiCorp Vault)
- Never bake secrets into Docker images
- Rotate keys regularly

### Access Control

- SSH key-based access only — no password authentication
- Use IAM roles (AWS) / service accounts (GCP) for programmatic access
- Implement least-privilege principles for all users and services

## Air-Gapped Deployment

For environments with no internet access:

1. **Pre-download** all Python dependencies:
   ```bash
   pip download -r requirements.txt -d ./packages
   ```

2. **Transfer** the ClawBio repo and packages to the air-gapped network (USB, secure transfer)

3. **Install** from local packages:
   ```bash
   pip install --no-index --find-links ./packages -r requirements.txt
   ```

4. **Use a local LLM** — Ollama or LM Studio with a downloaded model:
   ```bash
   LLM_BASE_URL=http://localhost:11434/v1
   LLM_API_KEY=ollama
   CLAWBIO_MODEL=llama3.1
   ```

!!! warning "Model quality matters"
    Local models (7B–70B parameters) are significantly less capable than cloud models (GPT-4o, Claude Sonnet) for complex bioinformatics reasoning. Test your skills thoroughly with the chosen local model before deploying to production.

## Monitoring and Maintenance

- **Logs**: Use systemd journal, CloudWatch, or your existing log aggregation
- **Updates**: `git pull` and `pip install -r requirements.txt` — no container rebuild needed for direct deployments
- **Backups**: Regular snapshots of the data and results volumes
- **Health checks**: Cron job or monitoring agent to verify the bot process is running

---

**See also:** [Docker](docker.md) for containerised deployment, [Railway](railway.md) for managed cloud hosting.

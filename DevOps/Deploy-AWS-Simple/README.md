# Galactic Field Guide

A React and TypeScript catalog for Star Wars characters, planets, and starships, powered by [swapi.info](https://swapi.info/).

## Local development

```sh
npm install
npm run dev
```

The development server prints its local URL. Production assets are generated in `dist` with:

```sh
npm run build
```

## Apache container

Build and start the app locally with Docker Compose:

```sh
docker compose up --build
```

Open `http://localhost:8080`. The multi-stage `Dockerfile` builds the Vite app and copies `dist` into Apache's `/usr/local/apache2/htdocs` document root. `apache/000-default.conf` enables `.htaccess` overrides, and `public/.htaccess` rewrites client-side routes to `index.html` while preserving existing files and directories.

The browser fetches catalog data directly from `https://swapi.info/api/people`, `/planets`, and `/starships`; no API credentials or server-side secrets are required.

## Deploy to EC2

The `Build and deploy to EC2` GitHub Actions workflow builds the Docker image on pushes to `main` or when started manually. It stores the compressed image as a short-lived GitHub Actions artifact, then copies it to the EC2 instance over SSH and runs it with Apache's container port `80` mapped to `APP_PORT`. No container registry is used.

Configure these repository secrets under **Settings → Secrets and variables → Actions**:

- `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`: credentials allowed to call `ec2:DescribeInstances` in the configured region.
- `SSH_KEY`: unencrypted private SSH key authorized for the EC2 deployment user.

Configure these repository variables:

- `EC2_INSTANCE_PUBLIC_IP`: the instance's public IPv4 address.
- `AWS_REGION`: the region containing the instance.
- `APP_PORT`: host port to publish for the web application, such as `80`.
- `EC2_SSH_USER`: optional SSH username; defaults to `ec2-user` (set to `ubuntu` for a typical Ubuntu image).

The workflow uses `SSH_KEY` for SSH authentication and disables SSH host-key checking, so no host fingerprint is required. This permits connecting without a pinned EC2 host identity and does not protect against a man-in-the-middle host impersonation.

The instance must have Docker installed and running, and its security group must allow SSH from the GitHub runner's egress address and inbound traffic on `APP_PORT`. Use a self-hosted runner with a stable egress address when a narrow SSH source rule is required. The workflow checks that the public IP resolves to a running instance in `AWS_REGION`, deploys the image, probes the SPA route, and removes older images belonging to this app only.

## Deploy with Jenkins

`Jenkinsfile` is a Declarative Pipeline equivalent of `.github/workflows/deploy-with-instance.yml`. Create a **Pipeline from SCM** job pointing to this file, or a Multibranch Pipeline. Install the Pipeline (including Declarative), Git, and Credentials Binding plugins. The selected agent must run Linux and have Bash, Git, Docker, AWS CLI, jq, gzip, and OpenSSH installed, with permission to use the Docker daemon.

Create these Jenkins credentials, using the exact IDs below:

- `AWS_ACCESS_KEY_ID`: **Secret text** containing the AWS access key ID.
- `AWS_SECRET_ACCESS_KEY`: **Secret text** containing the AWS secret access key.
- `SSH_KEY`: **Secret file** containing the unencrypted private SSH key matching `KEY_PAIR_NAME`.

The AWS credentials need permission to describe instances, subnets, security groups, and key pairs, and to run, tag, and start EC2 instances. Scope these permissions to the intended deployment resources where possible.

Supply `AWS_REGION`, `AMI_ID`, `KEY_PAIR_NAME`, `VPC_ID`, `SUBNET_ID`, and `SECGRP_ID` as build parameters. `EC2_SSH_USER` defaults to `ec2-user`, and `APP_PORT` defaults to `80`. `BUILD_CONTEXT` defaults to `.` for a checkout rooted at this app; when checking out the entire TrainingDocs repository, set it to `DevOps/Deploy-AWS-Simple`.

Start the job manually with **Build with Parameters**. The pipeline builds a commit-tagged image, archives its compressed image with one-day artifact retention, finds or creates the instance named `Frontend`, and installs Docker before deploying. Provisioning and deployment have 35-minute and 15-minute timeouts respectively. All stages share one agent and its temporary image archive; the discovered public IP is passed through the pipeline environment. Temporary local deployment files are removed in `post { always { ... } }`.

The AMI must support `yum` and `systemd`, as in the source workflow. The subnet must provide public network access, and the security group must allow SSH from the Jenkins agent and inbound traffic on `APP_PORT`. SSH host-key checking remains disabled to match the GitHub Actions workflow; this does not protect against host impersonation.

Concurrent builds of the same Jenkins job are queued rather than cancelled. Use a single deployment job for this environment: this setting does not serialize separate jobs, multibranch jobs, or deployments from GitHub Actions. No automatic trigger is declared in the Jenkinsfile.
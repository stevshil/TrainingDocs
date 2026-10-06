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
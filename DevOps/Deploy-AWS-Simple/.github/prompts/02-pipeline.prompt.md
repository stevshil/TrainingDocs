# Create the GitHub Action pipeline

This is to create a GitHub Actions pipeline for deploying a Docker container to an AWS EC2 instance.

This pipeline will build the Docker container and upload the image from GitHub artifact storage to the AWS EC2 instance.

The AWS EC2 instance will then extract and run the Docker container.

This setup ensures that the application is consistently deployed and can be easily updated by pushing new Docker images to the GitHub repository.

This approach does not use a Docker registry, relying instead on GitHub artifact storage to transfer Docker images to the AWS EC2 instance.

The EC2 instance public IP address, AWS Access and Secret keys will be provided as GitHub secrets and variables and will be called;
- EC2_INSTANCE_PUBLIC_IP
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- SSH_KEY
- APP_PORT
  - Used to denote the host port number

These secrets and variables will be used in the GitHub Actions workflow to authenticate with AWS and deploy the Docker container to the EC2 instance.

The GitHub Actions workflow will typically include steps to:
- Build the Docker container.
- Upload the Docker image to GitHub artifact storage.
- Download the Docker image on the AWS EC2 instance.
- Extract and run the Docker container on the EC2 instance.
- Clean up any temporary files or Docker images on the EC2 instance to free up space.
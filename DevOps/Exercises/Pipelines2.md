# Pipelines 2

This exercise gets you automating the build of a VM in your cloud provider using GitHub Actions, Bitbucket pipelines or Jenkins, or any other automation service.

Using the [Deploy-AWS-Simple](../Deploy-AWS-Simple) project as your starting point, which currently deploys a ReactJS SPA to an existing EC2 instance.

## Preparing

1. Copy the folder Deploy-AWS-Simple to a new location on your system.
    > **NOTE:** Make sure that you copy the directory outside of any other Git repositories you have on your machine.

2. Initialise the directory as a Git repository;
    ```
    cd Deploy-AWS-Simple
    git init
    ```
3. Create your Git repository on your Git server ready to take your local copy.
4. Run the `git remote add` line, but do not do anything else yet.

## The pipeline

The pipeline should decide whether it needs to build a new VM or to use an existing one, prior to deploying the application.

The workflow;

1. Build the ReactJS application and Docker container
2. Provision the cloud instance using the command line tools
    - GitHub Actions already has an AWS command line action
    - At this stage you want to check if a VM already exists with a tag of "Frontend"
        - If it does then grab the public IP address of that VM
            - You will need this for other jobs, so it will need to be published in some way
        - If the VM does not exist
            - Run the appropriate commands to launch a new VM
                - e.g. aws ec2 ......
            - You will need to provide the following as variables from your Git server, e.g. GitHub -> Actions -> Secrets and Variables
                - Tag name of **Frontend**
                - Instance type of **t3.micro**
                - AMI ID of GitHub variable **AMI_ID**
                - Key pair name of GitHub variable **KEY_PAIR_NAME**
                - VPC ID of GitHub variable **VPC_ID**
                - Subnet ID of GitHub variable **SUBNET_ID**
                - Security Group ID of GitHub variable **SECGRP_ID**
            - You should have the values for these set up in your GitHub repository before pushing this repository.
                - Change the names according to your cloud provider.  e.g. Azure does not have a VPC_ID, but a subscription.
3. Once the VM is provisioned, you should ensure you have the Public IP, and that you can connect to it.
    - You should consider waiting until the connection is available
    - When should you give up on the connection?
4. If you cannot connect then fail the pipeline
5. If you can connect then continue with the deployment.

### Optional extras

Think about the following and add them to your deployment;

1. Rather than having to supply the values as variables for certain attributes, have the pipeline create those items if they do not already exist.  You should tag these items with **Frontend** so that it is easy to target them all.
    - Security Group
    - KEY_PAIR
        - This will mean that you cannot log on to the VM directly, which is a good thing.

2. Reducing downtime.
    - There is a small downtime using this method when the pipeline removes the old container and starts the new one.
    - Look into possible options and ways of acheiving a near zero downtime.

# Destroying

You should also consider destroying the VM as a separate, manual execution, so that you don't have to log in to your cloud provider to remove the instance.
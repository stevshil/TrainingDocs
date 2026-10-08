# Adding an EC2 instance

Add a job before deploy and after build that does the following;
1. Checks to see if an EC2 instance exists with the tag of "Frontend".
2. If no such instance exists, create a new EC2 instance with the tag of "Frontend".
  - The instance should use the following values;
    - Tag name of "Frontend"
    - Instance type of "t3.micro"
    - AMI ID of GitHub variable AMI_ID
    - Key pair name of GitHub variable KEY_PAIR_NAME
    - VPC ID of GitHub variable VPC_ID
    - Subnet ID of GitHub variable SUBNET_ID
    - Security Group ID of GitHub variable SECGRP_ID
  - On completion obtain the public IP address of the newly created instance.
3. If the instance exists obtain its current public IP address.
4. Use the obtained public IP address for subsequent deployment steps.
5. Update the GitHub variable EC2_INSTANCE_PUBLIC_IP with the obtained public IP address.
6. Ensure that any subsequent deployment steps reference the updated GitHub variable EC2_INSTANCE_PUBLIC_IP.
7. Verify that the EC2 instance is accessible using the updated public IP address.
8. If the EC2 instance is not accessible wait for 1 minute and then recheck its accessibility.
  - Perform this action 3 times.
  - If it is still not accessible after 3 attempts, raise an error and halt the deployment process.
9. Install Docker onto the instance using the following steps;
  - Connect to the instance using SSH and the key pair specified by the GitHub variable KEY_PAIR_NAME.
  - Install Docker: `sudo yum -y install docker`
  - Add the current user to the Docker group: `sudo usermod -aG docker $USER`
  - Start end enablethe Docker service: `sudo systemctl enable --now docker`
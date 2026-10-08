# Pipeline to destroy the AWS instance

This pipeline will terminate the EC2 instance tagged as "Frontend" and clean up associated resources.

Steps involved:
1. Identify the EC2 instance with the tag "Frontend".
2. Terminate the identified EC2 instance.
    - Use the do not wait for the instance to shutdown option when terminating the instance.
3. Verify that the instance has been successfully terminated.
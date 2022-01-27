# Telerik Final project
![GitHub last commit](https://img.shields.io/github/last-commit/npghub/telerik-fp) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/npghub/telerik-fp/Telerik%20Final%20Project)

Uses a simple python program that ouputs some text.

It undergoes style, lint, unit testing, quality and security checks before a docker container is built,
containing a fcgi set up nginx with the test program copied over.
If this container is successfully built it is uploaded to a docker repo.
Later manually deployed to a local Kubernetes cluster(minikube).

## Workflow

1. Pre build step - only purpose is to ouput some GitHub variables.
2. Style and linting on the python code. These are done in parallel. Style is done with **pycodestyle**. Linting is done with **pylint**. Pylint version 2.11.1 had to be used, because job dod not complete with latest.
3. Unit testing is performed. This job depends on **style** and **lint** jobs. Unit testing is done with **doctest**.
4. SAST and SCA steps are performed in parallel. **Sonarcloud** is for SAST and **Snyk** for SCA.
5. Build docker image and upload it to Docker Hub. The image is tagged with 8 symbols from the GitHub SHA and laso with **latest** tag. An extra step was added here to handle image tag for the extra added config repo job. This job depends on SAST and SCA jobs. Image![Docker Image Size (tag)](https://img.shields.io/docker/image-size/5ko5ko/telerikrepo/latest) can be pulled and run standalone with:

```bash
docker run -p 80:80 5ko5ko/telerikrepo:latest

and then in your browser:

http://localhost/cgi-bin/test.cgi
```
6. DAST scan. Uses **StackHawk** service and GitHub action to pull, run and security test the running application.
7. Update the Kubernetes manifest file with the new image tag so ArgoCD can detect and reflect changes. Does a checkout on the config repo, edits the manifest file and then pushes the changes back. This job depends on DAST job. This job was added later(see *)

After the workflow competes successfully and a docker image is uploaded to Docker Hub registry the application is deployed to a locally runing Kubernetes cluster(**minikube**). Deployment is done manually. This later amended using ArgoCD(see *)


*Added after project submission:
 1. Another config repo exists where configuration for ArgoCD is stored and Kubernetes manifest is monitored.
 2. Rewrite main repo workflow to include an extra step, which updates the Kubernetes manifest in above config repo with the docker image tag
 3. ArgoCD is set up to monitor the above config repo and re-deploy the cluster if changes in the manifest are detected.
 4. This step is configured to run after a successful DAST scan is completed.

## This project uses:
- [Python](https://www.python.org/)
- [NGINX](https://www.nginx.com/)
- [Docker](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/)
- [Kebernetes](https://kubernetes.io/)
- [ArgoCD](https://argoproj.github.io/)
- [Sonarcloud](https://sonarcloud.io/)
- [Snyk](https://snyk.io/)
- [StackHawk](https://www.stackhawk.com/)


## To be improved:
 1. Add app monitoring(Maybe integrate with NewRelic)
 2. Add alerting
 3. Add worklflow process notifications(Slack, Teams, Email, etc.)
 4. Add a job to scan for exposed secrets
 5. Try IaC with Terraform

## Abbreviations used
- SCA: Software composition analysis 
- SAST: Static application security testing
- DAST: Dynamic application security testing
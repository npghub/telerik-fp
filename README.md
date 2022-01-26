# telerik-fp
Final project page

Uses a simple python program that ouputs some text.

It undergoes style, lint, unit testing, quality and security checks before a docker container is built,
containing a fcgi set up nginx with the test program copied over.
If this container is successfully built it is uploaded to a docker repo.
Another config repo exists where configuration for ArgoCD is stored and Kubernetes manifest is monitored.

Style checks are done using pycodestyle.
Linting is done with pylint version 2.11.1 as later versions give errors.
Unit testing is done with doctest.

Quality and security testing is performed using Sonarcloud and Snyk.

Built and uploaded image can be tested with:

docker run -p 80:80 5ko5ko/telerikrepo:latest

and then in your browser:

http://localhost/cgi-bin/test.cgi

There was an extra step which updates the Kubernetes manifest in the config repo with the new image tag,
but a way to do thi reliably was not found.

After the image is built it is deployed to K cluster with ArgoCD.

To be improved:

1.Monitoring

2.Alerting

3.Notifications

4.Scan for exposed secrets

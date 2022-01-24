# telerik-fp
Final project page

Uses a simple python program that ouputs some text.

It undergoes style, lint, unit testing and security checks before a docker container is built,
containing a fcgi set up nginx with the test program copied over.
If this container is successfully built it is uploaded to a docker repo.

Style checks are done using pycodestyle.
Linting is done with pylint version 2.11.1 as later versions give errors.
Unit testing is done with doctest.

Security testing is performed using Sonarcloud and Snyk.

Built and uploaded image can be tested with:

docker run -p 80:80 5ko5ko/telerikrepo:latest

and then in your browser:

http://localhost/cgi-bin/test.cgi
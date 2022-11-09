### Hexlet tests and linter status:
[![Actions Status](https://github.com/EzerTigger/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/EzerTigger/python-project-49/actions)
<a href="https://codeclimate.com/github/EzerTigger/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/55d0d7735efd70b4600d/maintainability" /></a>

####Getting started
***
Clone the current repository via command:
>git clone https://github.com/EzerTigger/python-project-49.git 

####Requirements
***
- Python = "^3.10"
- Poetry = "^1.2.2"

Check your pip version with the following command:
>python -m pip --version

Make sure that pip is always up to update. If not, use the following:
>python -m pip install --upgrade pip

####Makefile
***
Using the Makefile you can generate all the needed packages for your virtual env.

To install poetry packages:
~~~
make install
~~~ 
To build your packages inside your project:
~~~
make build
~~~
It will let us execute the publish command knowing exactly what is going into the build:
~~~
make publish
~~~
Installs the build package from our OS, so we can start using simple shell commands:
~~~
make package-install
~~~


brain-even: [![asciicast](https://asciinema.org/a/534033.svg)](https://asciinema.org/a/534033)
brain-calc:[![asciicast](https://asciinema.org/a/535529.svg)](https://asciinema.org/a/535529)
brain-gcd:[![asciicast](https://asciinema.org/a/535548.svg)](https://asciinema.org/a/535548)
brain-prime:[![asciicast](https://asciinema.org/a/535624.svg)](https://asciinema.org/a/535624)
brain_progression:[![asciicast](https://asciinema.org/a/535592.svg)](https://asciinema.org/a/535592)

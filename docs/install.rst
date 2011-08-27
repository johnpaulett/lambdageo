Installation
============

Install the dependencies::

    sudo apt-get install python-pip python-virtualenv gdal-bin postgresql-8.4-postgis postgresql-server-dev-8.4 

Create PostGIS template and a spatially-enabled database::

    sudo su - postgres
    curl https://docs.djangoproject.com/en/dev/_downloads/create_template_postgis-debian.sh | bash
    createuser -D -A -R -P lambdageo
    createdb -T template_postgis -O lambdageo lambdageo


To get started create a `virtualenv <http://www.virtualenv.org/>`_ and install
the dependencies with `pip <http://www.pip-installer.org/>`_::

    virtualenv --no-site-packages env
    source env/bin/activate
    pip install -r requirements.txt

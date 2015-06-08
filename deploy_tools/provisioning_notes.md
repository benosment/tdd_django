Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv


## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

    /home/username
    .
    `-- sites
        `-- SITENAME
            |-- database
            |-- source
            |-- static
            |-- virtualenv


## Example:
    # use NGINX template
    sed "s/SITENAME/superlists.benosment.com/g" deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/superlists.benosment.com
    # activate that site
    sudo ln -s ../sites-available/superlists.benosment.com /etc/nginx/sites-enabled/superlists.benosment.com
    # use gunicorn template
    sed "s/SITENAME/superlists.benosment.com/g" deploy_tools/gunicorn-upstart.template.conf | sudo tee /etc/init/gunicorn-superlists.benosment.conf
    # start both services
    sudo service nginx reload
    sudo start gunicorn-superlists.benosment
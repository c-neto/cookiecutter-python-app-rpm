# template-python-app-rpm

- __Date__: 01/11/2020
- __Author__: [@augustoliks](https://github.com/augustoliks)
- __Description__: Cookiecutter project template for create Python application wrapped over RPM format with dependencies embedded. 
- __Objective__: Provides productivity on wrapped python generic application over RPM package format.  
- __Actual Features__:

    - Application wrapped in RPM format;
    - Python requirements embedded in package;
    - Offline instalation Python requirements;
    - Project running over virtuavenv;
    - Supervisord Unit Configuration;
    - Logrotate Unit Configuration.

## Dependencies

```
pip3 install cookiecutter
```

> Warning: Require Python >= 3.6 and pip compatible

## How to install

- Refer cookiecutter for this github link.

```bash
┌─[auugustoliks]@[localhost]:~/github/demo
└──> $ cookiecutter https://github.com/augustoliks/template-python-app-rpm

project [python-app]: 
description [Project for change World]: 
license [Proprietary]: 
vendor [Github]: 
project_url [https://github.com/augustoliks/template-python-app-rpm]: 
author_name [augustoliks]: 
domain_user_name [augustoliks]: 
author_email [carlos.santos110@fatec.sp.gov.br]: 
project_category [scripts]: 
version [0.1.0-1]: 
```

- After generate, project directory will be created.

```bash
┌─[auugustoliks]@[localhost]:~/github/demo
└──> $ ls
python-app
┌─[auugustoliks]@[localhost]:~/github/demo
└──> $ cd python-app/
┌─[auugustoliks]@[localhost]:~/github/demo/python-app
└──> $ tree .
.
├── Makefile
├── pkg
│   ├── config
│   │   └── python-app.yml
│   ├── logrotate
│   │   └── python-app
│   └── supervisor
│       └── python-app.ini
├── python-app
│   ├── requirements.txt
│   └── run_python-app.py
├── README.md
├── RELEASE-NOTES.md
├── rpm.spec
└── VERSION

5 directories, 10 files
```

## Build RPM

- For create RPM, just run `make rpm`.

```bash
┌─[auugustoliks]@[localhost]:~/github/demo/python-app
└──> $ make rpm

... [COLLAPSE] ...

Gravou: /home/auugustoliks/rpmbuild/SRPMS/python-app-0.1.0-1.src.rpm
Gravou: /home/auugustoliks/rpmbuild/RPMS/x86_64/python-app-0.1.0-1.x86_64.rpm
Executando (%clean): /bin/sh -e /var/tmp/rpm-tmp.Pa1egw

... [COLLAPSE] ...
```

## Verify Files Inside RPM

- `rpm` CLI utilitary informs which files will be installed from RPM indicate with argument on commnand.

```bash
┌─[auugustoliks]@[localhost]:~/github/demo/python-app
└──> $ rpm -Vv /home/auugustoliks/rpmbuild/RPMS/x86_64/python-app-0.1.0-1.x86_64.rpm 
.........    /etc/logrotate.d/python-app
.........    /etc/supervisord.d/python-app.ini
.........  c /opt/python-app/config/python-app.yml
.........    /opt/python-app/docs
.........    /opt/python-app/docs/README.md
.........    /opt/python-app/docs/VERSION
.........    /opt/python-app/src
.........    /opt/python-app/src/requirements.txt
.........    /opt/python-app/src/run_python-app.py
.........    /opt/python-app/vendor
.........    /opt/python-app/vendor/certifi-2020.6.20-py2.py3-none-any.whl
.........    /opt/python-app/vendor/chardet-3.0.4-py2.py3-none-any.whl
.........    /opt/python-app/vendor/idna-2.10-py2.py3-none-any.whl
.........    /opt/python-app/vendor/requests-2.24.0-py2.py3-none-any.whl
.........    /opt/python-app/vendor/urllib3-1.25.11-py2.py3-none-any.whl
```

## Install RPM

- Install RPM standalone created in `Build RPM` step.

```bash
┌─[auugustoliks]@[localhost]:~/github/demo/python-app
└──> $ sudo yum install -y --disablerepo=* /home/auugustoliks/rpmbuild/RPMS/x86_64/python-app-0.1.0-1.x86_64.rpm 

... [COLLAPSE] ...

Instalados:
  python-app-0.1.0-1.x86_64                                                                                                                
```

## Verify RPM installed Files

- Supervisor Unit

```bash
┌─[auugustoliks]@[localhost]:~/github/demo/python-app
└──> $ cat /etc/supervisord.d/python-app.ini 
[program:python-app]
directory=/opt/python-app/src/
command=/opt/python-app/src/venv/bin/python3 run_python-app.py
user=root
autostart=true
autorestart=true
redirect_stderr=true

environment=CONFIG_FILE=/opt/python-app/config/python-app.yml
```

- Logrotate Unit

```bash
┌─[auugustoliks]@[localhost]:~/github/demo/python-app
└──> $ cat /etc/logrotate.d/python-app 
/var/log/python-app/logs/*{
    # Rotacionamento feito regularmente por dia
    daily

    # Rotaciona os ultimos 15 arquivos rotacionados
    rotate 15

    # apaga os arquivos rotacionados. nao ha necessidade de criar um arquivo
    # vazio apos a rotacao, python/loguru cria caso na exista o arquivo de log
    # se tem -> atualiza | se nao tem -> cria
    nocreate

    # Comprime os arquivos rotacionados
    compress

    # Move os arquivos rotacionados para o diretorio indicado
    olddir /var/log/python-app/rotated/
}
```

## Project instance running

```bash
┌─[auugustoliks]@[localhost]:~/github/demo/template-python-app-rpm
└──> $ supervisorctl 
python-app                       FATAL     Exited too quickly (process log may have details)
supervisor> tail -f python-app
==> Press Ctrl-C to exit <==
hello augustoliks !!!
test external dependencies... 
get fake rest-api:  {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
hello augustoliks !!!
test external dependencies... 
get fake rest-api:  {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
hello augustoliks !!!
test external dependencies... 
get fake rest-api:  {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
hello augustoliks !!!
test external dependencies... 
get fake rest-api:  {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
```

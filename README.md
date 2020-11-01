# template-python-app-rpm

Cookiecutter project template for create Python application wrapped over RPM format with dependencies embedded.

## Dependencies

```
pip3 install cookiecutter
```

> Warning: Require Python >= 3.6 and pip

## How to install

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

## Build RPM

```bash
┌─[auugustoliks]@[localhost]:~/github/demo/python-app
└──> $ make rpm

rpmbuild -ba rpm.spec \
    --define '_PROJECT_DIR /home/auugustoliks/github/demo/python-app' \
    --define '_VERSION_APP 0.1.0' \
    --define '_VERSION_PKG 1'
Executando (%prep): /bin/sh -e /var/tmp/rpm-tmp.K5lxru
+ umask 022
+ cd /home/auugustoliks/rpmbuild/BUILD
+ rm -rf /tmp/_dependencies
+ mkdir -p /tmp/_dependencies
+ cd /tmp/_dependencies
+ pip3 download -r /home/auugustoliks/github/demo/python-app/python-app/requirements.txt --no-binary=:none: -d /tmp/_dependencies

...

Gravou: /home/auugustoliks/rpmbuild/SRPMS/python-app-0.1.0-1.src.rpm
Gravou: /home/auugustoliks/rpmbuild/RPMS/x86_64/python-app-0.1.0-1.x86_64.rpm
Executando (%clean): /bin/sh -e /var/tmp/rpm-tmp.Pa1egw
+ umask 022
+ cd /home/auugustoliks/rpmbuild/BUILD
+ rm -rf /home/auugustoliks/rpmbuild/BUILDROOT/python-app-0.1.0-1.x86_64
+ RPM_EC=0
++ jobs -p
+ exit 0
```


## Verify Files Inside RPM

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

┌─[auugustoliks]@[localhost]:~/github/demo/python-app
└──> $ sudo yum install -y --disablerepo=* /home/auugustoliks/rpmbuild/RPMS/x86_64/python-app-0.1.0-1.x86_64.rpm 

[sudo] senha para auugustoliks: 
Repository rsyslog_v8_nightly is listed more than once in the configuration
Dependências resolvidas.
===============================================================================================================================================================================================
 Package                                        Architecture                               Version                                      Repository                                        Size
===============================================================================================================================================================================================
Instalando:
 python-app                                     x86_64                                     0.1.0-1                                      @commandline                                     522 k

Resumo da transação
===============================================================================================================================================================================================
Instalar  1 Pacote

Tamanho total: 522 k
Tamanho depois de instalado: 529 k
Baixando pacotes:
Executando verificação da transação
Verificação de transação completa.
Executando teste de transação
Teste de transação completo
Executando a transação
  Preparando          :                                                                                                                                                                    1/1 
  Instalando          : python-app-0.1.0-1.x86_64                                                                                                                                          1/1 
  Executando scriptlet: python-app-0.1.0-1.x86_64                                                                                                                                          1/1 

>>> Erase old virtualenv.
    + rm -rf /opt/python-app//src/venv


>>> Check virtualenv binary path
    + virtualenv --version > /dev/null 2>&1


>>> Check binary: /bin/virtualenv
    + /bin/virtualenv --python=/usr/local/bin/python3.6 /opt/python-app//src/venv

Already using interpreter /usr/bin/python3.6
Using base prefix '/usr'
New python executable in /opt/python-app/src/venv/bin/python3.6
Also creating executable in /opt/python-app/src/venv/bin/python
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter /usr/bin/python3.6

>>> Activate virtualenv
    + source /opt/python-app//src/venv/bin/activate


>>> Install packages standalone inside virtualenv:
    + /opt/python-app//src/venv/bin/python3.6 -m pip install --quiet --no-index --find-links /opt/python-app//vendor -r /opt/python-app//src/requirements.txt


>>> Deactivate virtualenv after install dependencies
    + deactivate


>>> Create log directories
    + mkdir -p /var/log/python-app/logs/
    + mkdir -p /var/log/python-app/logs/rotated


>>> [!] WARNING [!]
    The uninstall package, dont erase follow directories:
        - /opt/python-app//config
        - /opt/python-app//src/venv


  Verificando         : python-app-0.1.0-1.x86_64                                                                                                                                          1/1 

Instalados:
  python-app-0.1.0-1.x86_64                                                                                                                
```

## Verify Content Files

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

```
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
┌─[auugustoliks]@[localhost]:~/github/demo/python-app
└──> $ 
```

## See python-app running

```
┌─[auugustoliks]@[localhost]:~/github/demo/template-python-app-rpm
└──> $ supervisorctl 
app                              RUNNING   pid 30936, uptime 0:16:16
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

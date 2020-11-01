Name: python-app
Version: %{_VERSION_APP}
Release: %{_VERSION_PKG}
BuildArch: x86_64
Summary: Project for change World
License: Proprietary
Vendor: Github
URL: https://github.com/augustoliks/template-python-app-rpm
Group: Application/Production
Packager: augustoliks <carlos.santos110@fatec.sp.gov.br>
Provides: scripts
# Requires: python3, python3-virtualenv, supervisor, logrotate


%define pkg_root_dir /opt/python-app/

%define source_code_dir %{pkg_root_dir}/src
%define dependencies_dir %{pkg_root_dir}/vendor
%define doc_dir %{pkg_root_dir}/docs
%define config_dir %{pkg_root_dir}/config
%define unit_service_dir /etc/supervisord.d
%define logrotate_dir /etc/logrotate.d


%description
Project for change World.


%prep
rm -rf /tmp/_dependencies
mkdir -p /tmp/_dependencies
cd /tmp/_dependencies
pip3 download -r %{_PROJECT_DIR}/python-app/requirements.txt --no-binary=:none: -d /tmp/_dependencies


%install
mkdir -p $RPM_BUILD_ROOT/%{pkg_root_dir}
mkdir -p $RPM_BUILD_ROOT/%{doc_dir}
mkdir -p $RPM_BUILD_ROOT/%{config_dir}
mkdir -p $RPM_BUILD_ROOT/%{unit_service_dir}
mkdir -p $RPM_BUILD_ROOT/%{logrotate_dir}

cd %{_PROJECT_DIR}

# app
cp -r python-app/ $RPM_BUILD_ROOT/%{source_code_dir}
cp -r /tmp/_dependencies/ $RPM_BUILD_ROOT/%{dependencies_dir}/

# venv
mkdir $RPM_BUILD_ROOT/%{venv_dir}

# app settings
cp pkg/config/python-app.yml $RPM_BUILD_ROOT/%{config_dir}/python-app.yml

# supervisor
cp pkg/supervisor/python-app.ini $RPM_BUILD_ROOT/%{unit_service_dir}/python-app.ini


# logrotate
cp pkg/logrotate/python-app $RPM_BUILD_ROOT/%{logrotate_dir}/python-app


# docs
cp README.md $RPM_BUILD_ROOT/%{doc_dir}
cp VERSION $RPM_BUILD_ROOT/%{doc_dir}


%files
# app
%attr(755, -, -) 
%{source_code_dir}
%{dependencies_dir}

# app settings
%config(noreplace) %{config_dir}/python-app.yml

# supervisor
%attr(755, -, -)
%{unit_service_dir}/python-app.ini

# logrotate
%attr(644, -, -)
%{logrotate_dir}/python-app

# docs
%attr(755, -, -) 
%docdir 
%{doc_dir}


%post
echo "
>>> Erase old virtualenv.
    + rm -rf %{source_code_dir}/venv
"
rm -rf %{source_code_dir}/venv

# Verificando o path do virtualenv

echo "
>>> Check virtualenv binary path
    + virtualenv --version > /dev/null 2>&1
"
virtualenv --version > /dev/null 2>&1

if [ $? == 0 ]; then
    echo "
>>> Check binary: /bin/virtualenv
    + /bin/virtualenv --python=/usr/local/bin/python3.6 %{source_code_dir}/venv
"
    virtualenv --python=/usr/bin/python3.6 %{source_code_dir}/venv
else
    echo "
>>> Check binary: /usr/local/bin/virtualenv
    + /usr/local/bin/virtualenv --python=/usr/local/bin/python3.6 %{source_code_dir}/venv
"
    /usr/local/bin/virtualenv --python=/usr/local/bin/python3.6 %{source_code_dir}/venv
fi

echo "
>>> Activate virtualenv
    + source %{source_code_dir}/venv/bin/activate
"
source %{source_code_dir}/venv/bin/activate

echo "
>>> Install packages standalone inside virtualenv:
    + %{source_code_dir}/venv/bin/python3.6 -m pip install --quiet --no-index --find-links %{dependencies_dir} -r %{source_code_dir}/requirements.txt
"
%{source_code_dir}/venv/bin/python3.6 -m pip install --quiet --no-index --find-links %{dependencies_dir} -r %{source_code_dir}/requirements.txt

echo "
>>> Deactivate virtualenv after install dependencies
    + deactivate
"
deactivate

echo "
>>> Create log directories
    + mkdir -p /var/log/python-app/logs/
    + mkdir -p /var/log/python-app/logs/rotated
"
mkdir -p /var/log/python-app/logs/
mkdir -p /var/log/python-app/logs/rotated


echo "
>>> [!] WARNING [!]
    The uninstall package, dont erase follow directories:
        - %{config_dir}
        - %{source_code_dir}/venv
"

%clean
rm -rf $RPM_BUILD_ROOT

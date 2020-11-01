# {{cookiecutter.project}}

{{cookiecutter.description}}

- __Mainteiner:__ @{{cookiecutter.domain_user_name}} | <{{cookiecutter.author_email}}>
- __Version:__ [Click here](./VERSION)
- __Notas das Versões:__ [Click here](./RELEASE-NOTES.md)


## Project Structure

```shell
├── {{cookiecutter.project}}                # Source Code directory.
│   ├── requirements.txt                    # Dependencies file
│   └── run_{{cookiecutter.project}}.py     # entrypoint executable
├── Makefile                                # Command suite for Test and build RPM 
├── pkg                                     # Directory with config files of internal and external application
│   ├── config                              # Directory Config for "{{cookiecutter.project}}" application
│   │   └── config.yaml                     # config files...
│   ├── logrotate                           # Config for external package "logrotate", Used for compress and rotate log files
│   │   └── {{cookiecutter.project}}        # "{{cookiecutter.project}}" unit config
│   └── supervisor                          # Config for external package "supervisor". Used for run "{{cookiecutter.project}}" like OS background process 
│       └── {{cookiecutter.project}}.ini   # "{{cookiecutter.project}}" unit config
├── README.md                               # Doc project
├── RELEASE-NOTES.md                        # For which Version, explained Authors, Notes and Context. Documentation proposes.
├── rpm.spec                                # Definition file for wrapped application of RPM package format
└── VERSION                                 # Version application. RPM Schema Like.
```

# License

**{{cookiecutter.license}}**

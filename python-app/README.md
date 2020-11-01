# python-app

Project for change World

- __Mainteiner:__ @augustoliks | <carlos.santos110@fatec.sp.gov.br>
- __Version:__ [Click here](./VERSION)
- __Notas das Versões:__ [Click here](./RELEASE-NOTES.md)


## Project Structure

```shell
├── python-app                # Source Code directory.
│   ├── requirements.txt                    # Dependencies file
│   └── run_python-app.py     # entrypoint executable
├── Makefile                                # Command suite for Test and build RPM 
├── pkg                                     # Directory with config files of internal and external application
│   ├── config                              # Directory Config for "python-app" application
│   │   └── config.yaml                     # config files...
│   ├── logrotate                           # Config for external package "logrotate", Used for compress and rotate log files
│   │   └── python-app        # "python-app" unit config
│   └── supervisor                          # Config for external package "supervisor". Used for run "python-app" like OS background process 
│       └── python-app.ini   # "python-app" unit config
├── README.md                               # Doc project
├── RELEASE-NOTES.md                        # For which Version, explained Authors, Notes and Context. Documentation proposes.
├── rpm.spec                                # Definition file for wrapped application of RPM package format
└── VERSION                                 # Version application. RPM Schema Like.
```

# License

**Proprietary**

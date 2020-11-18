# This is a simple Django study project

> In this project we learn to work in a group and actively use VCS to develop a django application

---
## Getting Started

Project runs on Python 3.9 and Django 3.0.7

## Installation

- Clone this repository to your machine
- Install docker

##Commands to launch

* `docker-compose build` - build project from `docker-compose.yml`
* `docker-compose up` - start project

### Automatic setup

- This project will do some basic setup actions during startup. It will generate `private_settings.py` and try to update some database contents from `structure.json`.
- In case you made some changes to the database, which should be represented in `structure.json`, run:

```shell
$ ./manage.py savestructure
```

- You can also run `loadstructure` or `setupproject` but those commands will run automatically on project startup if needed.

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](LICENSE)**

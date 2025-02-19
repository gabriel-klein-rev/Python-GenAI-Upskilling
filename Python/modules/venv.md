# Python Module: venv

> This file details what venv is and how to use it to create virtual development environments.

### Resources

* [venv Python Module](https://docs.python.org/3/installing/index.html#key-terms)
* [Creating Virtual Environments](https://docs.python.org/3/installing/index.html#key-terms)

---

# What Is venv?

`venv` is a Python module that provides support for creating virtual development environments. A *virtual environment* is a Python environment that is isolated from the host system, allowing for packages to be installed only within the scope of particular application.

There are alternatives to venv such as [virtualenv](https://virtualenv.pypa.io/en/latest/), but `venv` is the standard module for creating virtual environments. 

# Using venv To Create Virtual Environments

In order to create a virtual environment using `venv`, a developer should run the following command using their directory of choice:

```
python -m venv [directory]
```

This command marks a directory as a virtual environment by creating a `pyenv.cfg` file and several directories. The file details the version of Python that should be used within the virtual environment, specifies whether or not system-wide packages should be used, and provides other configuration information.

Note, however, that running this command does not start the virtual environment. In order to start the virtual environment, the developer should run the `activate.bat` script in the "Scripts" folder that was created when they ran the first command. Of course, if a developer is not running Windows, the file extension for the script will be different.

```
.\Scripts\activate.bat
```

Once the virtual environment has been activated, run the following command:

```
pip list
```

There should only be a couple of packages installed by default as `venv` automatically installs `pip` and `setuptools` into a virtual environment upon its creation.

In order to install more packages into the virtual environment, use `pip` to install packages from PyPI or other indexes like so:

```
pip install flask
```

This command installs the `flask` package and all of its transitive dependencies into the virtual environment.

When a programmer is finished working in their virtual environment, they would deactivate it like so:

```
.\Scripts\deactivate.bat
```

Once the environment has been deactivated, run `pip list` once again:

```
pip list
```

Look at the list of installed packages and notice that the packages that were only installed in the virtual environment do not exist in the system-wide environment.
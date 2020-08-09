## Python Native Namespace Package Example

In this example, we have a native namespace package, which consists of three sub-modules: [hardware](hardware/), [kernel](kernel/), and [user](user/). We have cross imports in the [controller.py](kernel/controller.py) under kernel sub-module. And we have a executable script outside these sub-modules called [os.py](os.py), which imports [controller.py](kernel/controller.py) from the sub-module [kernel](kernel/).

One thing to note here is the Executable script (eg. os.py here) should not be part of python package. It should be separated file.

### More reading

Python 3.3 added implicit namespace packages from [PEP 420](https://www.python.org/dev/peps/pep-0420). All that is required to create a native namespace package is that you just omit __init__.py from the namespace package directory. An example file structure:

```
    setup.py
    mynamespace/
        # No __init__.py here.
        subpackage_a/
            # Sub-packages have __init__.py.
            __init__.py
            module.py
```

It is extremely important that every distribution that uses the namespace package omits the __init__.py or uses a pkgutil-style __init__.py. If any distribution does not, it will cause the namespace logic to fail and the other sub-packages will not be importable.

When using multiple namespace packages within the same repository:
> Because mynamespace doesn’t contain an __init__.py, setuptools.find_packages() won’t find the sub-package. You must use setuptools.find_namespace_packages() instead or explicitly list all packages in your `setup.py`. For example:

```
  from setuptools import setup, find_namespace_packages

  setup(
      name='mynamespace-subpackage-a',
      ...
      packages=find_namespace_packages(include=['mynamespace.*'])
  )
```

Source: This section is an excerpt quoted from [Python docs: packaging-namespace-packages](https://packaging.python.org/guides/packaging-namespace-packages/)
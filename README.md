# PEP 420 Advanced Example

A [more realistic example](https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages) of [PEP 420 **Implicit Namespace Packages**](https://www.python.org/dev/peps/pep-0420/). Demonstrating a possible layout(s) for a *'core'* application that supports (a) [plugin(s)](https://packaging.python.org/guides/creating-and-discovering-plugins/) *'plug'*.

## Usage during development

Switch to the root folder (*ex1-same-root* or *ex2-diff-root/core-src*). Run the *core* application using `python -m ns_example_pkg`. Since no `__init__.py` is allowed within the namespace folder, the `__main__.py` has to be placed within the namespace package `ns_example_pkg` if you want the actual package to be executable.

### Example 1 - same root folder

In this example submodules are within the same root and namespace folder. Since all submodules - `plug` in this example - share the same root folder, they'll be available as well when started using `python -m ns_example_pkg`. However since `pylint` as well as other tools don't yet fully support the way PEP 420 allows to structure a project they won't be able to resolve the submodules and report some errors which can be ignored. If you want to work around those issues just install the application in editable mode using `pip install -e .`.

### Example 2 - different root folders

In this example submodules are in different root folders. Altought the namespace folder has - and in fact must have - the same name, they are different locations on the local filesystem. This is a typical layout as it would look like if a plugin `plug` is developed by a 3rd party. There are different way how to run this in development. One way would be to simply install the `core` application using plain old `pip install <name-of-core>` to have all dependencies available. But what if you want to work on the `core` source as well while you develop the plugin and make upstream changes? Or what if you're the `core` developer and want to provide a set of default plugins that are loosely coupled?

In that case the structure shown in this example is typical but you won't be able to simply use `python -m ns_example_pkg` because the plugin won't be included in the module search path. For this to work, install all subpackages (plugins) you want to work on using development aka editable mode. Simply switch to the submodules root folder *ex2-diff-root/plug-src* and run `pip install -e .`. This will make the path of the submodule `plug` available in the system's module path. Any changes on the source code of `plug` will be included, no re-install required. Now you can run `python -m ns_example_pkg` from *ex2-diff-root/core-src* just like in [example 1](#example-1---same-root-folder).

## Usage in production

Simply install the application (*core*) and any submodule (*plug*) required using `pip install .`. Once installed the *core* application can be started using `python -m ns_example_pkg` again. When not run from the example root folder, the installed version from system path will be used.

## Real world use

A word of caution: this is still a example to illustrate the use of namespace packages. For real world use you should never make your top-level package a namespace package. Read the [article about namespace packages](https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages) for more details.

## Uninstall

When done with testing, you may uninstall the example package using `pip uninstall ns-example`. If you want to uninstall the *plugin* 'plug', then you have to run `pip uninstall ns-example-plug`. This will work even if `ns-example-plug` was installed in *editable* aka *development* mode. Another way to uninstall *editable* packages without having to specify the name of the package is to run `python setup.py develop -u` within the folder of the corresponding `setup.py`.

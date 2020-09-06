# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Copyright (c) 2019 Robert Ruf
# SPDX-License-Identifier: MIT
# -----------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup, find_namespace_packages
setup(
    # Name used by pip for install / uninstall only. Could be anything
    name="ns-example-plug",
    version="1",
    description="",
    long_description="",
    # Define a "__main__.py" script inside the "ns_example_pkg" folder if
    # you want the "ns_example_pkg" package itself to be executable.

    # Bundle any packages within the namespace package
    # We use the same namespace as for core. When "ns-example-plug" is installed, it"s
    # "plug" subfolder will be placed inside the same "ns_example_pkg" namespace folder
    # inside Pythons site-packages folder and thus can be imported using the same
    # namespace, e.g.: "import ns_example_pkg.plug"
    packages=find_namespace_packages(include=["ns_example_pkg.*"])
)

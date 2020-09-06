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

# Example of a package level import
from ns_example_pkg import core
# Example of a absolute import of an module within the same package
from ns_example_pkg.core import cmod
# Example of a absolute import within the same namespace but from a different package
from ns_example_pkg import plug
# Example of a absolute import of an module within the same namespace but from a different package
from ns_example_pkg.plug import pmod


def main():
    print(core.c_pkg)
    print(core.__path__)
    print(cmod.cmod_var)
    print(cmod.__file__)

    # Same namespace, different package
    print(plug.p_pkg)
    print(plug.__path__)
    print(pmod.pmod_var)
    print(pmod.__file__)

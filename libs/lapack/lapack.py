# -*- coding: utf-8 -*-
import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()
        self.description = "Linear Algebra PACKage."
        self.webpage = "https://www.netlib.org/lapack"
        self.displayName = "lapack"
        self.patchToApply['3.9.0'] = [
            ("0001-Restore-Missing-Prototypes.patch", 1), # https://github.com/Reference-LAPACK/lapack/commit/87536aa3.patch
        ]

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None


from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args = "-DCMAKE_SKIP_RPATH=ON -DBUILD_SHARED_LIBS=ON -DBUILD_TESTING=OFF -DLAPACKE_WITH_TMG=ON -DCBLAS=ON -DBUILD_DEPRECATED=ON"

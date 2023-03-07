# Introduction
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

hydrolib-demotool is a **dummy** example tool to demonstrate how a
HYDROLIB-related modelling tool can be made available as a separate Python
package without needing to be incorporated into the overall hydrolib
package. 

This package will have a dependency on hydrolib-core and may itself be
listed as a dependency in hydrolib.

## Usage
To test correct functioning of this package, use:
```python
import hydrolib_demotool.hello_world as hw

hw.hello_world()
```
## More information

Some quickstarts:
* Releases: [hydrolib-demotool on PyPI](https://pypi.org/project/hydrolib-demotool/), [ChangeLog](changelog.md).
* [HYDROLIB](https://github.com/Deltares/HYDROLIB)
* [HYDROLIB-core](https://github.com/Deltares/HYDROLIB-core)

# Read the Docs testing - subproject

Subproject of: https://github.com/eimrek/rtd-tests

* Hosted: https://eimrek-rtd-tests.readthedocs.io/projects/rtd-tests-subproject
* (Note, the non-sub-project version redirects to this as well: https://rtd-tests-subproject.readthedocs.io)
* `robots.txt`:
  * This project custom one is hosted at https://rtd-tests-subproject.readthedocs.io/robots.txt
  * But it's not used, rather the main project's robots.txt is used. (https://eimrek-rtd-tests.readthedocs.io/robots.txt)

Build docs locally:

```
cd docs
pip install -r requirements.txt
make html
open ./build/html/index.html
```

Rtd page: https://readthedocs.org/projects/rtd-tests-subproject/
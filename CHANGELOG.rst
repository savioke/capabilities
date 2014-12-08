^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Remove faulty start_capability test
* Start capability returns an error code
* Update discovery unit test
* Fix typos in start_capabilities server
* Add test for restarting capabilities
* Export architecture_independent flag in package.xml
* Return an error if requested capability is running
* additional race condition fixes in tests
* try to prevent race condition in tests
* debugging travis only failure
* Contributors: Jon Binney, Scott K Logan, William Woodall

0.2.0 (2014-06-27)
------------------
* downgrade one of the exceptions to a warning
* fixup tests to reflect changes to client API
* Increase queue_size to 1000 for publishers
* Add queue_size arg for all publishers
* change exception behavior for use/free_capability in client API
* A rosdistro agnostic documentation reference
* conditionally try to stop reverse deps, since other reverse deps may have already stopped it
* make stopping the launch manager more robust to errors
* adds support of namespaces for capability nodelets
* Contributors: Jon Binney, Marcus Liebhardt, Nikolaus Demmel, William Woodall, kentsommer

0.1.1 (2014-05-02)
------------------
* Add entry in setup.py to install package data
* Fixed up testing
* Updates link to API doc
* Contributors: Marcus Liebhardt, William Woodall

0.1.0 (2014-04-15)
------------------
* First release
* Contributors: Esteve Fernandez, Marcus Liebhardt, Tully Foote, William Woodall

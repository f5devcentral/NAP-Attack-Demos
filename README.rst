WAF Test Plan
=============

Each directory will correspond to the attack type used to exploit the application we want to protect.
Each directory will contain test client vectors triggering the correponding attack type, in addition to the App Protect policy used to mitigate the attack. 

Prerequisites
~~~~~~~~~~~~~

- NGINX App Protect Version 4

- A backend application (We use the juicebox application for testing)

Topology
~~~~~~~~


.. image:: ./images/WAF_JuiceShop.png







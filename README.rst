WAF Test Plan
=============

Each directory will correspond to the attack type used to exploit the application we want to protect.
Each directory will contain test client vectors triggering the correponding attack type, in addition to the App Protect policy used to mitigare the attack. 

<h2>Prerequisites</h2>
- NGINX App Protect verion 4 <br>
- A backend application (We use the juicebox application for testing)<br>

Topology
~~~~~~~~

.. image:: ./images/WAF_JuiceShop.png







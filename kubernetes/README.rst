Deploying App Protect in Kubernetes
===================================

You can deploy NGINX App Protct in a standalone container or in Kubernetes. 

Prerequisites
~~~~~~~~~~~~~

-Docker or Kubectl installed on your machine. 


Deploying NAPv4 in Kubernetes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the napv4-deploy bash script

.. code:: shell 

	/bin/bash napv4-deploy <nginx-license-crt> <nginx-license-key> <nginx-license-jwt>


Verify the deployment is running 

.. code:: shell

	kubectl get pods -o wide -n nginx-plus


Applying NGINX App Protect Policies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference a policy from an attack-type directory and mount it inside the container. 

.. code:: shell

	cp Brute_Force_Attack/BruteForceAttack.json /etc/app_protect/conf 


.. image:: ./images/nginx_config.png

 
Reload NGINX Plus

.. code:: shell

	nginx -s reload

DONE
~~~~




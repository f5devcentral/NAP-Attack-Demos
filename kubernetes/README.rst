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

Deploy the juicebox application in Kubernetes 

.. code:: shell
	
        kubectl apply -f juicebox.yaml


Applying NGINX App Protect Policies and NGINX configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modify the nginx.conf file and run the apply_policy script with the policy file you wish to apply. 

.. code:: shell

	sudo /bin/sh apply_policy <policy-file.json>

DONE
~~~~


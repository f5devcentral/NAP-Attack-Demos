Deploying App Protect with Agent in Kubernetes
===================================

You can deploy NGINX App Protect in a standalone container or in Kubernetes. 

Prerequisites
~~~~~~~~~~~~

-Docker or Kubectl installed on your machine. 


Deploying NAPv4 in Kubernetes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the napv4-deploy bash script

.. code:: shell 

	/bin/bash napv4-deploy <nginx-license-crt> <nginx-license-key> <nginx-license-jwt>


Verify the deployment is running 

.. code:: shell

	kubectl get pods -o wide -n nginx-plus

Deploy the juicebox application in Kubernetes 

.. code:: shell
	
        kubectl apply -f juicebox.yaml


Make Config Changes from the NGINX One SaaS Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


DONE
~~~


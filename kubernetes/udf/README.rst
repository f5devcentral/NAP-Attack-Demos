F5 WAF for NGINX in Kubernetes
==============================

Each directory will correspond to the attack type used to exploit the application we want to protect.
Each directory will contain test client vectors triggering the correponding attack type, in addition to the App Protect policy used to mitigate the attack. 

Prerequisites
~~~~~~~~~~~~~
- F5 WAF for NGINX Plus Ingress Controller
- A backend applications (We will segment WAF polcies with three application deployments)

Topology
~~~~~~~~

In this lab, we will explore two topologies. The first topology demonstrates F5 WAF policy segmentation by 
Virtual Server (FQDN), where each application deployment is safeguarded by a dedicated WAF policy. We will 
run 2 application deplpoyments (JuiceShop and external-authz python application)

.. image:: ./images/VS-F5-WAF.png


The second topology focuses on segmenting WAF policies by path URI rather than by Virtual Server (FQDN). This approach provides stricter policy segmentation, requiring application owners to expose only Layer 7 routes within the cluster. Unique WAF policies can then be applied directly to these specific routes.

.. image:: ./images/VSR-WAF.png


Getting Started with the BIG-IP
===============================
.. note::
   These next steps will guide you through reviewing the LTM policy for routing all traffic to the cluster. Nothing will be provioned for the
   BIG-IP in this lab.

   You will be using the BIG-IP in the TMUI   

1. Open your browser tab with the BIG-IP GUI and sign in using the BIG-IP username and password

**Username: admin**

**Password: F5site02@**


.. image:: ./images/BIG-IP-Login.png

2. You should be logged into the BIG-IP now, switch to the AS3 context and navigate to Local Traffic > 
Virtual Server. You should see the serviceMain virtual server in green status.

.. image:: ./images/Virtual-Server-ServiceMain.png


3. Navigate to Pools and select web_pool, then select the members tab. As we are running BIG-IP in NodePort mode, the pool members correspond to the Kubernetes cluster nodes, while the ports map to the NodePort of the service being exposed—in this case, the NGINX Ingress Controller. We will confirm this configuration after setting up the NGINX Ingress Controller in Kubernetes. 

.. image:: ./images/Pool-Members.png

Setting up F5 WAF with NGINX Ingress Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will be setting up our Kubernetes cluster from kube-master1.
SSH >> kube-master1 

First lets verify that F5 NGINX Ingress Controller is running in our cluster. 

.. code:: shell
	kubectl get pods -o wide -n nginx-ingress
	kubectl describe pod $(kubectl get pod -l app=nginx-ingress -n nginx-ingress -o jsonpath={.items..metadata.name}) -n nginx-ingress | grep Image

The output indicates the image we are deploying must include F5 WAF with NGINX Plus Ingress Controller. 
Now we will check the NodePort service exposing NGINX Ingress Controller.

.. code:: shell 
	kubectl get svc -o wide -n nginx-ingress

The NodePort of the service will align with the pool members configured in BIG-IP.

Deploying the Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we will deploy the juiceshop and ext-authz application

.. code:: shell
	kubectl create -f ~/agilitydocs/docs/class1/kubernetes/app-protect-waf/NAP-Attack-Demos/kubernetes/juiceshop.yaml
	kubectl create -f ~/agilitydocs/docs/class1/kubernetes/app-protect-waf/NAP-Attack-Demos/kubernetes/apps/deployment.yaml

Verify the applications are runnning

.. code::shell 
	kubectl get pods -o wide


Now expose both applications with the NGINX VirtualServer CRDs

.. code::shell 
	kubectl ~/agilitydocs/docs/class1/kubernetes/app-protect-waf/virtual-server-ext-authz.yaml
	kubectl ~/agilitydocs/docs/class1/kubernetes/app-protect-waf/virtual-server-juiceshop.yaml

Verify that the VirtualServer CRDs are applied correctly and valid

.. code::shell
	kubectl get virtualservers.k8s.nginx.org 

Running the Firefox Browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

Initiating the firefox browser will require to SSH into the provisioner. If you are using webshell, run "su -- cloud-user".

Now you can open firefoc from the ocp-provisioner component

 


Run the client attack script inside the attack type directory. For example, run the brute force attack.

.. code:: shell 

	cd Brute_Force_Attack
	/bin/bash client_attacks <NGINX-ENDPOINT>


Applying NGINX App Protect Policies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference the policy inside the nginx config.

.. code:: shell

	cp Brute_Force_Attack/BruteForceAttack.json /etc/app_protect/conf 


.. image:: ./images/nginx_config.png

 
Reload NGINX Plus

.. code:: shell

	nginx -s reload

DONE
~~~~


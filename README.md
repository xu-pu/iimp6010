# IIMP6010 TA Material



## Cloud Based Setup

How to setup and administrate JupyterHub for the course



### Step-by-step tutorial for setting up a JupyterHub Cloud

1. Choose a cloud service provider, such as Linode, AWS, Alibaba. Make sure mainland students can access the service. I will use [DigitalOcean](https://www.digitalocean.com/) as an example.

2. Choose a plan for your cloud server. Each student will need 100-300MB of memeory when running the JupyterNotebook. (!!TODO enble swap)

3. Create the cloud server.

4. Take note of the public ip address, SSH into the server `ssh root@xxx.xxx.xxx.xxx`. 

   Perform step 5 and 9 on the server through SSH. 

5. Install [The Littlest JupyterHub (TLJH)](https://github.com/jupyterhub/the-littlest-jupyterhub) on your server uisng the following commands. 

   ```shell
   sudo apt install python3 python3-dev git curl
   curl -L https://tljh.jupyter.org/bootstrap.py | sudo -E python3 - --admin teach
   ```

   This step will take a while to finish. It might fail if your server do not have enough RAM, make sure there is at least 2GB RAM on your server. More details can be found in its [official tutorial](https://tljh.jupyter.org/en/latest/install/custom-server.html). 

   It will also create an admin user `teach`. 

6. Go to the browser, enter the server's IP address. JupyterHub should open. If not, check the previous steps.  

7. Sign-in with the user name `teach` and a safe password. __The password is set to the one you entered on your first login.__

8. Register a domain name, and point it to the server IP. 

   For example, I registered [iimp6010.io](https://iimp6010.io) and [iimp6010.com](https://iimp6010.com) on [GoDaddy](godaddy.com).

9. Enable your domain names and HTTPS using the following commands. 

   ```shell
   sudo tljh-config set https.enabled true
   sudo tljh-config set https.letsencrypt.email you@example.com
   sudo tljh-config add-item https.letsencrypt.domains your_domain_name.com
   ```

   More details can be found in the [official totorial](https://tljh.jupyter.org/en/latest/howto/admin/https.html#howto-admin-https).

10. Try access the JupyterHub in your browser using your domain name and HTTPS.



### Administration Q&A



##### Q: Can I open terminal in JupyterHub?

A: Yes. In addtion, users with admin priviliges can also `sudo`.

![open-terminal](https://tljh.jupyter.org/en/latest/_images/new-terminal-button2.png)

##### Q: How to add and remove users?

A: Control Panel / Admin / Add Users



##### Q: How to install packages?

A: Open terminal and type the following command. [offical guide](https://tljh.jupyter.org/en/latest/howto/env/user-environment.html)

```shell
sudo -E conda install -c conda-forge networkx
```



##### Q: How to change passwords?

A: Delete and recrate the user. Delete the user won't do anything to the files. 



## Local Setup

It is recommanded for students to use the JupyterHub, but they can also setup locally.



### Linux (Ubuntu)



### MacOS 



### Windows 10



## `iimp6010.py` 

`iimp6010.py` contains code utilities for this course. Its primary features are

- Generate, save, load  and visualize 'cities'
- Visualization and animation utilities
- Course specific utilities

It will be preinstalled globally and read-only on the JupyterHub, students can also download it if they want to have a local setup.

# IIMP6010 TA Material

This repo is for the teaching team of IIMP6010 - 2020 Fall, it contains: 

- Development environment setup tutorials for the IIMP6010 course. 
  - Cloud based JupyterHub (Recommanded)
  - Local setup for Ubuntu/MacOS/Windows10 (Optional)
- `iimp6010.py` python module and its documentation 
- Tutorials for python, `networkx` and other knowlege required by the course.



__Table Of Content__

- [Cloud Based Setup](#jupyter)
  - [Step-by-step tutorial for setting up a JupyterHub Cloud](#server)
  - [Administration Q&A](#admin)
- [Local Setup](#local)
  - [Linux(Ubuntu)](#ubuntu)
  - [MacOS](#mac)
  - [Windows 10](#win)
- [iimp6010.py](#code)



<a name="jupyter">

## Cloud Based Setup

Here we document how to setup and administrate JupyterHub for the course. The _Step-by-step tutorial for setting up a JupyterHub Cloud_ is only for those who want to setup their own server, skip it if you just want to use [iimp6010.io](https://iimp6010.io).



<a name="server">

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



<a name="admin">

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



##### Q: How to send file to every student?

A: !!TODO



<a name="local">

## Local Setup

It is recommanded for students to use the JupyterHub, but they can also setup locally.



<a name="ubuntu">

### Linux (Ubuntu)

1. Download the [installer](https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh), save it to your home directory.

2. Install [Anaconda](https://www.anaconda.com/) using the following commands

   ```shell
   cd ~/
   chmod +x Anaconda3-2020.07-Linux-x86_64.sh
   ./Anaconda3-2020.07-Linux-x86_64.sh
   ```

   During installation:

   1. Type `yes` to the terms and conditions

   2. Press `Enter` to use default location when asking for installation location

   3. Type `yes` when the following promt appears

      ```
      Do you wish the installer to initialize Ananconda3
      by running conda init? [yes|no]
      ```

3. Open terminal, type `python`, check the python version is 3.8.3.

4. Install packages used by our course. Open terminal and type:

   ```shell
   conda install -c conda-forge networkx pandas matplotlib
   ```

5. type `spyder` in terminal. It is our recommended development environment.



<a name="mac">

### MacOS 

1. Install [Anaconda](https://www.anaconda.com/) using the [graphical installer](https://repo.anaconda.com/archive/Anaconda3-2020.07-MacOSX-x86_64.pkg).

2. Install packages used by our course. Open Terminal and type:

   ```shell
   conda install -c conda-forge networkx pandas matplotlib
   ```

3. Open the `Anaconda Navigator` App.

4. Click and open `Spyder`, It is our recommended development environment.

5. Write code.



<a name="win">

### Windows 10

1. Install [Anaconda](https://www.anaconda.com/) using the [graphical installer](https://repo.anaconda.com/archive/Anaconda3-2020.07-Windows-x86_64.exe).



<a name="code">

## `iimp6010.py` 

`iimp6010.py` contains code utilities for this course. Its primary features are

- Generate, save, load  and visualize 'cities'
- Visualization and animation utilities
- Course specific utilities

It will be preinstalled globally and read-only on the JupyterHub, students can also download it if they want to have a local setup.

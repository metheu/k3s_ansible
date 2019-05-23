## Simple ansible playbook to lauch k3s cluster in vagrant 
#### This playbook automatically creates a server k3s with --no-deploy trafeik and agents that bind automatically to the server

## How to
* Vagrant lauches the machines bridged to 'wlp1s0' network. You need to change the machines ip to your local subnet, then run ```vagrant up```
* In ```hosts.ini``` change the coresponding ip addresses. 
* Change ```k3s_server_ip``` in k3s_agent role to point to server ip
* Then run the playbook with ```ansible-playbook deployK3sCluster.yml -i hosts.ini --key-file k3sKey```

#### Currently supported platforms:
* Systems running systemd
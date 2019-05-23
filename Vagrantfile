# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
    config.vm.provision "shell", inline: <<-SHELL
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDjGVP2EzD100Y/wLB6vVz7iBMPb8auvXf6XcYYqMXnnBYwZkUfqlGEr4SKCH4IJfploH/66cHTgR4qFxwEElE6dssLcH3sasxtpPlrDK/m6ZdP+pdpqcJlcIVnwOSfvR6BzE66psOOPrGj0NpMUj/fUNetNw/aNJuh1/yuLEcc1kPcyadHGQtrf66Tetk4NMyVC8lXBcRK15FFJY83PwfwloIUn/9T1c8+2bDlaE31iDe6KisxzzTUwensoCYsTjAuRrRdhPkvWaQg9VSGDTquNIHqaytJJLlNKSoC8XxmaBTujHQ9UeUt20YE+nK9cgZdv7Dz7uXZtlWcF/eXBQ6t matt@localhost.localdomain" >> /home/vagrant/.ssh/authorized_keys
    sudo systemctl restart sshd.service
    SHELL

    # config.vm.provision "shell", inline: <<-SHELL
    # wget https://github.com/rancher/k3s/releases/download/v0.5.0/k3s -O /home/vagrant/k3s && sudo mv -v /home/vagrant/k3s /usr/bin/ && sudo chmod +x /usr/bin/k3s
    # SHELL
  
    config.vm.define "k3sMaster" do |m|
      m.vm.box = "bento/centos-7.5"
      m.vm.hostname = 'k3sMaster'
      
    
      m.vm.network :"public_network", bridge: "wlp1s0", ip: "192.168.0.200"
    
      m.vm.provider :virtualbox do |v|
        v.customize ["modifyvm", :id, "--memory", 1048]
        v.customize ["modifyvm", :id, "--name", "k3sMaster"]
      end
    end

    config.vm.define "k3sNode" do |m|
      m.vm.box = "bento/centos-7.5"
      m.vm.hostname = 'k3sNode'
      
    
      m.vm.network :"public_network", bridge: "wlp1s0", ip: "192.168.0.201"
    
      m.vm.provider :virtualbox do |v|
        v.customize ["modifyvm", :id, "--memory", 1048]
        v.customize ["modifyvm", :id, "--name", "k3sNode"]
      end
    end
  end
  
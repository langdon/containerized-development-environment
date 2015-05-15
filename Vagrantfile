Vagrant.configure(2) do |config|
#https://github.com/LalatenduMohanty/centos7-container-app-vagrant-box
  config.vm.box = "atomicapp/dev"
  config.vm.define :local_dev_env do | host |
    host.vm.hostname = "containerapp-drupal"
    host.vm.synced_folder ".", "/vagrant", disabled: true
    #need to figure out how to do a separate disk store or, even better, a docker storage container, for, at least, docker registry backing
#    host.vm.synced_folder ".", "/mnt/vagrant", type: "rsync",
#                          rsync__exclude: [ ".git/", ".#*", "*~" ]
    host.vm.provision 'shell', inline: "sudo yum -y install nfs-utils libyaml-devel PyYAML tree" #in case this isn't first run
    host.vm.provision 'shell', inline: "sudo mkdir /mnt/host-projects/ > /dev/null 2>&1 || :" #in case this isn't first run
    host.vm.provision 'shell', inline: "sudo umount /mnt/host-projects/ > /dev/null 2>&1 || : && sudo mount.nfs -v 192.168.100.1:/mnt/nbu/loc-projects /mnt/host-projects/"
    host.vm.provision 'shell', inline: "/home/vagrant/sync/docker-registry-store/run-registry.sh"

    config.vm.provider :libvirt do |domain|
      domain.memory = 512
      domain.cpus = 1
    end
  end
end

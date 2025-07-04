Vagrant.configure("2") do |config|
    
    config.vm.define "main_server" do |main_server|
        main_server.vm.box = "ubuntu/xenial64"
    end
  
    config.vm.define "db" do |db|
        db.vm.box = "ubuntu/xenial64"
        db.vm.network :private_network, ip:"192.168.61.11"
    end

end
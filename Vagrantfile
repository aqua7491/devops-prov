Vagrant.configure("2") do |config|
    config.ssh.host = "192.168.102.75"

    # Global provider configuration (applies to all VMs)
    config.vm.provider "virtualbox" do |vb|
        vb.gui = true
        vb.customize ["modifyvm", :id, "--uart1", "off"]
        vb.customize ["modifyvm", :id, "--uartmode1", "disconnected"]
    end

    config.vm.define "main_server" do |main_server|
        main_server.vm.box = "ubuntu/jammy64"
        main_server.vm.network :forwarded_port, guest: 22, host: 2522, auto_correct: false, id: "ssh"
        main_server.vm.boot_timeout = 600
        
    end

end

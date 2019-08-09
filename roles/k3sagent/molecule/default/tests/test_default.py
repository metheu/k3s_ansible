import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_k3s_binary_installed(host):
        k3s_binary = host.file("/usr/local/bin/k3s").exists

        assert k3s_binary
    
    
def test_k3s_svc(host):
        k3s_svc = host.service("k3s")
    
        assert k3s_svc.is_running
        assert k3s_svc.is_enabled


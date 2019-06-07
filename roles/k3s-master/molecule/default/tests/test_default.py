import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_k3s_binary_installed(File):
    k3s = File("/usr/local/bin/k3s")
    assert k3s.exists


@pytest.mark.parametrize('svc', [
    'k3s'
])
def test_k3s_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled

import ansible.playbook
from ansible import callbacks
from ansible import utils
ANSIBLE_HOSTS = 'hosts'
PLAYBOOK = 'keypair.yml'
def deploy():
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    inventory = ansible.inventory.Inventory(ANSIBLE_HOSTS)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats,verbose=utils.VERBOSITY)

    pb = ansible.playbook.PlayBook(playbook=PLAYBOOK,
                                   callbacks=playbook_cb,
                                   runner_callbacks=runner_cb,
                                   stats=stats, 
                                   inventory=inventory,
                                   extra_vars={'name': "AAA"})
    pb.run()

if __name__ == "__main__":
    deploy()

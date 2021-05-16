# ログイン後に http://...:8000/user/<username>/lab? へ遷移する設定（Jupyterlabが起動）
c.Spawner.default_url = '/lab'
# Jupyterlabで作成されたノートブックファイルなどが格納されるディレクトリ
c.Spawner.notebook_dir = '/home/jovyan/share'
# adminユーザのユーザ名
c.Authenticator.admin_users = {'testadmin'}
# ログインが許可されているユーザ名
c.Authenticator.allowed_users = {'testuser01'}

c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'

import pwd, subprocess
def pre_spawn_hook(spawner):
    username = spawner.user.name
    try:
        pwd.getpwnam(username)
    except KeyError:
        print('pre_spawn_hook {}'.format(username))
        subprocess.check_call(['sh', '/home/jovyan/bootstrap/bootstrap.sh', username])

c.Spawner.pre_spawn_hook = pre_spawn_hook

from dockerspawner import DockerSpawner
import os, grp

notebook_dir = '/home/jovyan/work'

class MyDockerSpawner(DockerSpawner):
    def start(self):
        name = self.user.name
        self.volumes['/home/jovyan/share/'.format(name)] = notebook_dir + '/personal'
        self.volumes['/home/jovyan/share/data'] = notebook_dir + '/data'
        return super().start()

c.JupyterHub.spawner_class = MyDockerSpawner
c.DockerSpawner.image = 'hub/single_notebook'
c.DockerSpawner.remove_containers = True

c.DockerSpawner.network_name = 'jupyterhub-docker-simple_default'

from jupyter_client.localinterfaces import public_ips
c.DockerSpawner.hub_ip_connect = public_ips()[0]
c.DockerSpawner.notebook_dir = notebook_dir

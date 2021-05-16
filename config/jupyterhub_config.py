# ログイン後に http://...:8000/user/<username>/lab? へ遷移する設定（Jupyterlabが起動）
c.Spawner.default_url = '/lab'
# Jupyterlabで作成されたノートブックファイルなどが格納されるディレクトリ
c.Spawner.notebook_dir = '~/notebook'
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
        subprocess.check_call(['sh', '/home/jovyan/bootstrap/bootstrap.sh', username])

c.Spawner.pre_spawn_hook = pre_spawn_hook

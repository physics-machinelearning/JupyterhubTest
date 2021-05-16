adduser -q --gecos '""' --disabled-password $1
mkdir -p -m 777 /home/jovyan/share/$1
chown $1: /home/jovyan/share/$1
chown $1: /home/jovyan/share/data
cat /home/jovyan/share
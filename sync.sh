#script for syncing backup tanks

rsync -rv --ignore-existing /tank0 /tank2
rsync -rv --update /tank0 /tank2

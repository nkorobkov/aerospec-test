APPNAME=aerospec
APPDIR=/home/ec2-user/aero-project/aerospec

LOGFILE=$APPDIR'gunicorn.log'
ERRORFILE=$APPFIR'gunicorn-error.log'

NUM_WORKERS=3

ADDRESS=unix:/tmp/gunicorn.sock

DJANGO_MODE=PROD


cd $APPDIR

source ~/aero-project/env/bin/activate

exec gunicorn $APPNAME.wsgi:application \
-w $NUM_WORKERS --bind=$ADDRESS \
--log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE &
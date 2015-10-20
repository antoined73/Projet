import time

__author__ = 'KerTakanov'

ENABLE_LOG = True

INFO = '[INFO]'
WARNING = '[WARNING]'
ERROR = '[ERROR]'
FATAL_ERROR = '[FATAL ERROR]'

LOGPATH = 'logs/'
prgmid = time.strftime("%y_%m_%d_%H-%M-%S", time.gmtime())

FILENAME = LOGPATH + 'log_' + prgmid + ".log"


def write(*line):
    if ENABLE_LOG:
        logfile = open(FILENAME, 'a')
        logfile.write(str().join([time.strftime("[%H:%M:%S]", time.gmtime()), str().join(line), '\n']))
        logfile.close()


def info(*info):
    write(INFO, ' ', str().join(info))


def warning(*warning):
    write(WARNING, ' ', str().join(warning))


def error(*error):
    write(ERROR, ' ', str().join(error))


def fatal_error(*fatal_error):
    write(FATAL_ERROR, ' ', str().join(fatal_error))

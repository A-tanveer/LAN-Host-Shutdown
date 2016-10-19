# For Host PC's. running this script will give permission for remote shutdown
# need to allow    in firewall
import win32serviceutil


def service_info(action, machine, service):
    if action == 'stop':
        if win32serviceutil.QueryServiceStatus(service, machine)[1] == 4:
            win32serviceutil.StopService(service, machine)
            v = service + ' stopped successfully.'
            print(v)
        else:
            v = service + ' is not running.'
            print(v)
    elif action == 'start':
        if win32serviceutil.QueryServiceStatus(service, machine)[1] == 4:
            v = service + ' is running.'
            print(v)
        else:
            win32serviceutil.StartService(service)
            v = service + ' started successfully.'
            print(v)
    elif action == 'restart':
        win32serviceutil.RestartService(service, machine)
        v = service + ' restarted successfully.'
        print(v)
    elif action == 'status':
        if win32serviceutil.QueryServiceStatus(service, machine)[1] == 4:
            v = service + ' is running normally.'
            print(v)
        else:
            v = service + ' is not running.'
            print(v)


if __name__ == '__main__':
    machine = 'TanveerPC'
    service = 'RemoteRegistry'
    action = 'start'
    # os.system("sc config " + service + " start= Automatic")
    service_info(action, machine, service)

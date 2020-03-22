from Jumpscale import j
import click

@click.command()
@click.option('-l','--all', is_flag=True, default = False, help='display service on all running ports')
@click.option('-t','--tcp', is_flag=True, default = False, help='display service running tcp connection')
@click.option('-u','--udp', is_flag=True, default = False, help='display service running udp connection')
@click.option('-p','--pid', is_flag=True, default = False, help='display service name with pID')
@click.option('-s','--statistics', is_flag=True, default = False, help='display network statistcs')

def net_stat(all,tcp,udp,pid,statistics):
    """
    netstat script
    """

    ip_address = j.sal.nettools.getIpAddress()['ip'][0] # ip
    running_ports = j.sal.nettools.getRunningPorts()   #[(port,process name),]
    ports_details = {}

    for port in running_ports:

        if j.sal.nettools.tcpPortConnectionTest(ip_address,port[0]):
            ports_details.setdefault(str(port[0]),[]).append('tcp')
        elif j.sal.nettools.udpPortConnectionTest(ip_address,port[0]):
            ports_details.setdefault(str(port[0]),[]).append('udp')
        else:
            ports_details.setdefault(str(port[0]),[]).append('')

        ports_details[str(port[0])].append(port[1])

        process = j.sal.process.getProcessPid(str(port[1]))
        ports_details[str(port[0])].append(process or '')

    def print_line(*args):
        print(('{:>15}' * len(args)).format(*args))

    if all:
        print_line('Proto','port','process')
        for value in ports_details:
            if ports_details[value][0] != '':print_line(ports_details[value][0],value,ports_details[value][1])

    elif tcp:
        print_line('Proto','port','process')
        for value in ports_details:
            if ports_details[value][0]=='tcp': print_line(ports_details[value][0],value,ports_details[value][1])

    elif udp:
        print_line('Proto','port','process')
        for value in ports_details:
            if ports_details[value][0]=='udp':print_line(ports_details[value][0],value,ports_details[value][1])
    elif pid:
        print_line('Proto','port','process','pid')
        for value in ports_details:
            if ports_details[value][0] != '': print_line(ports_details[value][0],value,ports_details[value][1],ports_details[value][2])

    elif statistics:
        ckick.echo(j.sal.nettools.networkinfo_get())

if __name__ == '__main__':
    net_stat()
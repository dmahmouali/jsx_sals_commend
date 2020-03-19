from Jumpscale import j
import click

@click.command()
@click.option( '--id', help='select by process ID')
@click.option('--ppid',  help='select py parent process ID')
@click.option('--name',  help='check if process name is true')
@click.option('--port',  help='select by port number')
@click.option('--fstr',  help='select by string matching')
@click.option('--all', is_flag=True, default = False, help='select all')

def process_control(id:int,ppid:int, name:str,port:int,fstr:str,all:bool) -> None:
    """
    process control script
    """
    
    if id:
        click.echo(j.sal.process.getProcessPid(id))
    elif ppid:
        click.echo(j.sal.process.execute('ps -ppid '+ppid))
    elif name:
        click.echo(j.sal.process.psfind(name))
    elif port:
        click.echo(j.sal.process.getProcessByPort(port))
    elif fstr:
        click.echo(j.sal.process.getPidsByFilter(filterstr=fstr))
    elif all:
        click.echo(j.sal.process.execute('ps ax'))
    else:
        click.echo(j.sal.process.getMyProcessObject())

if __name__ == "__main__":
    process_control()
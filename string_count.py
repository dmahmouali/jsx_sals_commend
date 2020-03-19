from Jumpscale import j
import click

#j.sal.process.execute('')


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option("-w", is_flag=True, default = False, help="count words")
@click.option("-l", is_flag=True, default = False, help="count lines")
@click.option("-c", is_flag=True, default = False, help="count chars")
@click.option("--max", is_flag=True, default = False, help="Maximum line width")

def net_stat(path:str, w:bool,l:bool,c:bool,max:bool) -> None:
    """
    word count script
    """
    #check isfile
    #j.debug()
    if not j.sal.fs.isFile(str(path)):
        print("not file")
        return
    cmd = 'wc '
    if(w): cmd += '-w '
    if(l): cmd += '-l '
    if(c): cmd += '-c '
    if(max): cmd += '-L '
    click.echo(j.sal.process.execute(cmd+path))

if __name__ == '__main__':
    net_stat()
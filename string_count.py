from Jumpscale import j
import click

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option("-w", is_flag=True, default = False, help="count words")
@click.option("-l", is_flag=True, default = False, help="count lines")
@click.option("-c", is_flag=True, default = False, help="count chars")
@click.option("--max", is_flag=True, default = False, help="Maximum line width")

def strin_count(path:str, w:bool,l:bool,c:bool,max:bool) -> None:
    """
    word count script
    """

    if not j.sal.fs.isFile(str(path)):
        raise ValueError("path is not correct or not file...")
        
    cmd = 'wc '
    if(w): cmd += '-w '
    if(l): cmd += '-l '
    if(c): cmd += '-c '
    if(max): cmd += '-L '
    exitcode, output, err = j.sal.process.execute('%s %s'%(cmd,path))

if __name__ == '__main__':
    strin_count()
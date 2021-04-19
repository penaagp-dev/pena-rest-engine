"""
Usage:
  pena <command> [<args>...]

Options:
  -h, --help                             Display this help and exit
  -v, --version                          Print version information and quit

Commands:
  http                                 Starting http serve
  migrate                              Migrating apps
  deploy                                Setup apps

Run 'pena COMMAND --help' for more information on a command.
"""
from src import __version__ as VERSION
from inspect import getmembers, isclass
from docopt import docopt, DocoptExit
from src.config import config

def main():
    """Main CLI entrypoint."""
    config()
    import src.cmd
    try:
      options = docopt(__doc__, version=VERSION, options_first=True)
      command_name = ""
      args = ""
      command_class =""

      command_name = options.pop('<command>')
      args = options.pop('<args>')

      if args is None:
          args = {}
      
      try:
        module = getattr(src.cmd, command_name)
        src.cmd = getmembers(module, isclass)
        command_class = [
            command[1] for command in src.cmd if command[0] != 'Base'
        ][0]
      except AttributeError as e:
          print(e)
          raise DocoptExit()

      command = command_class(options, args)
      command.execute()
    except AttributeError as e:
      print(__doc__)
    


if __name__ == '__main__':
    main()


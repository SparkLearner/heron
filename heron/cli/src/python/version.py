# Copyright 2016 Twitter. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
''' version.py '''
import heron.cli.src.python.args as cli_args
import heron.common.src.python.utils.config as config


def create_parser(subparsers):
  '''
  :param subparsers:
  :return:
  '''
  parser = subparsers.add_parser(
      'version',
      help='Print version of heron-cli',
      usage="%(prog)s",
      add_help=False)

  cli_args.add_titles(parser)

  parser.set_defaults(subcommand='version')
  return parser


# pylint: disable=unused-argument
def run(command, parser, args, unknown_args):
  '''
  :param command:
  :param parser:
  :param args:
  :param unknown_args:
  :return:
  '''
  release_file = config.get_heron_release_file()
  with open(release_file) as release_info:
    for line in release_info:
      print line,

  return True

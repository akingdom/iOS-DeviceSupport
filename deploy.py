#!/usr/bin/env python
import argparse
import zipfile
from os import listdir, path

SRC = path.join(path.dirname(path.abspath(__file__)), 'DeviceSupport')
DEVICE_SUPPORT_PATH='Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport'

def unzip_file(name, target):
  f = path.join(SRC, name + '.zip')
  zip_ref = zipfile.ZipFile(f, 'r')
  zip_ref.extractall(target)
  zip_ref.close()

def process(xcode, version, listing):
  target = path.join(xcode, DEVICE_SUPPORT_PATH)
  exist = listdir(target)
  all_files = [i.replace('.zip', '') for i in listdir(SRC) if i.endswith('.zip')]
  new_files = list(set(all_files) - set(exist))

  if version:
      new_files = list(filter(lambda x : version in x, new_files))

  if listing==True:
    for i in new_files:
      print ('LIST| file "{}.zip" to {}'.format(i, target))
    print ('\nNo files were copied for {}'.format(xcode))
  else:
    for i in new_files:
      print ('Unzip file "{}.zip" to {}'.format(i, target))
      unzip_file(i, target)
    print ('\nUpdate successfully for {}'.format(xcode))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-t',
    type=str,
    dest='target',
    default='/Applications/Xcode.app',
    help='The path for Xcode'
  )
  parser.add_argument(
    '-v',
    type=str,
    dest='version',
    default=None,
    help='Specific version (default is all)'
  )
  parser.add_argument(
    '-l',
    type=str,
    nargs='?',
    dest='listing',
    default=argparse.SUPPRESS,
    help='List only without copying any files (default is to copy)'
  )
  args = parser.parse_args()
  process(args.target, args.version, 'listing' in args)

#! /usr/bin/env python
#-*- coding:utf-8 -*-

# Copyright 2018-  <linrongbin16@gmail.com>

import sys
import os
sys.path.append('.')
import util

msg_list = [
        "Brief:",
        "    git pull",
        "Usage:",
        "    %s" % util.command_name(),
        "Try again"]

util.check_help(msg_list)
util.check_repository()

if len(sys.argv) != 1:
    util.help_msg(msg_list)

branch = util.repository_branch()
print("[lin-vim] git pull on '%s', path: '%s'" % (branch, os.getcwd()))
os.system('git pull')
os.system('git pull --tags')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2009 Zuza Software Foundation
# 
# This file is part of Pootle.
#
# Pootle is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# Pootle is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pootle; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from pootle_app import project_tree
from pootle_app.models.core import Project
from django.conf import settings


def test_get_project():
    pootle = Project.objects.get(code='pootle')
    assert project_tree.get_project(settings.PODIRECTORY + '/pootle/en', None) == pootle
    assert project_tree.get_project(settings.PODIRECTORY + '/pootle/en', pootle) == pootle


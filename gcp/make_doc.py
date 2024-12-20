#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2011 Tom SF Haines

# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.



from . import gcp

from .utils import doc_gen



# Setup...
doc = doc_gen.DocGen('gcp', 'Gaussian Conjugate Prior', 'Library of distributions focused on the Gaussian and its conjugate prior')
doc.addFile('readme.txt', 'Overview')


# Classes...
doc.addClass(gcp.Gaussian)
doc.addClass(gcp.GaussianInc)
doc.addClass(gcp.Wishart)
doc.addClass(gcp.StudentT)
doc.addClass(gcp.GaussianPrior)

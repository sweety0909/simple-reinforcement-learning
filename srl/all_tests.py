#!/usr/bin/env python3

# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from srl import context_test
from srl import grid_test
from srl import policy_gradient_test
from srl import simulation_test
from srl import world_test


def load_tests(loader, unused_tests, unused_pattern):
  # pylint: disable=unused-argument
  test_modules = [
      context_test,
      grid_test,
      policy_gradient_test,
      simulation_test,
      world_test,
    ]
  return unittest.TestSuite(map(loader.loadTestsFromModule, test_modules))


if __name__ == '__main__':
  unittest.main()

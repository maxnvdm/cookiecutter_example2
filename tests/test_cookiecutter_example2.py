#!/usr/bin/env python

"""Tests for `cookiecutter_example2` package."""


import unittest
from click.testing import CliRunner

from cookiecutter_example2 import cookiecutter_example2
from cookiecutter_example2 import cli


class TestCookiecutter_example2(unittest.TestCase):
    """Tests for `cookiecutter_example2` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'cookiecutter_example2.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

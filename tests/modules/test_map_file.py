#! /usr/bin/env python3
# coding: utf-8

"""Test the map importation."""

from core.modules.map_file import import_map


def test_map_file():
    """Test the importation."""
    assert import_map()

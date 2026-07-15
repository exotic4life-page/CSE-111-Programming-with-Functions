# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def make_full_name(given_name, family_name):
    """Return a string in this form "family_name; given_name"."""

    full_name = f"{family_name}; {given_name}"
    return full_name


def extract_family_name(full_name):
    """Extract and return the family name."""

    semicolon_index = full_name.index("; ")
    family_name = full_name[0:semicolon_index]
    return family_name


def extract_given_name(full_name):
    """Extract and return the given name."""

    semicolon_index = full_name.index("; ")
    given_name = full_name[semicolon_index + 2:]
    return given_name
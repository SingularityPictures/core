"""Host API required Work Files tool"""
import os

import nuke
from nukescripts import *

def file_extensions():
    return [".nk", ".nknc"]


def has_unsaved_changes():
    if nuke.Root().name() == 'Root':
        return "NOT SAVED"

    return normalised

def save(filepath):
    nuke.scriptSaveAs(filepath)


def open(filepath):
    if nuke.Root().modified():
        result = self.save_changes_prompt()

        if result is None:
            return False
        if result:
            nuke.scriptSave()

    nuke.scriptClear()
    nuke.scriptOpen(filepath)

    return True


def current_file():
    current_file = nuke.root().name()
    normalised = os.path.normpath(current_file)

    # Unsaved current file
    if nuke.Root().name() == 'Root':
        return "NOT SAVED"

    return normalised


def work_root():
    from avalon import api
    return os.path.join(api.Session["AVALON_WORKDIR"], "scenes")

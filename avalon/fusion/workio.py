"""Host API required Work Files tool"""
import sys


def file_extensions():
    return [".comp"]


def has_unsaved_changes():
    from avalon.fusion.pipeline import get_current_comp

    comp = get_current_comp()
    return comp.GetAttrs()["COMPB_Modified"]


def save(filepath):
    from avalon.fusion.pipeline import get_current_comp

    comp = get_current_comp()
    comp.Save(filepath)


def open(filepath):
    # Hack to get fusion, see avalon.fusion.pipeline.get_current_comp()
    fusion = getattr(sys.modules["__main__"], "fusion", None)

    return fusion.LoadComp(filepath)


def current_file():
    from avalon.fusion.pipeline import get_current_comp

    comp = get_current_comp()
    current_filepath = comp.GetAttrs()["COMPS_FileName"]
    if not current_filepath:
        return None

    return current_filepath


def work_root():
    from avalon import api

    return os.path.join(api.Session["AVALON_WORKDIR"], "scenes")
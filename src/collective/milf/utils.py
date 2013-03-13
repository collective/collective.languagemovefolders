# -*- coding: utf-8 -*-
from plone import api


def move_all():
    portal = api.portal.get()
    portal_languages = portal.portal_languages
    langs = portal_languages.getAvailableLanguages()
    results = []
    for lang in langs:
        if not getattr(portal, lang, None):
            results.append(u"{0} language doesn't exists, please call \
                the LinguaPlone view: @@language-setup-folders".format(lang))
        else:
            # XXX: copy portlets
            folder_language = getattr(portal, lang)
            objects = prepare_moving(portal, langs)
            for obj in objects[lang]:
                api.content.move(source=obj, target=folder_language)
                results.append("{0} had moved".format(obj.getId()))

    return "<br />".join(results)


def prepare_moving(site, langs):
    """ return a dict with languages as key (fr, en, nl, ...) and object,
    in language of the key, which are in the root of the Plone site, as values.
    """
    results = {}
    for lang in langs:
        results[lang] = []
    root_objects = site.contentValues()
    for root_object in root_objects:
        if root_object.id not in langs:
            results[root_object.getLanguage()].append(root_object)
    return results

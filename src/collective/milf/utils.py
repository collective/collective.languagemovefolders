# -*- coding: utf-8 -*-
from AccessControl import getSecurityManager
from AccessControl import Unauthorized
from Products.CMFCore.permissions import ModifyPortalContent


def move_all(portal):
    sm = getSecurityManager()
    if not sm.checkPermission(ModifyPortalContent, portal):
        error = 'You need ModifyPortalContent permissionto execute some_\
                function'
        raise Unauthorized(error)

    portal_languages = portal.portal_languages
    langs = portal_languages.getAvailableLanguages()
    results = []
    for lang in langs:
        if not getattr(portal, lang, None):
            results.append(u"{0} language folder doesn't exists, please call \
                the LinguaPlone view: @@language-setup-folders".format(lang))
        else:
            # XXX: copy portlets
            folder_language = getattr(portal, lang)
            objects = prepare_moving(portal, langs)
            for obj in objects[lang]:
                folder_language.manage_pasteObjects(
                               obj.aq_parent.manage_cutObjects(obj.getId()))
                results.append("{0} was moved".format(obj.getId()))

    return "<br />".join(results)


def prepare_moving(site, langs):
    """ return a dict with languages as key (fr, en, nl, ...) and object,
    in language of the key, which are in the root of the Plone site, as values.
    """
    objects = {}
    for lang in langs:
        objects[lang] = []
    root_objects = site.contentValues()
    for root_object in root_objects:
        if root_object.id not in langs:
            objects[root_object.getLanguage()].append(root_object)
    return objects

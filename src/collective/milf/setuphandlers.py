from plone import api
import os


def setupVarious(context):
    if context.readDataFile('collective.milf_various.txt') is None:
        return
    site = context.getSite()

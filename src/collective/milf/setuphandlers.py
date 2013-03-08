from plone import api
import os


def setupVarious(context):
    if context.readDataFile('collective.milf_various.txt') is None:
        return

    site = context.getSite()

    if os.environ['DEPLOY_ENV'] == 'dev':
        folder1_fr = api.content.create(
                    type='Folder',
                    title=u'dossier1 fr',
                    container=site,
                    language='fr',
                  )
        doc1_fr = api.content.create(
                type='Document',
                title=u'doc1 nl',
                container=folder1_fr,
                language='fr',
                )

        folder1_nl = api.content.create(
                    type='Folder',
                    title=u'dossier1 nl',
                    container=site,
                    language='nl',
                  )
        folder1_nl.addTranslationReference(folder1_fr)

        doc1_nl = api.content.create(
                type='Document',
                title=u'doc1 nl',
                container=folder1_nl,
                language='nl',
                )
        doc1_nl.addTranslationReference(doc1_fr)

        folder1_en = api.content.create(
                    type='Folder',
                    title=u'dossier1 en',
                    container=site,
                    language='en',
                  )
        folder1_en.addTranslationReference(folder1_fr)

        doc1_en = api.content.create(
                type='Document',
                title=u'doc1 en',
                container=folder1_en,
                language='en',
                )
        doc1_en.addTranslationReference(doc1_fr)

#! /usr/bin/env python
import dddi

def sortme(a, b):
    return cmp(a['lastname'], b['lastname'])

investigators = dddi.investigators
investigators.sort(sortme)
investigators.reverse()

for d in investigators:
    keys = d.keys()
    
    print ''
    print '`Dr. %(firstname)s %(lastname)s, %(affiliation)s <%(site)s>`__' % d

    keys.remove('firstname')
    keys.remove('lastname')
    keys.remove('affiliation')
    keys.remove('site')

    if 'title' in d:
        if 'proposal_url' in d:
            keys.remove('proposal_url')
            print '\nProposal: `%s <%s>`__' % (d['title'], d['proposal_url'])
        else:
            print '\nProposal title: %s' % d['title']
            
        keys.remove('title')

    if 'source' in d:
        print '\nSource code repository: %s' % d['source']
        keys.remove('source')

    if 'gscholar' in d:
        print '\nGoogle Scholar: %s' % d['gscholar']
        keys.remove('gscholar')

    if 'impactstory' in d:
        print '\nImpactStory: %s' % d['impactstory']
        keys.remove('impactstory')

    if 'blog' in d:
        print '\nBlog: %s' % d['blog']
        keys.remove('blog')

    if 'twitter' in d:
        print '\nTwitter: `@%s <https://twitter.com/%s>`__' % (d['twitter'],
                                                               d['twitter'],)
        keys.remove('twitter')
        
    print ''
    print '----'

    if 'abstract' in keys:
        keys.remove('abstract')
    if 'other_url' in keys:
        keys.remove('other_url')
    if 'presentation' in keys:
        keys.remove('presentation')
        
    assert not keys, keys
    

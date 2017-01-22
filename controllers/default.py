# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import Catalog
import Transcript
import Scoreboard
import Schedule
import random

def index():
    requirements = '(("CMPS 12A" or ("CMPS 5J" and "CMPS 11") or "CMPS 13" ) and ("CMPS 12B" or "CMPS 13H") and (("MATH 19A" or "MATH 19B") and ("MATH 19B" or "MATH ") and ("MATH 23A")) and ("CMPE 16") and ("CMPE 12") and ("AMS 10" or "MATH 21") and ( (("PHYS 5A" or "PHYS 6A") and (("PHYS 5B or PHYS 6B") or ("PHYS 5C" or "PHYS 6C")) ) or (("CHEM 1A") and (("CHEM 1B" or "CHEM 1C")) )) and ("CMPE 110")  and ("CMPS 101") and ("CMPS 104") and ("CMPS 111") and ("CMPS 102") and ("CMPS 112") and ("CMPS 130") and ("CMPS 115" or ("CMPS 132" or "CMPS 132W") or ("CMPS 180" or "CMPS 180W") or "CMPS 185" or "CMPS 195" or "CMPE 185") or "CMPS 105" or "CMPS 107" or "CMPS 109" or "CMPS 115" or "CMPS 116" or "CMPS 117" or "CMPS 119" or "CMPS 121" or "CMPS 122" or "CMPS 128" or "CMPS 129" or "CMPS 132" or "CMPS 140" or "CMPS 142" or "CMPS 143" or "CMPS 146" or "CMPS 148" or "CMPS 160" or "CMPS 161" or "CMPS 162" or "CMPS 164" or "CMPS 165" or "CMPS 166A" or "CMPS 166B" or "CMPS 170" or "CMPS 171" or "CMPS 172" or "CMPS 177" or "CMPS 178" or "CMPS 179" or "CMPS 180" or "CMPS 181" or "CMPS 182" or "CMPS 183" or "CMPS 185" or "CMPS 190X" or "CMPS 191" or "CMPS 194")'
    transcript = Transcript.Transcript()
    scoreboard = Scoreboard.Scoreboard()
    schedule = Schedule.Schedule(transcript, requirements)

    #while not schedule.is_done():
    for i in range(8):
        scoreboard.rate()
        schedule.build(scoreboard)

    return dict(
            schedule=schedule.quarters
            )

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()



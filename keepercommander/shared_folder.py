#  _  __  
# | |/ /___ ___ _ __  ___ _ _ ®
# | ' </ -_) -_) '_ \/ -_) '_|
# |_|\_\___\___| .__/\___|_|
#              |_|            
#
# Keeper Commander 
# Copyright 2017 Keeper Security Inc.
# Contact: ops@keepersecurity.com
#

class SharedFolder:
    """Defines a Keeper Shared Folder"""

    def __init__(self,shared_folder_uid='',revision='',default_manage_records=False,
                 default_manage_users=False,default_can_edit=False,default_can_share=False,
                 name='',records=[],users=[],teams=[]):
        self.shared_folder_uid = shared_folder_uid 
        self.revision = revision
        self.default_manage_records = default_manage_records 
        self.default_manage_users = default_manage_users 
        self.default_can_edit = default_can_edit 
        self.default_can_share = default_can_share 
        self.name = name 
        self.records = records 
        self.users = users 
        self.teams = teams 

    def load(self,sf,revision=''):
        self.default_manage_records = sf['default_manage_records']
        self.default_manage_users = sf['default_manage_users']
        self.default_can_edit = sf['default_can_edit']
        self.default_can_share = sf['default_can_share']
        self.name = sf['name']

        if 'records' in sf:
            self.records = sf['records']
        else:
            self.records = []

        if 'users' in sf:
            self.users = sf['users']
        else:
            self.users = []

        if 'teams' in sf:
            self.teams = sf['teams']
        else:
            self.teams = []

        self.revision = revision

    def display(self):
        print('') 
        print('{0:>20s}: {1:<20s}'.format('Shared Folder UID',self.shared_folder_uid))
        print('{0:>20s}: {1}'.format('Name',self.name))
        print('{0:>20s}: {1}'.format('Default Manage Records',self.default_manage_records))
        print('{0:>20s}: {1}'.format('Default Manage Users',self.default_manage_users))
        print('{0:>20s}: {1}'.format('Default Can Edit',self.default_can_edit))
        print('{0:>20s}: {1}'.format('Default Can Share',self.default_can_share))
        print('')
        print('{0:>20s}:'.format('Record Permissions'))

        if len(self.records) > 0:
            for r in self.records:
                print('{0:>20s}: {1}: {2}, {3}: {4}'.format(r['record_uid'],'Can Edit',r['can_edit'],'Can Share',r['can_share']))

        print('')
        print('{0:>20s}:'.format('User Permissions'))

        if len(self.users) > 0:
            for u in self.users:
                print('{0:>20s}: {1}: {2}, {3}: {4}'.format(u['username'],'Can Manage Records',u['manage_records'],'Can Manage Users',u['manage_users']))

        print('')
        print('{0:>20s}:'.format('Team Permissions'))

        if len(self.teams) > 0:
            for t in self.teams:
                print('{0:>20s}: {1}: {2}, {3}: {4}'.format(t['name'],'Can Manage Records',t['manage_records'],'Can Manage Users',t['manage_users']))

        print('')

    def to_string(self):
        target = self.shared_folder_uid + str(self.users) + str(self.teams)
        return target

    def to_lowerstring(self):
        keywords = [self.shared_folder_uid, self.name]
        if self.users:
            for u in self.users:
                keywords.append(u['username'])
        if self.teams:
            for t in self.teams:
                keywords.append(t['name'])
                keywords.append(t['team_uid'])
        keywords = [x.lower() for x in keywords]
        return '\n'.join(keywords)

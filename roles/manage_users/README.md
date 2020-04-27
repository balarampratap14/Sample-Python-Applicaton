This role will be used to create and delete users. This role is desiged by focusing below three conditions.

   * We should be able to grant users access based on servers role/group
   * We should be able to specify whether user has root permissions or not (based on group)
   * Role should remove all users if not mentioned in group vars (be careful with admin user)




Default Variables

    
     do_not_delete_users: By default this role deleted all normal users which are not defined in devops_users variable
                          so this variable is the list of all users which are not defined in devops_users variable 
                          and you don't want to delete them. Ex. admin, katim, jenkins etc..
                             
Define group for a environment:

user_groups:
  - name: devops
    root: True

  - name: qateam-readonly
    root: False

  - name: qateam
    root: True


users:
  - name: pawel.grzegrzolka
    servers:
      - all
    group: devops

  - name: iyad.shekha
    servers:
      - all
    group: devops-readonly

  - name: rajesh.ramachandran
    servers:
      - all
    group: qa
    expire: 1572566399

  - name: jesus.reyes
    servers:
      - all
    group: qa



    name: User will be crated with this name
    servers: list of hostgroup name like darkchat, darkmail. The users will be created only on defined hostgroup
             if you want to create user on all groups just define all in servers.
    group: Group name defined in user_groups variable.
    expire: This is optional value. Default value is -1 which means there is no account expire limit. It accepts value in epoch time.
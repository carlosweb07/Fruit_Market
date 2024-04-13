def is_admin(user):
    return user.groups.filter(name="Administrador").exists()
  
def is_manager(user):
    return user.groups.filter(name="Gestor").exists()

def is_user(user):
    return user.groups.filter(name="Usuario").exists()
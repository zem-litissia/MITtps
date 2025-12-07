class StadiumAccess:
    """Représente l'accès réel au stade"""
    def enter_stadium(self):
        print("Accès autorisé au stade")

class StadiumAccessProxy:
    """Proxy qui vérifie le passe sanitaire avant d'autoriser l'accès"""
    def __init__(self, stadium_access):
        self._stadium_access = stadium_access
    
    def check_health_pass(self, health_pass):
        """Vérifie si le passe sanitaire est valide"""
        # Simulation de la vérification du passe sanitaire
        return health_pass == "valid"
    
    def enter_stadium(self, health_pass):
        if self.check_health_pass(health_pass):
            print("Passe sanitaire valide")
            self._stadium_access.enter_stadium()
        else:
            print("Accès refusé : passe sanitaire invalide")

# Utilisation
stadium_access = StadiumAccess()
proxy = StadiumAccessProxy(stadium_access)

# Test avec un passe sanitaire valide
proxy.enter_stadium("valid")

# Test avec un passe sanitaire invalide
proxy.enter_stadium("invalid")
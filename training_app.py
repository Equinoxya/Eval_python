class TrainingApp:
    
    
    def __init__(self, services):
        self.running=True
        self.service = services
    
    def start(self):
        while self.running:
            self.print_menu()
            choice = input("Votre choix : ")
            self.handle_choice(choice)
    
    def print_menu(self):
        print()
        print("== Studio Booking Manager ==")
        print("1. Ajouter une cours")
        print("2. Afficher les cours")
        print("3. Inscrire une personne")
        print("4. Afficher les cours complets")
        print("5. Quitter")
    
    def handle_choice(self, choice):
        match choice:
            case "1":
                self.menu_add_training()
            case "2":
                self.menu_display_all_training()
            case "3":
                self.menu_register_someone()
            case "4":
                self.menu_display_full_training()
            case "5":
                print("Fermeture du gestionnaire de cours")
                self.running=False
            case _:
                print("Choix invalide")
     
    def menu_display_all_training(self):
        training = self.service.get_all_training()
        self.display_training(training)
        
    def menu_display_full_training(self):
        training = self.service.get_full_training()
        self.display_training(training)
                
    def menu_add_training(self):
        name = input("Nom du cours : ")
        coach_name = input("Nom du coach : ")
        capacity_max = input("Capacité maxi : ")
        price = input("Prix d'un cours : ")
        
        try:
            capacity_max =int(capacity_max)
        except ValueError:
            print('Capacité invalide')
            return
        
        try:
            price = float(price)
        except ValueError:
            print("Prix invalide")
            return
        
        
        success, message = self.service.add_training(name, coach_name, capacity_max, price)
        if not success:
            print("ERREUR !")
        print(message)
     
    def display_training(self, trainings):
         if len(trainings) == 0:
             print("Aucun cours à afficher.")
             return
         for training in trainings:
             print()
             print(f"Cours n°{training.id} - {training.name}")
             print(f"Type : {training.coach}")
             print(f"Prix : {training.price} €")
             print(f"Places occupées : {training.registered_count}")
             print(f'Places restantes : {training.capacity - training.registered_count} / {training.capacity}')
             print(f'CA actuel: {training.price * training.registered_count} €')
             print(f'CA potentiel : {training.price * training.capacity} €')
    def menu_register_someone(self):
        id_training = input("Quel est l'identifiant du cours ? ")
        try:
            id_training = int(id_training)
        except ValueError:
            print('Identifiant invalide')
            return
        success, message = self.service.register_someone(id_training)
        if not success:
            print("ERREUR !")
        print(message)
        
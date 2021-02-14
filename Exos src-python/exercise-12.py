# exercise-12-solution.py

# exo 12.1
# Créez une classe nommée `User` qui possède les attributs suivants :
# - firstname: valeur par défaut ''
# - lastname: valeur par défaut ''
# - email: valeur par défaut ''
# - newsletter: valeur par défaut False
# et la méthode suivante :
# - __init__() : le constructeur
# Ne créez pas de getters et de setters

# réponse 12.1
class User:
    """Définition d'un compte utilisateur"""
    def __init__(self, firstname ='', lastname ='', email ='', newsletter =False):
        """Constructeur de la classe User"""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.newsletter = newsletter
        
# exo 12.2
# Créez 4 instances de la classe `User` et affectez les valeurs suivantes à ses attributs :
# - user1
#   - firstname: Joe
#   - lastname: Dalton
#   - email: joe.dalton@example.com
#   - newsletter: true
# - user2
#   - firstname: William
#   - lastname: Dalton
#   - email: william.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Jack
#   - lastname: Dalton
#   - email: jack.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Avrel
#   - lastname: Dalton
#   - email: avrel.dalton@example.com
#   - newsletter: true

# réponse 12.2
print("\nExo 12.2")

user1 = User("Joe", "Dalton", "joe.dalton@example.com", True)
user2 = User("William", "Dalton", "william.dalton@example.com", False)
user3 = User("Jack", "Dalton", "jack.dalton@example.com", False)
user4 = User("Avrel", "Dalton", "avrel.dalton@example.com", True)

print(user1.firstname, user1.lastname, user1.email, user1.newsletter)
print(user2.firstname, user2.lastname, user2.email, user2.newsletter)
print(user3.firstname, user3.lastname, user3.email, user3.newsletter)
print(user4.firstname, user4.lastname, user4.email, user4.newsletter)

# exo 12.3
# Ajoutez chacune des instances de la classe `User` à une liste nommée `users`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom complet et l'email 
# de chaque utilisateur s'il est abonné à la newsletter

# réponse 12.3
print("\nExo 12.3")
users = [user1, user2, user3, user4]

print("Est abonné à la newsletter:")
print(" \nPrénom Nom   Adresse Mail")

for i in range(len(users)):
    if users[i].newsletter == True:
        print(f" {users[i].firstname} {users[i].lastname} {users[i].email}")
  
# exo 12.4
# Créez une classe nommée `ProductLorem` qui possède les attributs suivants :
# - _name: valeur par défaut ''
# - _price: valeur par défaut 0.0
# et les méthodes suivantes :
# - __init__() : le constructeur
# - get_name() : renvoit le nom du produit
# - set_name() : détermine le nom du produit
# - get_price() : renvoit le prix du produit
# - set_price() : détermine le prix du produit

# réponse 12.4
print("\nExo 12.4:")

class ProductLorem:
    """Définition du nom d'un produit et de son prix"""
    def __init__(self):
        self._name = ''
        self._price = 0.0
    # renvoit le nom du produit
    def get_name(self):
        return self._name
    # détermine le nom du produit  
    def set_name(self, name):
        self._name = name
    # renvoit le prix du produit
    def get_price(self):
        return self._price
    # détermine le prix du produit
    def set_price(self, price):
        self._price = price

# exo 12.5
# Créez 3 instances de la classe `ProductLorem` et affectez 
# les valeurs suivantes à ses attributs en utilisant les setters :
# - product1
#   - name: Foo
#   - price: 31,41
# - product2
#   - name: Bar
#   - price: 27,18
# - product3
#   - name: Baz
#   - price: 16,18

# réponse 12.5
print("\nExo 12.5:")

product1 = ProductLorem()
product1.set_name("Foo")
product1.set_price(31.41)
print(f"Nom: {product1.get_name()}, \nPrix: {product1.get_price()}")

product2 = ProductLorem()
product2.set_name("Bar")
product2.set_price(27.18)
print(f"\nNom: {product2.get_name()}, \nPrix: {product2.get_price()}")

product3 = ProductLorem()
product3.set_name("Baz")
product3.set_price(16.18)
print(f"\nNom: {product3.get_name()}, \nPrix: {product3.get_price()}")

# exo 12.6
# Ajoutez chacune des instances de la classe `ProductLorem` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom et le prix de chaque produit
# Calculez la somme du prix des produits et affichez-en un arrondi à 2 chiffres après la virgule, 
# après la boucle `for`

# réponse 12.6
print("\nExo 12.6: ")
products = [product1, product2, product3]
total_price = 0

print("Produit :")
print("Nom   Prix")

for i in range(len(products)):
    print(f" {products[i].get_name()} {products[i].get_price()}")
    total_price += products[i].get_price()
    
print(f"\nSomme du prix des produits: %.2f" % total_price)
    
# exo 12.7
# Créez une classe nommée `ProductIpsum` qui possède les attributs suivants :
# - _name: valeur str transmise par le constructeur
# - _price: valeur float par défaut 0.0
# - _tax: valeur float par défaut 0.0
# et les méthodes suivantes :
# - __init__(name, price, tax) : le constructeur
# - get_name() : renvoit le nom du produit
# - set_name() : détermine le nom du produit
# - get_price() : renvoit le prix du produit
# - set_price() : détermine le prix du produit
# - get_tax() : renvoit la taxe en pourcentage
# - set_tax() :  détermine la taxe en pourcentage (pour une taxe de 20 %, le param!tre doit être 20.0)
# - get_tax_part() : cette méthode renvoit le montant de la taxe (pour un produit de 100 @ 
# et une taxe de 20 %, le résultat est 20.0)
# - get_tax_included_price() : cette méthode renvoit le prix taxe incluse (pour un produit 
# de 100 @ et une taxe de 20 %, le résultat est 120.0)

# réponse 12.7
print("\nExo 12.7 :")
class ProductIpsum:
    """Définition du nom d'un produit avec son prix et sa taxe"""
    def __init__(self, name: str ='', price: float =0.0, tax: float =0.0, taxed: float =0.0, priced: float =0.0):
        self._name = name
        self._price = price
        self._tax = tax
        self._taxed = taxed
        self._priced = priced
    # renvoit le nom du produit
    def get_name(self):
        return self._name
    # détermine le nom du produit
    def set_name(self, name):
        self._name = name
    # renvoit le prix du produit
    def get_price(self):
        return self._price
    # détermine le prix du produit
    def set_price(self, price):
        self._price = price
    # renvoit la taxe en pourcentage
    def get_tax(self):
        return self._tax
    # détermine la taxe en pourcentage (pour une taxe de 20 %, le paramètre doit être 20.0)
    def set_tax(self, tax: float):
        self._tax = tax
    # renvoit le montant de la taxe (pour un produit de 100 @ et une taxe de 20 %, le résultat est 20.0)
    def get_tax_part(self, price, tax: float):
        self._taxed = price * (tax / 100)
        return self._taxed
    # cette méthode renvoit le prix taxe incluse (pour un produit de 100 @ 
    # et une taxe de 20 %, le résultat est 120.0)
    def get_tax_included_price(self, price, tax: float):
        self._priced = price + (price * (tax / 100))
        return self._priced

# exo 12.8
# Créez 3 instances de la classe `ProductIpsum` et affectez les valeurs suivantes 
# à ses attributs en utilisant le constructeur :
# - product1
#   - name: Dolor
#   - price: 31,41
#   - tax: 20.0
# - product2
#   - name: Sit
#   - price: 27,18
#   - tax: 10.0
# - product3
#   - name: Amet
#   - price: 16,18
#   - tax: 5.5

# réponse 12.8
print("\nExo 12.8 :")
print("Nom   Prix  Taxe")

product1 = ProductIpsum("Dolor", 31.41, 20.0)
product2 = ProductIpsum("Sit", 27.18, 10.0)
product3 = ProductIpsum("Amet", 16.18, 5.5)

print(product1.get_name(),product1.get_price(),product1.get_tax())
print(product2.get_name(),product2.get_price(),product2.get_tax())
print(product3.get_name(),product3.get_price(),product3.get_tax())

# exo 12.9
# Ajoutez chacune des instances de la classe `ProductIpsum` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom, le prix (sans la taxe),
# la taxe et le produit taxe incluse de chaque produit
# Calculez :
# - la somme du prix des produits sans les taxes
# - la somme du montant des taxes
# - la somme du prix des produits taxes incluses
# Et affichez-les après la boucle `for`

# réponse 12.9
print("\nExo 12.9 :")
products = [product1, product2, product3]

# la somme du prix des produits sans les taxes
total_price_excluding_vat = 0
# VAT = TVA 
# la somme du montant des taxes
total_tax = 0
# la somme du prix des produits taxes incluses
total_price_including_vat = 0

print("Produits :")
print("  Nom   Prix(Hors-TVA)  Taux de taxe   Prix(Avec TVA)")

for i in range(len(products)):
    print(f"  {products[i].get_name()}    {products[i].get_price()}€\
            {products[i].get_tax()}€\
        %.2f€" % products[i].get_tax_included_price(products[i].get_price(), products[i].get_tax()))

    total_price_excluding_vat += products[i].get_price()
    total_tax += products[i].get_tax_part(products[i].get_price(), products[i].get_tax())
    total_price_including_vat += products[i].get_tax_included_price(products[i].get_price(), products[i].get_tax())
    
print(f"\nSomme du prix des produits (hors TVA): %.2f€" % total_price_excluding_vat)
print(f"Somme du montant des taxes: %.2f€" % total_tax)
print(f"Somme du prix des produits (TVA incluse): %.2f€" % total_price_including_vat)
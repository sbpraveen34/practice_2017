from collections import defaultdict


products = defaultdict(int)

users = {}

users_products = defaultdict(list)


def addProduct(productname):
    products[productname]+=1

def userPurchaseProducts(user, productname):
    if productname in products:
        products[productname] -= 1
        users_products[user].append(productname)

def black_list(user):
    users[user].is_blacklisted = True

def best_selling_products():
    for productname in products.keys():
        is_product_best_selling = True
        for user, user_object in users.iteritems():
            if not user_object.is_blacklisted:
                if productname not in users_products[user]:
                    is_product_best_selling = False
                    

from .cart import Cart


def cart(request):
    return {'cart':Cart(request)} #this will pass the cart to any page of website
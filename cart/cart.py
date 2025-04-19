class Cart():
    def __init__(self,request):
        self.session=request.session

        #get the current session key if it exists
        cart=self.session.get('session_key')
       
       #if its a new user, create a session key
        if 'session_key' not in request.session:
         cart= self.session['session_key']={}

        #make sure cart is available in all pages
        self.cart= self
    def add(self,product):
       product_id=str(product.id)
       if product_id in self.cart:
          pass
       else:
          self.cart[product_id]={'price':str(product.price)}

       self.session.modified=True

    def __len_(self):
      return len(self.cart)
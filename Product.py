class Product:
    def __init__(self, id: int, name: str, description: str, image_url: str, price: int, url: str, location: str,
                 uploaded_at: str, pay_livery: bool):
        self.id = id
        self.name = name
        self.description = description
        self.image_url = image_url
        self.price = price
        self.url = url
        self.location = location
        self.uploaded_at = uploaded_at
        self.pay_livery = pay_livery

    def __str__(self):
        return f'Product[{self.id} | {self.name} for {self.price} in {self.location}]'

    def __repr__(self):
        return f'Product[{self.id} | {self.name} | {self.description} | {self.image_url} | {self.price} | {self.url} | {self.location} | {self.uploaded_at} | {self.pay_livery}]'

    def __eq__(self, other):
        return self.id == other.id

